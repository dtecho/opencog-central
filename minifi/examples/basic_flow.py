
"""
Basic MiniNiFi Flow Example
Demonstrates a simple data generation and logging flow
"""

import asyncio
import yaml
from pathlib import Path

# Example flow configuration
BASIC_FLOW_CONFIG = {
    'id': 'basic-demo-flow',
    'name': 'Basic Demo Flow',
    'processors': [
        {
            'id': 'generate-data',
            'type': 'GenerateFlowFile',
            'properties': {
                'interval': '3.0',
                'format': 'json'
            }
        },
        {
            'id': 'log-data',
            'type': 'LogAttribute',
            'properties': {
                'log_level': 'INFO',
                'log_content': 'true',
                'max_content_length': '512'
            }
        }
    ],
    'connections': [
        {
            'source': 'generate-data',
            'destination': 'log-data',
            'relationship': 'success'
        }
    ]
}

async def run_basic_example():
    """Run the basic flow example"""
    from ..core.agent import MiniNiFiAgent
    
    # Create temporary config
    config = {
        'agent': {
            'id': 'demo-agent',
            'name': 'Demo MiniNiFi Agent'
        },
        'server': {'port': 8081, 'host': '0.0.0.0'},
        'logging': {'level': 'INFO'},
        'api': {'enabled': True, 'port': 8081}
    }
    
    # Save temporary config
    config_path = 'minifi/config/demo.yaml'
    Path(config_path).parent.mkdir(parents=True, exist_ok=True)
    with open(config_path, 'w') as f:
        yaml.dump(config, f)
    
    # Create and start agent
    agent = MiniNiFiAgent(config_path)
    await agent.initialize()
    
    # Create the basic flow
    flow_id = await agent.create_flow(BASIC_FLOW_CONFIG)
    
    # Start agent
    await agent.start()
    
    print(f"Basic flow example started. Flow ID: {flow_id}")
    print("The flow will generate data every 3 seconds and log it.")
    print("Check the logs to see the generated data.")
    print("REST API available at http://0.0.0.0:8081")
    print("Try: curl http://localhost:8081/status")
    
    try:
        # Run for demo purposes
        await asyncio.sleep(30)
    finally:
        await agent.stop()

if __name__ == "__main__":
    asyncio.run(run_basic_example())

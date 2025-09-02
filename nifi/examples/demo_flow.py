
#!/usr/bin/env python3
"""
Demonstration of NiFi flow creation and execution
"""

import asyncio
import logging
from nifi.core.flow_engine import FlowEngine
from nifi.atomspace.connector import AtomSpaceConnector

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

async def create_demo_flow():
    """Create and run a demonstration flow"""
    
    # Initialize components
    engine = FlowEngine()
    atomspace = AtomSpaceConnector()
    
    # Connect to AtomSpace
    await atomspace.connect()
    engine.register_atomspace(atomspace)
    
    # Create a new flow
    flow_id = engine.create_flow("Demo Cognitive Flow", "Demonstrates cognitive processing")
    
    # Add processors to the flow
    generator_id = engine.add_processor(flow_id, "GenerateFlowFile", {
        "content": "This is sample text for cognitive analysis",
        "format": "text",
        "interval_seconds": 10
    })
    
    cognitive_id = engine.add_processor(flow_id, "CognitiveProcessor", {
        "operation": "analyze"
    })
    
    logger_id = engine.add_processor(flow_id, "LogAttribute", {
        "log_level": "INFO",
        "log_content": True,
        "max_content_length": 500
    })
    
    atomspace_writer_id = engine.add_processor(flow_id, "AtomSpaceWriter", {
        "atom_type": "ConceptNode"
    })
    
    # Create connections between processors
    engine.create_connection(generator_id, cognitive_id, "success")
    engine.create_connection(cognitive_id, logger_id, "success") 
    engine.create_connection(cognitive_id, atomspace_writer_id, "success")
    
    # Start the flow
    await engine.start_flow(flow_id)
    
    logger.info("Demo flow created and started!")
    logger.info(f"Flow ID: {flow_id}")
    
    # Let it run for a while
    await asyncio.sleep(30)
    
    # Stop the flow
    await engine.stop_flow(flow_id)
    
    # Print final statistics
    stats = engine.get_engine_stats()
    logger.info(f"Final stats: {stats}")
    
    # Cleanup
    await atomspace.disconnect()

if __name__ == "__main__":
    asyncio.run(create_demo_flow())

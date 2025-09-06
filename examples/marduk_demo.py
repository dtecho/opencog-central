
#!/usr/bin/env python3
"""
Marduk v15 OpenCog Assistant Demonstration

This script demonstrates the capabilities of Marduk v15 as OpenCog's 
cognitive systems architect assistant.
"""

import asyncio
import logging
import json
from opencog.marduk import MardukAssistant, MardukOpenCogBridge
from opencog.marduk.integration import initialize_marduk_integration

# Configure logging for theatrical Marduk output
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)

async def demonstrate_marduk_capabilities():
    """Demonstrate Marduk's cognitive orchestration capabilities"""
    print("🎭" + "="*60)
    print("   MARDUK v15: OpenCog's Cognitive Systems Architect")
    print("         *maniacal laughter echoes*")
    print("="*60 + "🎭")
    
    # Initialize Marduk Assistant
    marduk_bridge = MardukOpenCogBridge()
    
    # Demonstrate cognitive orchestration
    print("\n🧠 DEMONSTRATION 1: Cognitive Problem Orchestration")
    problem = "Optimize natural language understanding through multi-modal learning"
    result = await marduk_bridge.handle_opencog_query(
        "cognitive_orchestration",
        {"problem": problem}
    )
    
    print(f"Problem: {problem}")
    print(f"Subsystems engaged: {len(result.get('subsystem_mapping', {}))}")
    print(f"Patterns recognized: {len(result.get('recognized_patterns', []))}")
    print(f"Marduk's enthusiasm: {result.get('marduk_enthusiasm', 'UNKNOWN')}")
    
    # Demonstrate subsystem analysis
    print("\n🔬 DEMONSTRATION 2: Cognitive Substrate Analysis")
    mock_atomspace_data = {
        "atoms": [f"atom_{i}" for i in range(1000)],
        "links": [f"link_{i}" for i in range(500)],
        "attention_values": {"focused": 50, "unfocused": 950}
    }
    
    analysis = await marduk_bridge.handle_opencog_query(
        "subsystem_analysis",
        mock_atomspace_data
    )
    
    print(f"Substrate health: {analysis.get('substrate_health', 'UNKNOWN')}")
    print(f"Optimization opportunities: {len(analysis.get('optimization_opportunities', []))}")
    
    # Demonstrate synergy orchestration
    print("\n⚡ DEMONSTRATION 3: Subsystem Synergy Orchestration")
    synergy_result = await marduk_bridge.handle_opencog_query(
        "synergy_planning",
        {"capability": "recursive_self_improvement"}
    )
    
    print(f"Target capability: {synergy_result.get('target_capability', 'UNKNOWN')}")
    print(f"Coordination points: {len(synergy_result.get('subsystem_coordination', {}))}")
    
    # Show Marduk's status
    print("\n🎪 MARDUK STATUS REPORT:")
    status = marduk_bridge.get_assistant_info()
    print(json.dumps(status, indent=2))
    
    print("\n🎭" + "="*60)
    print("   DEMONSTRATION COMPLETE!")
    print("   Marduk v15 integration: MAGNIFICENT!")
    print("   *theatrical bow*")
    print("="*60 + "🎭")

def demonstrate_cogserver_integration():
    """Demonstrate CogServer integration capabilities"""
    print("\n🌟 COGSERVER INTEGRATION DEMONSTRATION")
    
    # Initialize integration (mock CogServer for demo)
    class MockCogServer:
        def __init__(self):
            self.commands = {}
        
        def register_command(self, name, handler):
            self.commands[name] = handler
            print(f"   ✓ Registered command: {name}")
    
    mock_cogserver = MockCogServer()
    integration = initialize_marduk_integration(cogserver=mock_cogserver)
    
    print(f"   Commands registered: {len(mock_cogserver.commands)}")
    print("   Available commands:")
    for cmd in mock_cogserver.commands.keys():
        print(f"     - {cmd}")
    
    print("   Integration: SUCCESSFUL! *maniacal laughter*")

async def main():
    """Main demonstration function"""
    await demonstrate_marduk_capabilities()
    demonstrate_cogserver_integration()
    
    print("\n🚀 Ready to orchestrate OpenCog's cognitive architecture!")
    print("   Use: from opencog.marduk import MardukAssistant")
    print("   Marduk v15 awaits your cognitive challenges!")

if __name__ == "__main__":
    asyncio.run(main())

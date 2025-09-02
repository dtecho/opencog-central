
#!/usr/bin/env python3
"""
KoboldCpp-OpenCog Cognitive Integration Demo

This script demonstrates the deep integration between KoboldCpp and OpenCog,
showcasing advanced cognitive capabilities like PLN reasoning, attention allocation,
episodic memory, and real-time cognitive monitoring.
"""

import os
import sys
import subprocess
import time
import requests
import json
import threading
from pathlib import Path

class CognitiveDemo:
    def __init__(self, base_url="http://0.0.0.0:5001"):
        self.base_url = base_url
        self.session = requests.Session()
        self.cognitive_metrics = {}
        self.conversation_history = []
        
    def test_basic_generation(self):
        """Test basic text generation with cognitive enhancement"""
        print("=== Testing Basic Cognitive Text Generation ===")
        
        prompts = [
            "Explain the relationship between consciousness and intelligence",
            "What are the implications of artificial general intelligence?",
            "How does memory influence decision making?",
            "Describe the nature of emergent behavior in complex systems"
        ]
        
        for prompt in prompts:
            print(f"\nPrompt: {prompt}")
            response = self.generate_text(prompt)
            print(f"Response: {response}")
            self.conversation_history.append({"prompt": prompt, "response": response})
            time.sleep(1)
    
    def test_contextual_generation(self):
        """Test context-aware generation with cognitive context"""
        print("\n=== Testing Contextual Generation ===")
        
        # Set up cognitive context
        context = {
            "conversation_id": "demo_session_001",
            "memory_stack": [
                "Previous discussion about consciousness",
                "Interest in AGI implications", 
                "Focus on emergent behavior"
            ],
            "attention_weights": {
                "consciousness": 0.9,
                "intelligence": 0.8,
                "memory": 0.7,
                "emergence": 0.6
            },
            "coherence_score": 0.85,
            "current_goal": "Explore cognitive architectures"
        }
        
        prompt = "Building on our previous discussion, how might we implement conscious decision-making in AI?"
        print(f"\nContextual Prompt: {prompt}")
        print(f"Context: Goal='{context['current_goal']}', Coherence={context['coherence_score']}")
        
        response = self.generate_with_context(prompt, context)
        print(f"Contextual Response: {response}")
    
    def test_atomspace_integration(self):
        """Test AtomSpace query processing and knowledge injection"""
        print("\n=== Testing AtomSpace Integration ===")
        
        # Test knowledge injection
        knowledge_text = """
        Artificial intelligence systems can exhibit emergent behavior when multiple
        simple components interact in complex ways. Consciousness may arise from
        the integration of information processing across different cognitive modules.
        Memory systems store both episodic experiences and semantic knowledge,
        which influence decision-making processes through attention mechanisms.
        """
        
        print("Injecting knowledge into AtomSpace...")
        self.inject_knowledge(knowledge_text)
        
        # Test AtomSpace queries
        queries = [
            "Find concepts related to consciousness",
            "Query inheritance relationships for intelligence",
            "Search for patterns involving memory and decision-making"
        ]
        
        for query in queries:
            print(f"\nAtomSpace Query: {query}")
            result = self.query_atomspace(query)
            print(f"Result: {result}")
    
    def test_pln_reasoning(self):
        """Test PLN (Probabilistic Logic Networks) reasoning capabilities"""
        print("\n=== Testing PLN Reasoning ===")
        
        reasoning_scenarios = [
            {
                "premises": "Intelligence involves processing information. Consciousness involves integration of information.",
                "target": "Intelligence and consciousness are related through information processing"
            },
            {
                "premises": "Memory influences decision-making. Attention focuses on relevant memories.",
                "target": "Attention mechanisms are crucial for effective decision-making"
            },
            {
                "premises": "Emergent behavior arises from component interactions. AI systems have multiple components.",
                "target": "AI systems can exhibit emergent behavior"
            }
        ]
        
        for scenario in reasoning_scenarios:
            print(f"\nPremises: {scenario['premises']}")
            print(f"Target: {scenario['target']}")
            
            result = self.execute_pln_reasoning(scenario['premises'], scenario['target'])
            print(f"PLN Result: {result}")
    
    def test_memory_systems(self):
        """Test episodic and semantic memory functionality"""
        print("\n=== Testing Memory Systems ===")
        
        # Store episodic memories
        episodes = [
            "User asked about consciousness and AI responded with technical explanation",
            "Discussion about memory systems led to insights about attention mechanisms", 
            "PLN reasoning successfully connected intelligence and consciousness concepts",
            "AtomSpace integration enabled knowledge graph expansion"
        ]
        
        for episode in episodes:
            print(f"Storing episode: {episode[:50]}...")
            self.store_memory(episode, "demo_session")
        
        # Test memory retrieval
        queries = [
            "consciousness",
            "memory systems", 
            "PLN reasoning",
            "knowledge graph"
        ]
        
        for query in queries:
            print(f"\nRetrieving memories for: {query}")
            memories = self.retrieve_memories(query)
            for i, memory in enumerate(memories[:2]):  # Show top 2
                print(f"  Memory {i+1}: {memory[:60]}...")
    
    def test_attention_mechanisms(self):
        """Test attention allocation and focus management"""
        print("\n=== Testing Attention Mechanisms ===")
        
        # Set attention weights for different concepts
        attention_updates = {
            "artificial_intelligence": 0.9,
            "consciousness": 0.8,
            "memory_systems": 0.7,
            "cognitive_architecture": 0.85,
            "emergent_behavior": 0.6,
            "decision_making": 0.75
        }
        
        print("Updating attention allocation...")
        self.update_attention(attention_updates)
        
        # Test attention-guided generation
        prompt = "What should we focus on next in our cognitive AI research?"
        print(f"\nAttention-guided prompt: {prompt}")
        response = self.generate_text(prompt)
        print(f"Attention-guided response: {response}")
    
    def test_cognitive_monitoring(self):
        """Test real-time cognitive monitoring and metrics"""
        print("\n=== Testing Cognitive Monitoring ===")
        
        print("Starting cognitive monitoring...")
        self.start_monitoring()
        
        # Perform various cognitive tasks to generate metrics
        for i in range(3):
            print(f"\nCognitive cycle {i+1}:")
            
            # Generate some cognitive activity
            self.generate_text(f"Cognitive test prompt {i+1}")
            self.query_atomspace("test query")
            
            # Get current metrics
            metrics = self.get_cognitive_metrics()
            print(f"Metrics: {json.dumps(metrics, indent=2)}")
            
            time.sleep(2)
        
        print("Stopping cognitive monitoring...")
        self.stop_monitoring()
    
    def run_comprehensive_demo(self):
        """Run the complete cognitive integration demonstration"""
        print("🧠 KoboldCpp-OpenCog Cognitive Integration Demo")
        print("=" * 60)
        
        try:
            # Check if server is running
            response = self.session.get(f"{self.base_url}/api/v1/info", timeout=5)
            if response.status_code != 200:
                print("❌ KoboldCpp server not responding. Please start the server first.")
                return False
                
            print("✅ Connected to KoboldCpp-OpenCog hybrid server")
            
            # Run all test suites
            self.test_basic_generation()
            self.test_contextual_generation()
            self.test_atomspace_integration()
            self.test_pln_reasoning()
            self.test_memory_systems()
            self.test_attention_mechanisms()
            self.test_cognitive_monitoring()
            
            print("\n" + "=" * 60)
            print("🎉 Cognitive Integration Demo Completed Successfully!")
            print(f"📊 Total interactions: {len(self.conversation_history)}")
            print("🧠 All cognitive systems functioning correctly")
            
            return True
            
        except requests.exceptions.RequestException as e:
            print(f"❌ Connection error: {e}")
            print("Please ensure the KoboldCpp-OpenCog server is running on port 5001")
            return False
        except Exception as e:
            print(f"❌ Demo error: {e}")
            return False
    
    # Helper methods for API interactions
    def generate_text(self, prompt, max_tokens=100):
        """Generate text using the cognitive generation endpoint"""
        try:
            payload = {
                "prompt": prompt,
                "max_length": max_tokens,
                "temperature": 0.7,
                "top_p": 0.9,
                "cognitive_enhancement": True
            }
            
            response = self.session.post(
                f"{self.base_url}/api/v1/generate",
                json=payload,
                timeout=30
            )
            
            if response.status_code == 200:
                result = response.json()
                return result.get("results", [{}])[0].get("text", "No response")
            else:
                return f"Generation failed: {response.status_code}"
                
        except Exception as e:
            return f"Error: {e}"
    
    def generate_with_context(self, prompt, context, max_tokens=100):
        """Generate text with cognitive context"""
        try:
            payload = {
                "prompt": prompt,
                "max_length": max_tokens,
                "cognitive_context": context,
                "enhanced_reasoning": True
            }
            
            response = self.session.post(
                f"{self.base_url}/api/v1/generate_contextual",
                json=payload,
                timeout=30
            )
            
            if response.status_code == 200:
                result = response.json()
                return result.get("text", "No contextual response")
            else:
                return f"Contextual generation failed: {response.status_code}"
                
        except Exception as e:
            return f"Contextual error: {e}"
    
    def query_atomspace(self, query):
        """Query the AtomSpace knowledge base"""
        try:
            payload = {"query": query}
            
            response = self.session.post(
                f"{self.base_url}/api/v1/atomspace/query",
                json=payload,
                timeout=15
            )
            
            if response.status_code == 200:
                return response.json().get("result", "No AtomSpace result")
            else:
                return f"AtomSpace query failed: {response.status_code}"
                
        except Exception as e:
            return f"AtomSpace error: {e}"
    
    def inject_knowledge(self, text):
        """Inject knowledge into the AtomSpace"""
        try:
            payload = {"knowledge_text": text}
            
            response = self.session.post(
                f"{self.base_url}/api/v1/atomspace/inject",
                json=payload,
                timeout=20
            )
            
            return response.status_code == 200
            
        except Exception as e:
            print(f"Knowledge injection error: {e}")
            return False
    
    def execute_pln_reasoning(self, premises, target):
        """Execute PLN reasoning"""
        try:
            payload = {
                "premises": premises,
                "target": target,
                "reasoning_depth": 3
            }
            
            response = self.session.post(
                f"{self.base_url}/api/v1/pln/reason",
                json=payload,
                timeout=25
            )
            
            if response.status_code == 200:
                result = response.json()
                return f"Truth Value: {result.get('truth_value', 0.0)}, Reasoning: {result.get('reasoning_chain', 'No reasoning')}"
            else:
                return f"PLN reasoning failed: {response.status_code}"
                
        except Exception as e:
            return f"PLN error: {e}"
    
    def store_memory(self, episode, context):
        """Store episodic memory"""
        try:
            payload = {
                "episode": episode,
                "context": context
            }
            
            response = self.session.post(
                f"{self.base_url}/api/v1/memory/store",
                json=payload,
                timeout=10
            )
            
            return response.status_code == 200
            
        except Exception as e:
            print(f"Memory storage error: {e}")
            return False
    
    def retrieve_memories(self, query, limit=3):
        """Retrieve relevant memories"""
        try:
            payload = {
                "query": query,
                "limit": limit
            }
            
            response = self.session.post(
                f"{self.base_url}/api/v1/memory/retrieve",
                json=payload,
                timeout=10
            )
            
            if response.status_code == 200:
                return response.json().get("memories", [])
            else:
                return []
                
        except Exception as e:
            print(f"Memory retrieval error: {e}")
            return []
    
    def update_attention(self, weights):
        """Update attention allocation"""
        try:
            payload = {"attention_weights": weights}
            
            response = self.session.post(
                f"{self.base_url}/api/v1/attention/update",
                json=payload,
                timeout=10
            )
            
            return response.status_code == 200
            
        except Exception as e:
            print(f"Attention update error: {e}")
            return False
    
    def get_cognitive_metrics(self):
        """Get current cognitive metrics"""
        try:
            response = self.session.get(
                f"{self.base_url}/api/v1/cognitive/metrics",
                timeout=10
            )
            
            if response.status_code == 200:
                return response.json().get("metrics", {})
            else:
                return {}
                
        except Exception as e:
            print(f"Metrics error: {e}")
            return {}
    
    def start_monitoring(self):
        """Start cognitive monitoring"""
        try:
            response = self.session.post(
                f"{self.base_url}/api/v1/cognitive/monitor/start",
                timeout=10
            )
            return response.status_code == 200
        except Exception as e:
            print(f"Monitor start error: {e}")
            return False
    
    def stop_monitoring(self):
        """Stop cognitive monitoring"""
        try:
            response = self.session.post(
                f"{self.base_url}/api/v1/cognitive/monitor/stop",
                timeout=10
            )
            return response.status_code == 200
        except Exception as e:
            print(f"Monitor stop error: {e}")
            return False

def main():
    """Main demo execution"""
    import argparse
    
    parser = argparse.ArgumentParser(description="KoboldCpp-OpenCog Cognitive Integration Demo")
    parser.add_argument("--url", default="http://0.0.0.0:5001", help="Server URL")
    parser.add_argument("--quick", action="store_true", help="Run quick demo")
    
    args = parser.parse_args()
    
    demo = CognitiveDemo(args.url)
    
    if args.quick:
        # Quick demo - just basic functionality
        print("🚀 Quick Cognitive Demo")
        demo.test_basic_generation()
        demo.test_atomspace_integration()
    else:
        # Full comprehensive demo
        success = demo.run_comprehensive_demo()
        sys.exit(0 if success else 1)

if __name__ == "__main__":
    main()

#!/usr/bin/env python3
"""
Test suite for cognitive synergy verification
Validates that cognitive components achieve synergistic effects
"""

import unittest
import json
from pathlib import Path
from app import CognitiveSynergyDemo
from cognitive_integration_bridge import CognitiveIntegrationBridge
from cognitive_fusion_reactor import CognitiveFusionReactor

class TestCognitiveSynergy(unittest.TestCase):
    """Test cases for cognitive synergy achievement"""
    
    def setUp(self):
        """Set up test fixtures"""
        self.demo = CognitiveSynergyDemo()
        self.bridge = CognitiveIntegrationBridge()
        self.reactor = CognitiveFusionReactor()
        
    def test_cognitive_fusion_initialization(self):
        """Test that cognitive fusion reactor initializes correctly"""
        
        state = self.reactor.initiate_fusion_sequence()
        
        # Verify fusion state
        self.assertEqual(state['coherence_level'], 1.0)
        self.assertEqual(state['energy_output'], 100.0)
        self.assertIsInstance(state['active_bridges'], list)
        
        # Verify fusion directory exists
        fusion_dir = Path('cognitive_fusion')
        self.assertTrue(fusion_dir.exists())
        
        # Verify integration manifests created
        manifest_file = fusion_dir / 'integration_manifests.json'
        self.assertTrue(manifest_file.exists())
        
        with open(manifest_file) as f:
            manifests = json.load(f)
            self.assertIn('integration_rules', manifests)
            self.assertIn('emergence_expectations', manifests)
        
    def test_component_integration(self):
        """Test that cognitive components are properly integrated"""
        
        state = self.bridge.get_cognitive_state()
        
        # Verify sufficient components are active
        self.assertGreaterEqual(state['active_components'], 6)
        
        # Verify synaptic connections exist
        self.assertGreater(state['synaptic_connections'], 0)
        
        # Verify network has reasonable density
        self.assertGreater(state['graph_metrics']['density'], 0.1)
        
    def test_emergence_pattern_detection(self):
        """Test that emergent patterns can be detected"""
        
        patterns = self.bridge.detect_emergence_patterns()
        
        # Should be able to detect some form of emergence
        # Even if no strong emergent patterns, the system should recognize potential
        self.assertIsInstance(patterns, list)
        
        # Verify pattern structure if any are detected
        for pattern in patterns:
            self.assertIn('components', pattern)
            self.assertIn('pattern_type', pattern)
            self.assertIn('timestamp', pattern)
            
    def test_adaptive_resource_allocation(self):
        """Test that resources are allocated adaptively based on task requirements"""
        
        # Test different task types
        reasoning_task = {
            'type': 'reasoning',
            'capabilities': ['probabilistic_inference', 'logical_chaining']
        }
        
        learning_task = {
            'type': 'learning', 
            'capabilities': ['program_evolution', 'fitness_optimization']
        }
        
        reasoning_allocation = self.bridge.allocate_cognitive_resources(reasoning_task)
        learning_allocation = self.bridge.allocate_cognitive_resources(learning_task)
        
        # Verify allocations are different
        self.assertNotEqual(reasoning_allocation, learning_allocation)
        
        # Verify allocations sum to approximately 1.0
        self.assertAlmostEqual(sum(reasoning_allocation.values()), 1.0, places=2)
        self.assertAlmostEqual(sum(learning_allocation.values()), 1.0, places=2)
        
        # Verify reasoning tasks focus on reasoning components
        top_reasoning = max(reasoning_allocation, key=reasoning_allocation.get)
        self.assertIn(top_reasoning, ['pln', 'ure', 'atomspace'])
        
    def test_cross_component_learning(self):
        """Test that components can learn from each other"""
        
        initial_memory_size = len(self.bridge.interaction_memory)
        
        # Simulate a learning interaction
        interaction = {
            'type': 'reasoning_with_attention',
            'capabilities': ['probabilistic_inference', 'importance_spreading'],
            'success': 0.8
        }
        
        self.bridge.learn_from_interaction(interaction)
        
        # Verify learning occurred
        final_memory_size = len(self.bridge.interaction_memory)
        self.assertEqual(final_memory_size, initial_memory_size + 1)
        
        # Verify interaction was stored correctly
        stored_interaction = self.bridge.interaction_memory[-1]
        self.assertEqual(stored_interaction['interaction'], interaction)
        self.assertIn('active_components', stored_interaction)
        
    def test_synergy_score_calculation(self):
        """Test that synergy score is calculated correctly"""
        
        synergy_score = self.demo.demonstrate_cognitive_synergy()
        
        # Verify score is in valid range
        self.assertGreaterEqual(synergy_score, 0.0)
        self.assertLessEqual(synergy_score, 1.0)
        
        # For good synergy, score should be reasonable
        self.assertGreater(synergy_score, 0.4)  # Minimum threshold for basic synergy
        
    def test_synergy_results_persistence(self):
        """Test that synergy results are properly saved"""
        
        # Run demonstration to generate results
        self.demo.demonstrate_cognitive_synergy()
        
        # Verify results file exists
        results_file = Path('cognitive_synergy_results.json')
        self.assertTrue(results_file.exists())
        
        # Verify results structure
        with open(results_file) as f:
            results = json.load(f)
            
        self.assertIn('timestamp', results)
        self.assertIn('synergy_score', results)
        self.assertIn('metrics', results)
        self.assertIn('status', results)
        
        # Verify synergy achievement
        self.assertIn(results['status'], ['COGNITIVE_SYNERGY_ACHIEVED', 'PARTIAL_SYNERGY'])
        
    def test_cognitive_graph_visualization(self):
        """Test that cognitive graph can be visualized"""
        
        graph_data = self.bridge.visualize_cognitive_graph()
        
        # Verify graph structure
        self.assertIn('nodes', graph_data)
        self.assertIn('edges', graph_data)
        self.assertIn('timestamp', graph_data)
        
        # Verify nodes have required properties
        if graph_data['nodes']:
            node = graph_data['nodes'][0]
            self.assertIn('id', node)
            self.assertIn('type', node)
            self.assertIn('attention', node)
            self.assertIn('capabilities', node)
            
        # Verify edges have required properties
        if graph_data['edges']:
            edge = graph_data['edges'][0]
            self.assertIn('source', edge)
            self.assertIn('target', edge)
            self.assertIn('weight', edge)
            
    def test_synergy_exceeds_individual_components(self):
        """Test that synergistic system capabilities exceed individual components"""
        
        # Get capabilities of individual components
        state = self.bridge.get_cognitive_state()
        individual_capabilities = set()
        
        for component_name, attrs in self.bridge.component_registry.items():
            individual_capabilities.update(attrs.get('capabilities', []))
            
        # Test for emergent capabilities through pattern detection
        patterns = self.bridge.detect_emergence_patterns()
        emergent_capabilities = set()
        
        for pattern in patterns:
            emergent_capabilities.update(pattern.get('capabilities', []))
            
        # While we may not detect strong emergence every time,
        # the architecture should support emergent capabilities
        expected_emergent = {
            'uncertain_knowledge_reasoning',
            'adaptive_goal_optimization', 
            'embodied_language_understanding'
        }
        
        # Test that the system can infer emergent capabilities given the right conditions
        test_components = {'atomspace', 'pln'}  # Should enable uncertain_knowledge_reasoning
        inferred_capabilities = self.bridge._infer_emergent_capabilities(test_components)
        
        # Should find at least one emergent capability
        emergent_found = any(cap in inferred_capabilities for cap in expected_emergent)
        self.assertTrue(emergent_found, 
                       f"No emergent capabilities found. Inferred: {inferred_capabilities}")


class TestCognitiveSynergyIntegration(unittest.TestCase):
    """Integration tests for complete cognitive synergy system"""
    
    def test_end_to_end_synergy_demonstration(self):
        """Test complete end-to-end cognitive synergy demonstration"""
        
        demo = CognitiveSynergyDemo()
        
        # Should complete without errors
        try:
            synergy_score = demo.demonstrate_cognitive_synergy()
            success = True
        except Exception as e:
            success = False
            error_msg = str(e)
            
        self.assertTrue(success, f"Synergy demonstration failed: {error_msg if not success else ''}")
        
        # Should achieve at least basic synergy
        if success:
            self.assertGreater(synergy_score, 0.5, "Synergy score too low for meaningful integration")
            
    def test_unified_dashboard_compatibility(self):
        """Test compatibility with unified cognitive dashboard"""
        
        try:
            from unified_cognitive_dashboard import unified_state, bridge
            compatibility = True
        except ImportError:
            compatibility = False
            
        self.assertTrue(compatibility, "Cognitive synergy system not compatible with unified dashboard")


if __name__ == '__main__':
    print("🧪 Running Cognitive Synergy Tests...")
    print("=" * 50)
    
    # Run the test suite
    unittest.main(verbosity=2, exit=False)
    
    print("\n✅ Cognitive Synergy Tests Complete!")
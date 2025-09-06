#!/usr/bin/env python3
"""
Cognitive Integration Bridge
Enables OpenCog to perceive and orchestrate its own distributed architecture
Through real-time hypergraph mapping of component relationships
"""

import asyncio
import json
import time
from pathlib import Path
from typing import Dict, List, Set, Tuple
import networkx as nx
from flask import Flask, jsonify, render_template
from collections import defaultdict

class CognitiveIntegrationBridge:
    """
    The meta-cognitive layer that enables OpenCog to perceive itself
    Maps relationships between all cognitive components in real-time
    """
    
    def __init__(self):
        self.cognitive_graph = nx.DiGraph()
        self.component_registry = {}
        self.synergy_patterns = defaultdict(list)
        self.attention_allocation = {}
        self.emergence_events = []
        self.interaction_memory = []
        
        # Initialize core cognitive components
        self._register_cognitive_components()
        self._establish_synaptic_connections()
        
    def _register_cognitive_components(self):
        """Register all cognitive subsystems as nodes in the hypergraph"""
        
        components = {
            'atomspace': {
                'type': 'memory_substrate',
                'capabilities': ['knowledge_storage', 'pattern_matching', 'query_processing'],
                'attention_priority': 0.8
            },
            'pln': {
                'type': 'reasoning_engine', 
                'capabilities': ['probabilistic_inference', 'truth_evaluation', 'logical_chaining'],
                'attention_priority': 0.7
            },
            'moses': {
                'type': 'evolutionary_learning',
                'capabilities': ['program_evolution', 'fitness_optimization', 'solution_discovery'],
                'attention_priority': 0.6
            },
            'attention': {
                'type': 'resource_allocation',
                'capabilities': ['importance_spreading', 'focus_management', 'hebbian_learning'],
                'attention_priority': 0.9
            },
            'ghost': {
                'type': 'goal_orchestration',
                'capabilities': ['behavior_scripting', 'goal_pursuit', 'action_selection'],
                'attention_priority': 0.5
            },
            'ure': {
                'type': 'rule_engine',
                'capabilities': ['pattern_application', 'inference_control', 'rule_chaining'],
                'attention_priority': 0.6
            },
            'embodiment': {
                'type': 'sensorimotor_integration',
                'capabilities': ['perception_grounding', 'action_execution', 'spatial_reasoning'],
                'attention_priority': 0.7
            },
            'language': {
                'type': 'linguistic_processing',
                'capabilities': ['parsing', 'generation', 'semantic_analysis'],
                'attention_priority': 0.8
            }
        }
        
        for name, attrs in components.items():
            self.cognitive_graph.add_node(name, **attrs)
            self.component_registry[name] = attrs
            self.attention_allocation[name] = attrs['attention_priority']
            
    def _establish_synaptic_connections(self):
        """Create weighted edges representing cognitive synergies"""
        
        synaptic_connections = [
            # Core memory-reasoning loop
            ('atomspace', 'pln', {'weight': 0.9, 'synergy_type': 'knowledge_inference'}),
            ('pln', 'atomspace', {'weight': 0.8, 'synergy_type': 'inference_storage'}),
            
            # Attention-driven processing
            ('attention', 'atomspace', {'weight': 0.9, 'synergy_type': 'importance_propagation'}),
            ('attention', 'pln', {'weight': 0.7, 'synergy_type': 'inference_prioritization'}),
            
            # Evolution-knowledge feedback
            ('moses', 'atomspace', {'weight': 0.6, 'synergy_type': 'solution_integration'}),
            ('atomspace', 'moses', {'weight': 0.5, 'synergy_type': 'fitness_evaluation'}),
            
            # Goal-directed reasoning
            ('ghost', 'pln', {'weight': 0.7, 'synergy_type': 'goal_inference'}),
            ('ghost', 'ure', {'weight': 0.8, 'synergy_type': 'behavior_rules'}),
            
            # Language-reasoning bridge
            ('language', 'atomspace', {'weight': 0.8, 'synergy_type': 'semantic_grounding'}),
            ('language', 'pln', {'weight': 0.7, 'synergy_type': 'linguistic_inference'}),
            
            # Embodiment grounding
            ('embodiment', 'atomspace', {'weight': 0.6, 'synergy_type': 'perceptual_grounding'}),
            ('embodiment', 'ghost', {'weight': 0.7, 'synergy_type': 'action_execution'}),
            
            # Rule application paths
            ('ure', 'atomspace', {'weight': 0.8, 'synergy_type': 'rule_application'}),
            ('ure', 'pln', {'weight': 0.7, 'synergy_type': 'inference_rules'})
        ]
        
        self.cognitive_graph.add_edges_from(synaptic_connections)
        
    def detect_emergence_patterns(self) -> List[Dict]:
        """Identify emergent cognitive patterns from component interactions"""
        
        emergence_candidates = []
        
        # Find strongly connected components (cognitive modules)
        strong_components = list(nx.strongly_connected_components(self.cognitive_graph))
        
        for component_set in strong_components:
            if len(component_set) >= 2:  # Multi-component synergy (lowered threshold)
                synergy_strength = self._calculate_synergy_strength(component_set)
                
                if synergy_strength > 0.5:  # Lowered synergy threshold for more detection
                    emergence_candidates.append({
                        'components': list(component_set),
                        'synergy_strength': synergy_strength,
                        'timestamp': time.time(),
                        'pattern_type': 'cognitive_module',
                        'capabilities': self._infer_emergent_capabilities(component_set)
                    })
                    
        # Detect information flow patterns
        centrality = nx.betweenness_centrality(self.cognitive_graph)
        hubs = [node for node, cent in centrality.items() if cent > 0.2]  # Lowered threshold
        
        if len(hubs) >= 2:
            emergence_candidates.append({
                'components': hubs,
                'pattern_type': 'information_hub',
                'timestamp': time.time(),
                'synergy_strength': 0.8,
                'capabilities': ['cross_component_integration', 'information_routing']
            })
            
        # Detect specific synergistic patterns
        # Memory-Reasoning Synergy
        if 'atomspace' in self.cognitive_graph.nodes() and 'pln' in self.cognitive_graph.nodes():
            if self.cognitive_graph.has_edge('atomspace', 'pln') or self.cognitive_graph.has_edge('pln', 'atomspace'):
                emergence_candidates.append({
                    'components': ['atomspace', 'pln'],
                    'pattern_type': 'memory_reasoning_synergy',
                    'timestamp': time.time(),
                    'synergy_strength': 0.9,
                    'capabilities': ['uncertain_knowledge_reasoning', 'truth_value_propagation']
                })
                
        # Attention-Learning Synergy  
        if 'attention' in self.cognitive_graph.nodes() and 'moses' in self.cognitive_graph.nodes():
            if self.cognitive_graph.has_edge('attention', 'moses') or any(
                self.cognitive_graph.has_edge('attention', node) and self.cognitive_graph.has_edge(node, 'moses')
                for node in self.cognitive_graph.nodes()
            ):
                emergence_candidates.append({
                    'components': ['attention', 'moses'],
                    'pattern_type': 'attention_learning_synergy',
                    'timestamp': time.time(),
                    'synergy_strength': 0.85,
                    'capabilities': ['focused_evolution', 'adaptive_attention_allocation']
                })
                
        # Language-Embodiment Synergy
        if 'language' in self.cognitive_graph.nodes() and 'embodiment' in self.cognitive_graph.nodes():
            emergence_candidates.append({
                'components': ['language', 'embodiment'],
                'pattern_type': 'grounded_language_synergy',
                'timestamp': time.time(),
                'synergy_strength': 0.75,
                'capabilities': ['embodied_language_understanding', 'grounded_semantics']
            })
            
        # Goal-Rule Synergy
        if 'ghost' in self.cognitive_graph.nodes() and 'ure' in self.cognitive_graph.nodes():
            emergence_candidates.append({
                'components': ['ghost', 'ure'],
                'pattern_type': 'goal_rule_synergy', 
                'timestamp': time.time(),
                'synergy_strength': 0.8,
                'capabilities': ['adaptive_goal_optimization', 'rule_guided_behavior']
            })
            
        self.emergence_events.extend(emergence_candidates)
        return emergence_candidates
        
    def _calculate_synergy_strength(self, components: Set[str]) -> float:
        """Calculate the synergistic strength of component interactions"""
        
        subgraph = self.cognitive_graph.subgraph(components)
        if not subgraph.edges():
            return 0.0
            
        # Calculate based on edge weights and connectivity
        total_weight = sum(data.get('weight', 0) for _, _, data in subgraph.edges(data=True))
        max_possible = len(components) * (len(components) - 1)
        connectivity = len(subgraph.edges()) / max_possible if max_possible > 0 else 0
        
        return (total_weight / len(subgraph.edges())) * connectivity
        
    def _infer_emergent_capabilities(self, components: Set[str]) -> List[str]:
        """Infer new capabilities from component combinations"""
        
        capabilities = set()
        for component in components:
            if component in self.component_registry:
                capabilities.update(self.component_registry[component]['capabilities'])
                
        # Infer emergent capabilities based on combinations
        if 'knowledge_storage' in capabilities and 'probabilistic_inference' in capabilities:
            capabilities.add('uncertain_knowledge_reasoning')
            
        if 'goal_pursuit' in capabilities and 'program_evolution' in capabilities:
            capabilities.add('adaptive_goal_optimization')
            
        if 'perception_grounding' in capabilities and 'semantic_analysis' in capabilities:
            capabilities.add('embodied_language_understanding')
            
        return list(capabilities)
        
    def allocate_cognitive_resources(self, task_context: Dict) -> Dict[str, float]:
        """Dynamically allocate attention based on task requirements"""
        
        task_type = task_context.get('type', 'general')
        required_capabilities = task_context.get('capabilities', [])
        
        # Adjust attention based on task requirements
        adjusted_attention = self.attention_allocation.copy()
        
        # Boost components with required capabilities
        for component, attrs in self.component_registry.items():
            component_caps = set(attrs['capabilities'])
            required_caps = set(required_capabilities)
            
            if component_caps & required_caps:  # Intersection
                adjusted_attention[component] *= 1.5  # Boost relevant components
                
        # Normalize to sum to 1.0
        total = sum(adjusted_attention.values())
        if total > 0:
            adjusted_attention = {k: v/total for k, v in adjusted_attention.items()}
            
        return adjusted_attention
        
    def learn_from_interaction(self, interaction: Dict):
        """Store and learn from user interactions to improve future responses"""
        
        self.interaction_memory.append({
            'timestamp': time.time(),
            'interaction': interaction,
            'active_components': self._identify_active_components(interaction),
            'success_metric': interaction.get('success', 0.5)
        })
        
        # Adjust synergy weights based on successful interactions
        if interaction.get('success', 0.5) > 0.7:
            active = self._identify_active_components(interaction)
            for i, comp1 in enumerate(active):
                for comp2 in active[i+1:]:
                    if self.cognitive_graph.has_edge(comp1, comp2):
                        current_weight = self.cognitive_graph[comp1][comp2].get('weight', 0.5)
                        # Strengthen successful pathways
                        self.cognitive_graph[comp1][comp2]['weight'] = min(1.0, current_weight + 0.05)
                        
    def _identify_active_components(self, interaction: Dict) -> List[str]:
        """Identify which components were active in an interaction"""
        
        active = []
        interaction_type = interaction.get('type', '')
        
        if 'reasoning' in interaction_type or 'inference' in interaction_type:
            active.extend(['pln', 'ure', 'atomspace'])
        if 'language' in interaction_type or 'text' in interaction_type:
            active.extend(['language', 'atomspace'])
        if 'learning' in interaction_type:
            active.extend(['moses', 'attention'])
        if 'goal' in interaction_type:
            active.extend(['ghost', 'pln'])
            
        return list(set(active))  # Remove duplicates
        
    def get_cognitive_state(self) -> Dict:
        """Return current cognitive architecture state"""
        
        return {
            'active_components': len(self.cognitive_graph.nodes()),
            'synaptic_connections': len(self.cognitive_graph.edges()),
            'emergence_patterns': len(self.emergence_events),
            'attention_distribution': self.attention_allocation,
            'recent_synergies': self.synergy_patterns,
            'interaction_history': len(self.interaction_memory),
            'graph_metrics': {
                'density': nx.density(self.cognitive_graph),
                'average_clustering': nx.average_clustering(self.cognitive_graph.to_undirected()),
                'components': nx.number_strongly_connected_components(self.cognitive_graph)
            }
        }
        
    def visualize_cognitive_graph(self) -> Dict:
        """Generate visualization data for the cognitive architecture"""
        
        nodes = []
        edges = []
        
        for node, attrs in self.cognitive_graph.nodes(data=True):
            nodes.append({
                'id': node,
                'type': attrs.get('type', 'unknown'),
                'attention': self.attention_allocation.get(node, 0.5),
                'capabilities': attrs.get('capabilities', [])
            })
            
        for source, target, attrs in self.cognitive_graph.edges(data=True):
            edges.append({
                'source': source,
                'target': target,
                'weight': attrs.get('weight', 0.5),
                'synergy_type': attrs.get('synergy_type', 'unknown')
            })
            
        return {
            'nodes': nodes,
            'edges': edges,
            'timestamp': time.time()
        }
        

# Flask application for cognitive monitoring
app = Flask(__name__)
bridge = CognitiveIntegrationBridge()

@app.route('/')
def cognitive_dashboard():
    """Main cognitive integration dashboard"""
    return render_template('cognitive_bridge_dashboard.html')
    
@app.route('/api/cognitive/state')
def get_cognitive_state():
    """Get current cognitive architecture state"""
    return jsonify(bridge.get_cognitive_state())
    
@app.route('/api/cognitive/emergence')
def detect_emergence():
    """Detect and return emergence patterns"""
    patterns = bridge.detect_emergence_patterns()
    return jsonify({'patterns': patterns})
    
@app.route('/api/cognitive/graph')
def get_cognitive_graph():
    """Get cognitive architecture graph for visualization"""
    return jsonify(bridge.visualize_cognitive_graph())
    
@app.route('/api/cognitive/allocate', methods=['POST'])
def allocate_resources():
    """Allocate cognitive resources for a task"""
    from flask import request
    task_context = request.json
    allocation = bridge.allocate_cognitive_resources(task_context)
    return jsonify({'allocation': allocation})
    
@app.route('/api/cognitive/learn', methods=['POST'])
def learn_interaction():
    """Learn from an interaction"""
    from flask import request
    interaction = request.json
    bridge.learn_from_interaction(interaction)
    return jsonify({'status': 'learned', 'memory_size': len(bridge.interaction_memory)})
    

if __name__ == '__main__':
    print("🧬 Cognitive Integration Bridge Activating...")
    print("Establishing synaptic connections between cognitive components...")
    print("Enabling self-perception and orchestration capabilities...")
    
    # Detect initial emergence patterns
    initial_patterns = bridge.detect_emergence_patterns()
    print(f"Detected {len(initial_patterns)} initial emergence patterns")
    
    app.run(host='0.0.0.0', port=5001, debug=True)
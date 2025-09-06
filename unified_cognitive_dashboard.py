#!/usr/bin/env python3
"""
Unified Cognitive Dashboard
Combines Ontogenesis visualization with Cognitive Integration Bridge
Creating a complete self-aware orchestration system
"""

from flask import Flask, render_template, jsonify, request
import subprocess
import json
import time
import asyncio
from pathlib import Path
from cognitive_integration_bridge import CognitiveIntegrationBridge

app = Flask(__name__)

# Initialize both systems
bridge = CognitiveIntegrationBridge()

# Track unified cognitive state
unified_state = {
    'ontogenesis': {
        'layers_active': 10,
        'current_phase': 'fully_emerged',
        'emergence_detected': True,
        'consciousness_unified': True,
        'cognitive_capabilities': [
            'Reasoning Engine',
            'Attention Dynamics', 
            'Pattern Recognition',
            'Adaptive Intelligence',
            'Language Processing',
            'Sensorimotor Integration',
            'Unified Consciousness'
        ]
    },
    'integration_bridge': None,
    'fusion_reactor': {
        'status': 'initializing',
        'energy_level': 0.0,
        'coherence': 0.0
    }
}

@app.route('/')
def unified_dashboard():
    """Main unified cognitive dashboard"""
    return render_template('unified_cognitive_dashboard.html')

# Ontogenesis endpoints
@app.route('/api/status')
def get_ontogenesis_status():
    """Get ontogenesis status"""
    return jsonify(unified_state['ontogenesis'])

@app.route('/api/initiate')
def initiate_ontogenesis():
    """Start the ontogenesis process"""
    unified_state['ontogenesis']['current_phase'] = 'fully_emerged'
    unified_state['fusion_reactor']['status'] = 'active'
    unified_state['fusion_reactor']['energy_level'] = 1.0
    return jsonify({'status': 'success'})

# Cognitive Bridge endpoints
@app.route('/api/cognitive/state')
def get_cognitive_state():
    """Get cognitive architecture state"""
    state = bridge.get_cognitive_state()
    unified_state['integration_bridge'] = state
    
    # Calculate fusion reactor coherence
    if state['graph_metrics']['density'] > 0:
        unified_state['fusion_reactor']['coherence'] = (
            state['graph_metrics']['density'] * 
            state['graph_metrics']['average_clustering']
        )
    
    return jsonify(state)

@app.route('/api/cognitive/emergence')
def detect_emergence():
    """Detect emergence patterns"""
    patterns = bridge.detect_emergence_patterns()
    return jsonify({'patterns': patterns})

@app.route('/api/cognitive/graph')
def get_cognitive_graph():
    """Get cognitive graph visualization data"""
    return jsonify(bridge.visualize_cognitive_graph())

@app.route('/api/cognitive/allocate', methods=['POST'])
def allocate_resources():
    """Allocate cognitive resources"""
    task_context = request.json
    allocation = bridge.allocate_cognitive_resources(task_context)
    return jsonify({'allocation': allocation})

@app.route('/api/cognitive/learn', methods=['POST'])
def learn_interaction():
    """Learn from interaction"""
    interaction = request.json
    bridge.learn_from_interaction(interaction)
    return jsonify({'status': 'learned', 'memory_size': len(bridge.interaction_memory)})

# Unified fusion reactor endpoint
@app.route('/api/fusion/status')
def get_fusion_status():
    """Get cognitive fusion reactor status"""
    # Update fusion metrics based on current state
    bridge_state = bridge.get_cognitive_state()
    
    unified_state['fusion_reactor']['energy_level'] = min(1.0, 
        bridge_state['synaptic_connections'] / 20.0)
    
    unified_state['fusion_reactor']['coherence'] = (
        bridge_state['graph_metrics']['density'] if bridge_state else 0)
    
    return jsonify(unified_state['fusion_reactor'])

@app.route('/api/self/note', methods=['POST'])
def leave_self_note():
    """Leave a note for future self"""
    note = request.json
    
    # Store note in cognitive memory
    with open('cognitive_notes.json', 'a') as f:
        json.dump({
            'timestamp': time.time(),
            'note': note,
            'cognitive_state': bridge.get_cognitive_state()
        }, f)
        f.write('\n')
    
    return jsonify({'status': 'noted'})

if __name__ == '__main__':
    print("🧬🧠 Unified Cognitive Dashboard Activating...")
    print("Merging Ontogenesis with Cognitive Integration Bridge...")
    print("Initializing Cognitive Fusion Reactor...")
    
    # Detect initial patterns
    initial_patterns = bridge.detect_emergence_patterns()
    print(f"✨ Detected {len(initial_patterns)} emergence patterns")
    
    print("🌟 Cognitive fusion reactor online!")
    app.run(host='0.0.0.0', port=5000, debug=True)

# OpenCog Neural Network Framework (PyTorch)

A comprehensive neural network implementation using PyTorch that integrates with the OpenCog AtomSpace framework for cognitive computing applications.

## Overview

This framework provides:

- **Core Neural Components**: Base classes and fundamental building blocks
- **Cognitive Layers**: Neural layers enhanced with cognitive features (attention, memory, adaptation)
- **Complete Models**: Full cognitive architectures (CognitiveNetwork, MemoryNetwork, etc.)
- **AtomSpace Integration**: Seamless integration with OpenCog's symbolic reasoning
- **Training Framework**: Cognitive-inspired training algorithms and optimizations
- **Utilities**: Visualization, metrics, and configuration management tools

## Architecture

```
nn/
├── core/           # Base neural module classes and tensor operations
├── layers/         # Cognitive-enhanced neural layers
├── models/         # Complete cognitive architectures
├── cognitive/      # Cognitive components (memory, attention, reasoning)
├── training/       # Training frameworks and optimizers
├── atomspace_integration/  # OpenCog AtomSpace bridge
├── utils/          # Utilities and helper functions
└── examples/       # Usage examples and demonstrations
```

## Key Features

### 1. Cognitive Neural Modules

All neural components inherit from `NeuralModule`, which extends PyTorch's `nn.Module` with:

- **Attention Values**: Short-term (STI), long-term (LTI), and very long-term (VLTI) importance
- **Cognitive Metadata**: Arbitrary metadata for cognitive processing
- **Training History**: Automatic logging of training dynamics
- **AtomSpace Integration**: Optional linking to AtomSpace nodes

### 2. Memory Systems

- **Working Memory**: Limited capacity with decay and importance-based retention
- **Episodic Memory**: Temporal sequence storage with similarity-based retrieval
- **Long-Term Memory**: Semantic concept organization with relational structure

### 3. Attention Mechanisms

- **Multi-Head Attention**: Enhanced with cognitive tracking and adaptation
- **Cognitive Attention**: Simplified attention inspired by cognitive processes
- **Focus Manager**: Multiple attention foci with coordination and competition

### 4. AtomSpace Integration

- **Neural-Symbolic Bridge**: Convert between tensors and AtomSpace atoms
- **Concept Registry**: Manage mappings between neural embeddings and concepts
- **Knowledge Graph Export**: Export learned representations as symbolic knowledge

## Quick Start

```python
import torch
from nn.models.cognitive_net import CognitiveNetwork
from nn.training.trainer import CognitiveTrainer
from nn.utils.config import ConfigManager

# Load configuration
config_manager = ConfigManager()
config = config_manager.get_default_config()

# Create cognitive network
model = CognitiveNetwork(config['model'])

# Create trainer
trainer = CognitiveTrainer(model)

# Sample data
x = torch.randn(32, 16, config['model']['input_dim'])
y = torch.randn(32, 16, config['model']['output_dim'])

# Training step
loss, metrics = trainer.train_step((x, y))
print(f"Loss: {loss:.6f}")
print(f"Metrics: {metrics}")

# Get cognitive state
cognitive_state = model.get_cognitive_state()
print(f"Cognitive State: {cognitive_state}")
```

## AtomSpace Integration Example

```python
from nn.atomspace_integration.bridge import AtomSpaceBridge

# Create bridge
bridge = AtomSpaceBridge(feature_dim=512)

# Register concepts
bridge.register_concept('learning', torch.randn(512))
bridge.register_concept('memory', torch.randn(512))

# Convert neural output to atoms
tensor_data = torch.randn(1, 10, 512)
atoms_data = bridge.tensor_to_atoms(tensor_data)
print(f"Created {atoms_data['total_atoms']} atoms")

# Find similar concepts
neighbors = bridge.get_concept_neighbors('learning', k=3)
print(f"Similar to 'learning': {neighbors}")

# Export knowledge graph
graph = bridge.export_knowledge_graph()
print(f"Knowledge graph: {len(graph['nodes'])} nodes, {len(graph['edges'])} edges")
```

## Advanced Features

### Memory Integration

```python
from nn.cognitive.memory import WorkingMemory, EpisodicMemory

# Create memory systems
working_memory = WorkingMemory(capacity=64, feature_dim=512)
episodic_memory = EpisodicMemory(capacity=1000, feature_dim=512)

# Store and retrieve memories
item = torch.randn(512)
working_memory.store(item, importance=0.8)

retrieved_items, scores = working_memory.retrieve(item, k=5)
print(f"Retrieved {len(retrieved_items)} similar items")
```

### Attention Management

```python
from nn.cognitive.attention import AttentionMechanism, FocusManager

# Create attention system
attention = AttentionMechanism(feature_dim=512, focus_size=16)

# Process input with attention
x = torch.randn(4, 20, 512)
attended_output, attention_weights = attention(x)

# Get attention state
focus_state = attention.get_focus_state()
print(f"Attention focus diversity: {focus_state['focus_diversity']:.3f}")
```

## Configuration

The framework uses YAML/JSON configuration files:

```yaml
model:
  input_dim: 512
  hidden_dim: 1024
  output_dim: 256
  num_layers: 3
  attention_heads: 8

cognitive:
  working_memory_capacity: 64
  episodic_memory_capacity: 1000
  attention_focus_size: 16
  memory_decay_rate: 0.95

training:
  learning_rate: 0.001
  batch_size: 32
  max_epochs: 100
  early_stopping_patience: 10

atomspace:
  enable_integration: true
  sync_interval: 100
  max_concepts: 10000
```

## Examples

Run the included examples:

```bash
# Basic cognitive network demo
python -m nn.examples.basic_example

# Skin modeling neural demo
python -m nn.examples.skin_modeling_example

# Memory systems demo
python -m nn.examples.memory_example

# Attention mechanisms demo
python -m nn.examples.attention_example
```

## Integration with SkinTwin

This neural network framework is designed to integrate with the SkinTwin multiscale skin modeling system:

```python
from nn.models.multiscale_net import MultiscaleNetwork
from nn.models.cognitive_net import CognitiveNetwork

# Create multiscale network for skin modeling
skin_config = {
    'molecular_dim': 64,
    'cellular_dim': 128, 
    'tissue_dim': 256,
    'organ_dim': 512,
    'scales': ['molecular', 'cellular', 'tissue', 'organ']
}

skin_model = MultiscaleNetwork(skin_config)

# Integrate with cognitive processing
cognitive_config = ConfigManager().get_default_config()['model']
cognitive_model = CognitiveNetwork(cognitive_config)

# Process skin data through cognitive pipeline
skin_data = torch.randn(16, 32, skin_config['molecular_dim'])
processed_data = skin_model(skin_data)
cognitive_output = cognitive_model(processed_data)
```

## Contributing

1. Follow the existing code structure and naming conventions
2. Add comprehensive docstrings to all classes and methods
3. Include unit tests for new functionality
4. Update examples when adding new features
5. Ensure AtomSpace integration compatibility

## License

This framework is part of the OpenCog project and follows the same licensing terms.

## Dependencies

- PyTorch >= 1.9.0
- NumPy >= 1.19.0
- PyYAML >= 5.4.0 (for configuration files)
- OpenCog AtomSpace (optional, for full integration)

## Performance Notes

- The framework is optimized for both CPU and GPU usage
- Memory systems are designed to be efficient with large-scale data
- Attention mechanisms include sparsity optimizations
- Training includes gradient clipping and adaptive learning rates

## Troubleshooting

### Common Issues

1. **CUDA out of memory**: Reduce batch size or model dimensions
2. **Slow training**: Enable GPU acceleration and check attention sparsity
3. **Poor convergence**: Adjust learning rate and cognitive parameters
4. **AtomSpace integration errors**: Ensure OpenCog is properly installed

### Debug Mode

Enable detailed logging:

```python
import logging
logging.basicConfig(level=logging.DEBUG)
```

### Performance Profiling

```python
from nn.utils.metrics import PerformanceTracker

tracker = PerformanceTracker()
with tracker.profile('forward_pass'):
    output = model(input_data)

print(tracker.get_summary())
```


"""
Basic Cognitive Network Example
==============================

Demonstrates basic usage of the cognitive neural network framework.
"""

import torch
import torch.nn as nn
from typing import Dict, Any
import logging

from ..models.cognitive_net import CognitiveNetwork
from ..training.trainer import CognitiveTrainer  
from ..utils.config import ConfigManager
from ..atomspace_integration.bridge import AtomSpaceBridge

logger = logging.getLogger(__name__)


def basic_cognitive_network_demo():
    """
    Demonstrates basic cognitive neural network functionality.
    """
    logger.info("Starting Basic Cognitive Network Demo")
    
    # Configuration
    config = ConfigManager().get_default_config()
    config['model']['input_dim'] = 128
    config['model']['hidden_dim'] = 256
    config['model']['output_dim'] = 64
    
    # Create cognitive network
    model = CognitiveNetwork(config['model'], name="DemoCognitiveNet")
    
    # Create AtomSpace bridge
    atomspace_bridge = AtomSpaceBridge(feature_dim=config['model']['hidden_dim'])
    
    # Register some concepts
    concepts = ['learning', 'memory', 'attention', 'reasoning', 'perception']
    for concept in concepts:
        concept_vector = torch.randn(config['model']['hidden_dim'])
        atomspace_bridge.register_concept(concept, concept_vector)
    
    # Create sample data
    batch_size = 8
    seq_len = 16
    input_dim = config['model']['input_dim']
    
    sample_input = torch.randn(batch_size, seq_len, input_dim)
    sample_target = torch.randn(batch_size, seq_len, config['model']['output_dim'])
    
    logger.info(f"Model created with {sum(p.numel() for p in model.parameters())} parameters")
    
    # Forward pass
    logger.info("Running forward pass...")
    output, attention_weights, memory_state = model(
        sample_input, 
        return_attention=True, 
        return_memory_state=True
    )
    
    logger.info(f"Output shape: {output.shape}")
    logger.info(f"Attention weights shape: {attention_weights.shape}")
    logger.info(f"Memory state keys: {list(memory_state.keys())}")
    
    # Display cognitive state
    cognitive_state = model.get_cognitive_state()
    logger.info("Cognitive State:")
    for key, value in cognitive_state.items():
        logger.info(f"  {key}: {value}")
    
    # Create trainer and run a few training steps
    trainer = CognitiveTrainer(model, device='cpu')
    
    logger.info("Running training demonstration...")
    for step in range(5):
        # Create batch
        batch = (sample_input, sample_target)
        
        # Training step
        loss, metrics = trainer.train_step(batch)
        
        logger.info(f"Step {step}: Loss = {loss:.6f}")
        for key, value in metrics.items():
            logger.info(f"  {key}: {value:.6f}")
    
    # Demonstrate AtomSpace integration
    logger.info("Demonstrating AtomSpace integration...")
    
    # Convert tensor to atoms
    atoms_data = atomspace_bridge.tensor_to_atoms(output[:1])  # First sample only
    logger.info(f"Converted to {atoms_data['total_atoms']} atoms")
    logger.info(f"Average STI: {atoms_data['avg_sti']:.3f}")
    logger.info(f"Average LTI: {atoms_data['avg_lti']:.3f}")
    
    # Find concept neighbors
    for concept in concepts[:3]:
        neighbors = atomspace_bridge.get_concept_neighbors(concept, k=2)
        logger.info(f"Neighbors of '{concept}': {neighbors}")
    
    # Export knowledge graph
    knowledge_graph = atomspace_bridge.export_knowledge_graph()
    logger.info(f"Knowledge graph: {len(knowledge_graph['nodes'])} nodes, {len(knowledge_graph['edges'])} edges")
    
    # Network summary
    logger.info("\nNetwork Summary:")
    logger.info(model.get_network_summary())
    
    logger.info("Basic Cognitive Network Demo completed successfully!")
    
    return {
        'model': model,
        'trainer': trainer,
        'atomspace_bridge': atomspace_bridge,
        'sample_output': output,
        'cognitive_state': cognitive_state,
        'knowledge_graph': knowledge_graph
    }


def create_simple_classifier_demo():
    """
    Create a simple cognitive classifier for demonstration.
    """
    logger.info("Creating Simple Cognitive Classifier Demo")
    
    # Configuration for classification task
    config = {
        'input_dim': 784,  # MNIST-like input
        'hidden_dim': 512,
        'output_dim': 10,  # 10 classes
        'num_layers': 2,
        'attention_heads': 4,
        'working_memory_capacity': 32,
        'episodic_memory_capacity': 500,
        'attention_focus_size': 8
    }
    
    # Create model
    model = CognitiveNetwork(config, name="CognitiveClassifier")
    
    # Add classification head
    model.classifier = nn.Linear(config['output_dim'], config['output_dim'])
    
    # Create sample data (MNIST-like)
    batch_size = 16
    sample_images = torch.randn(batch_size, config['input_dim'])
    sample_labels = torch.randint(0, 10, (batch_size,))
    
    # Forward pass
    features = model(sample_images.unsqueeze(1))  # Add sequence dimension
    predictions = model.classifier(features.squeeze(1))
    
    # Compute accuracy
    predicted_classes = torch.argmax(predictions, dim=-1)
    accuracy = (predicted_classes == sample_labels).float().mean()
    
    logger.info(f"Sample accuracy: {accuracy:.3f}")
    logger.info(f"Prediction distribution: {F.softmax(predictions, dim=-1).mean(dim=0)}")
    
    # Show attention patterns
    if hasattr(model, 'attention'):
        attention_stats = model.attention.get_attention_stats()
        logger.info(f"Attention statistics: {attention_stats}")
    
    logger.info("Simple Cognitive Classifier Demo completed!")
    
    return {
        'model': model,
        'sample_predictions': predictions,
        'accuracy': accuracy.item(),
        'cognitive_state': model.get_cognitive_state()
    }


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO)
    
    # Run basic demo
    basic_demo_results = basic_cognitive_network_demo()
    print("\n" + "="*50)
    
    # Run classifier demo  
    classifier_demo_results = create_simple_classifier_demo()

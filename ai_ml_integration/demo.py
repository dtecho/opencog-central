
"""
OpenCog AI/ML Integration Demo
Demonstrates integration between neural networks, symbolic reasoning, and LLMs
"""

import torch
import logging
from pathlib import Path
import time

from .core import OpenCogAIMLIntegration, get_integration_manager
from .moses_integration import create_moses_integration
from .llm_integration import create_llm_integration, CognitivePromptEnhancer

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

def demo_basic_integration():
    """Demonstrate basic AI/ML integration features"""
    print("=== OpenCog AI/ML Integration Demo ===\n")
    
    # Create integration
    integration = OpenCogAIMLIntegration()
    
    print("1. Processing text input...")
    text_result = integration.process_input("Humans are intelligent beings who can learn and reason")
    print(f"   Neural output shape: {text_result['neural_output'].shape if text_result['neural_output'] is not None else 'None'}")
    print(f"   Symbolic concepts: {len(text_result.get('symbolic_output', {}).get('concepts', []))}")
    
    print("\n2. Processing numerical data...")
    numerical_data = torch.randn(1, 10, 512)
    numerical_result = integration.process_input(numerical_data)
    print(f"   Attention weights shape: {numerical_result['attention_weights'].shape if numerical_result['attention_weights'] is not None else 'None'}")
    
    print("\n3. Reasoning with PLN...")
    reasoning_result = integration.reason_with_pln("If all humans are mortal, and Socrates is human, then Socrates is mortal")
    print(f"   Reasoning confidence: {reasoning_result.get('confidence', 'N/A')}")
    
    print("\n4. Learning from feedback...")
    integration.learn_from_interaction("Learning is important for intelligence", feedback=0.9)
    integration.learn_from_interaction("Confusion leads to understanding", feedback=0.7)
    
    print("\n5. Cognitive state summary...")
    state = integration.get_cognitive_state()
    print(f"   AtomSpace size: {state['atomspace_size']}")
    print(f"   Working memory: {state['memory_state']['working_memory_size']} items")
    print(f"   Integration success rate: {state['integration_metrics'].get('successful_processes', 0) / state['integration_metrics'].get('total_processes', 1):.2%}")

def demo_moses_integration():
    """Demonstrate MOSES evolutionary learning integration"""
    print("\n=== MOSES Integration Demo ===\n")
    
    try:
        moses = create_moses_integration()
        
        print("1. Creating training data...")
        # Simple XOR-like problem
        training_inputs = torch.tensor([
            [0, 0], [0, 1], [1, 0], [1, 1],
            [0, 0], [0, 1], [1, 0], [1, 1]
        ], dtype=torch.float32).unsqueeze(1)
        
        training_targets = torch.tensor([
            [0], [1], [1], [0],
            [0], [1], [1], [0]
        ], dtype=torch.float32)
        
        print("2. Evolving program with MOSES...")
        evolution_result = moses.evolve_neural_program(
            training_inputs, 
            training_targets,
            generations=10,  # Small for demo
            population_size=50
        )
        
        if 'error' not in evolution_result:
            print(f"   Evolved program: {evolution_result['program']['program']}")
            print(f"   Fitness: {evolution_result['program']['fitness']:.4f}")
            
            print("3. Getting best programs...")
            best_programs = moses.get_best_programs(top_k=3)
            for i, prog in enumerate(best_programs):
                print(f"   #{i+1}: Fitness {prog['fitness']:.4f}")
        else:
            print(f"   MOSES evolution failed: {evolution_result['error']}")
            print("   (This is expected if MOSES is not properly installed)")
    
    except Exception as e:
        print(f"MOSES demo failed: {e}")
        print("This is expected if MOSES is not built or available")

def demo_llm_integration():
    """Demonstrate LLM integration with cognitive processing"""
    print("\n=== LLM Integration Demo ===\n")
    
    # Create integrations
    ai_integration = OpenCogAIMLIntegration()
    llm_integration = create_llm_integration()
    enhancer = CognitivePromptEnhancer(ai_integration)
    
    print("1. Available LLM services:")
    for service, info in llm_integration.llm_services.items():
        print(f"   {service}: {'Available' if info['available'] else 'Not available'}")
    
    print("\n2. Enhancing prompts with cognitive context...")
    base_prompt = "Explain the relationship between learning and intelligence"
    
    enhanced_reasoning = enhancer.enhance_prompt(base_prompt, 'reasoning')
    print(f"   Enhanced prompt length: {len(enhanced_reasoning)} characters")
    
    enhanced_memory = enhancer.enhance_prompt(base_prompt, 'memory')
    print(f"   Memory-enhanced prompt length: {len(enhanced_memory)} characters")
    
    print("\n3. Simulated cognitive chat...")
    # Since we may not have actual LLM models, simulate the response
    simulated_response = "Intelligence emerges from the ability to learn patterns, adapt to new situations, and apply knowledge flexibly across different domains."
    
    # Process through cognitive system
    response_analysis = ai_integration.process_input(simulated_response)
    print(f"   Response processed through cognitive system")
    print(f"   Symbolic concepts extracted: {len(response_analysis.get('symbolic_output', {}).get('concepts', []))}")

def demo_multimodal_integration():
    """Demonstrate multimodal AI/ML integration"""
    print("\n=== Multimodal Integration Demo ===\n")
    
    integration = OpenCogAIMLIntegration()
    
    print("1. Processing different data modalities...")
    
    # Text modality
    text_data = "The sky is blue and birds can fly"
    text_result = integration.process_input(text_data)
    
    # Numerical modality
    sensor_data = {
        'temperature': 23.5,
        'humidity': 65.0,
        'light_level': 800,
        'sound_level': 45.2
    }
    sensor_result = integration.process_input(sensor_data)
    
    # Image-like modality (simulated)
    image_data = torch.randn(1, 3, 64, 64)  # Simulated image tensor
    image_result = integration.process_input(image_data)
    
    print(f"   Text processing: {'Success' if text_result.get('neural_output') is not None else 'Failed'}")
    print(f"   Sensor processing: {'Success' if sensor_result.get('neural_output') is not None else 'Failed'}")
    print(f"   Image processing: {'Success' if image_result.get('neural_output') is not None else 'Failed'}")
    
    print("\n2. Cross-modal reasoning...")
    # Combine insights from different modalities
    combined_context = f"Text concepts: {len(text_result.get('symbolic_output', {}).get('concepts', []))}, "
    combined_context += f"Sensor readings: {len(sensor_data)} values, "
    combined_context += f"Image features: {image_data.numel()} pixels"
    
    reasoning_result = integration.reason_with_pln(
        f"Analyze relationships between: {combined_context}"
    )
    print(f"   Cross-modal reasoning confidence: {reasoning_result.get('confidence', 'N/A')}")

def demo_learning_and_adaptation():
    """Demonstrate learning and adaptation capabilities"""
    print("\n=== Learning and Adaptation Demo ===\n")
    
    # Create integration manager
    manager = get_integration_manager()
    
    # Create learning integration
    learning_config = {
        'neural': {'feature_dim': 256, 'hidden_dim': 512},
        'learning': {'learning_rate': 0.01, 'adaptation_rate': 0.2}
    }
    
    integration = manager.create_integration('learning_demo', learning_config)
    
    print("1. Starting learning session...")
    manager.start_learning_session('learning_demo', 'demo_session')
    
    # Simulate learning interactions
    learning_scenarios = [
        ("Mathematics is logical and precise", 0.9),
        ("Art is creative and expressive", 0.8),
        ("Science requires experimentation", 0.85),
        ("Music evokes emotions", 0.7),
        ("Programming involves problem solving", 0.95)
    ]
    
    print("2. Learning from interactions...")
    for scenario, feedback in learning_scenarios:
        integration.learn_from_interaction(scenario, feedback)
        print(f"   Learned: '{scenario[:30]}...' (feedback: {feedback})")
    
    print("\n3. Analyzing learning progress...")
    final_state = integration.get_cognitive_state()
    print(f"   Learning episodes: {len(integration.learning_history)}")
    print(f"   Memory systems updated: {final_state['memory_state']}")
    
    # End session
    session_summary = manager.end_learning_session('demo_session')
    print(f"   Session completed with {session_summary['interactions']} interactions")

def main():
    """Run all integration demos"""
    print("Starting OpenCog AI/ML Integration Demonstrations\n")
    
    try:
        demo_basic_integration()
        demo_moses_integration()
        demo_llm_integration()
        demo_multimodal_integration()
        demo_learning_and_adaptation()
        
        print("\n=== Demo Complete ===")
        print("All integration components demonstrated successfully!")
        print("\nNext steps:")
        print("- Configure actual LLM models in ai_ml_integration/llm_integration.py")
        print("- Build MOSES if you want evolutionary learning")
        print("- Set up AtomSpace persistence for production use")
        print("- Explore specific integration patterns for your use case")
        
    except Exception as e:
        logger.error(f"Demo failed: {e}")
        print(f"Demo encountered an error: {e}")

if __name__ == "__main__":
    main()

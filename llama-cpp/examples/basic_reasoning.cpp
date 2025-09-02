
#include <iostream>
#include <vector>
#include <string>

#include "../include/opencog_llama.h"
#include "../include/atomspace_llama.h"

using namespace opencog;
using namespace opencog::llama;

int main() {
    std::cout << "=== OpenCog-Llama Basic Reasoning Example ===" << std::endl;
    
    try {
        // Initialize the OpenCog-Llama system
        OpenCogLlama llama_engine;
        
        std::cout << "\n1. Initializing system..." << std::endl;
        if (!llama_engine.initialize("models/llama-7b.gguf", "")) {
            std::cerr << "Failed to initialize OpenCog-Llama system" << std::endl;
            return 1;
        }
        
        // Set up cognitive parameters
        llama_engine.set_reasoning_depth(5);
        llama_engine.set_creativity_level(0.7);
        llama_engine.set_logical_strictness(0.8);
        
        // Set up callbacks for monitoring
        llama_engine.set_reasoning_callback([](const std::string& reasoning, double confidence) {
            std::cout << "Reasoning completed with confidence: " << confidence << std::endl;
        });
        
        llama_engine.set_learning_callback([](const Handle& atom, const TruthValue& tv) {
            std::cout << "Knowledge updated: " << atom->get_name() 
                     << " (confidence: " << tv->get_confidence() << ")" << std::endl;
        });
        
        std::cout << "\n2. Creating knowledge base..." << std::endl;
        
        // Create some basic concepts
        Handle human = llama_engine.create_concept("Human", 
            SimpleTruthValue::createTV(0.9, 0.95));
        Handle animal = llama_engine.create_concept("Animal", 
            SimpleTruthValue::createTV(0.9, 0.95));
        Handle mortal = llama_engine.create_concept("Mortal", 
            SimpleTruthValue::createTV(0.9, 0.95));
        Handle socrates = llama_engine.create_concept("Socrates", 
            SimpleTruthValue::createTV(0.95, 0.99));
        
        // Create relationships
        Handle human_is_animal = llama_engine.create_relationship(human, animal, "is_a");
        Handle animal_is_mortal = llama_engine.create_relationship(animal, mortal, "is_a");
        Handle socrates_is_human = llama_engine.create_relationship(socrates, human, "is_a");
        
        std::cout << "Knowledge base created with " << llama_engine.get_knowledge_base_size() 
                 << " atoms" << std::endl;
        
        std::cout << "\n3. Performing basic reasoning..." << std::endl;
        
        // Basic deductive reasoning
        std::vector<Handle> context = {human, animal, mortal, socrates, 
                                     human_is_animal, animal_is_mortal, socrates_is_human};
        
        std::string query = "Is Socrates mortal?";
        std::string reasoning_result = llama_engine.reason(query, context);
        
        std::cout << "\nQuery: " << query << std::endl;
        std::cout << "Reasoning Result:\n" << reasoning_result << std::endl;
        
        std::cout << "\n4. Testing different types of reasoning..." << std::endl;
        
        // Analogical reasoning
        std::cout << "\n--- Analogical Reasoning ---" << std::endl;
        std::string analogy = llama_engine.analogical_reasoning(human, animal);
        std::cout << analogy << std::endl;
        
        // Causal reasoning
        std::cout << "\n--- Causal Reasoning ---" << std::endl;
        Handle cause = llama_engine.create_concept("Rain", SimpleTruthValue::createTV(0.8, 0.9));
        Handle effect = llama_engine.create_concept("WetGround", SimpleTruthValue::createTV(0.8, 0.9));
        std::string causation = llama_engine.causal_reasoning(cause, effect);
        std::cout << causation << std::endl;
        
        // Temporal reasoning
        std::cout << "\n--- Temporal Reasoning ---" << std::endl;
        std::vector<Handle> events = {
            llama_engine.create_concept("Wake_Up", SimpleTruthValue::createTV(0.9, 0.95)),
            llama_engine.create_concept("Eat_Breakfast", SimpleTruthValue::createTV(0.8, 0.9)),
            llama_engine.create_concept("Go_To_Work", SimpleTruthValue::createTV(0.85, 0.92))
        };
        std::string temporal = llama_engine.temporal_reasoning(events);
        std::cout << temporal << std::endl;
        
        std::cout << "\n5. Testing learning capabilities..." << std::endl;
        
        // Simulate learning from interaction
        llama_engine.learn_from_interaction(
            "What is the capital of France?",
            "The capital of France is Paris. Paris is a major European city known for its culture and history."
        );
        
        llama_engine.learn_from_interaction(
            "How do birds fly?",
            "Birds fly using their wings to generate lift and thrust. They have hollow bones and specialized muscles."
        );
        
        std::cout << "\n6. Testing inference capabilities..." << std::endl;
        
        // Forward inference
        Handle premise = llama_engine.create_concept("All_birds_can_fly", 
            SimpleTruthValue::createTV(0.7, 0.8));
        Handle inference_result = llama_engine.forward_inference(premise, "universal_instantiation");
        
        if (inference_result != Handle::UNDEFINED) {
            std::cout << "Forward inference result: " << inference_result->get_name() << std::endl;
        }
        
        // Backward inference
        Handle goal = llama_engine.create_concept("Prove_Socrates_is_mortal", 
            SimpleTruthValue::createTV(0.6, 0.7));
        Handle backward_result = llama_engine.backward_inference(goal);
        
        if (backward_result != Handle::UNDEFINED) {
            std::cout << "Backward inference found path to goal" << std::endl;
        }
        
        std::cout << "\n7. System analysis and metrics..." << std::endl;
        
        // Display system status
        std::cout << llama_engine.get_system_status() << std::endl;
        
        // Test explanation capabilities
        std::cout << "\n--- Explaining Reasoning ---" << std::endl;
        std::string explanation = llama_engine.explain_reasoning(socrates);
        std::cout << explanation << std::endl;
        
        // Calculate cognitive metrics
        auto metrics = utils::calculate_cognitive_metrics(llama_engine);
        std::cout << "\n--- Cognitive Metrics ---" << std::endl;
        std::cout << "Reasoning Accuracy: " << metrics.reasoning_accuracy << std::endl;
        std::cout << "Knowledge Coverage: " << metrics.knowledge_coverage << std::endl;
        std::cout << "Inference Speed: " << metrics.inference_speed << " inferences/sec" << std::endl;
        std::cout << "Active Concepts: " << metrics.active_concepts << std::endl;
        std::cout << "Learned Patterns: " << metrics.learned_patterns << std::endl;
        
        std::cout << "\n8. Saving knowledge base..." << std::endl;
        
        if (llama_engine.save_atomspace("knowledge_base_output.scm")) {
            std::cout << "Knowledge base saved successfully" << std::endl;
        } else {
            std::cout << "Failed to save knowledge base" << std::endl;
        }
        
        std::cout << "\n=== Example completed successfully ===" << std::endl;
        
        // Cleanup is automatic via destructors
        
    } catch (const LlamaInitializationError& e) {
        std::cerr << "Initialization Error: " << e.what() << std::endl;
        return 1;
    } catch (const ReasoningError& e) {
        std::cerr << "Reasoning Error: " << e.what() << std::endl;
        return 1;
    } catch (const AtomSpaceError& e) {
        std::cerr << "AtomSpace Error: " << e.what() << std::endl;
        return 1;
    } catch (const std::exception& e) {
        std::cerr << "Error: " << e.what() << std::endl;
        return 1;
    }
    
    return 0;
}

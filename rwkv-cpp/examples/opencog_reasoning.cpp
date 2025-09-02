
#include "cognitive_processor.h"
#include "atomspace_bridge.h"
#include <iostream>
#include <memory>

int main() {
    // Initialize RWKV model
    auto model = std::make_shared<rwkv::RWKVModel>();
    if (!model->load("models/rwkv-opencog.bin")) {
        std::cerr << "Failed to load RWKV model" << std::endl;
        return 1;
    }
    
    // Create cognitive processor
    rwkv::cognitive::CognitiveProcessor processor(model);
    
    // Example 1: Logical reasoning
    std::string premises = "All humans are mortal. Socrates is human.";
    std::string query = "Is Socrates mortal?";
    std::string inference_result = processor.performLogicalInference(premises, query);
    std::cout << "PLN Inference: " << inference_result << std::endl;
    
    // Example 2: Attention allocation
    std::vector<std::string> stimuli = {
        "urgent email from boss",
        "coffee getting cold", 
        "interesting research paper",
        "phone ringing"
    };
    auto attention_results = processor.allocateAttention(stimuli, 1.0);
    std::cout << "ECAN Attention Allocation:" << std::endl;
    for (const auto& item : attention_results) {
        std::cout << "  " << item << std::endl;
    }
    
    // Example 3: Pattern mining
    std::vector<std::string> corpus = {
        "The cat sat on the mat",
        "The dog ran in the park", 
        "The bird flew over the tree",
        "The fish swam in the pond"
    };
    auto patterns = processor.mineSemanticPatterns(corpus, 2);
    std::cout << "Mined Patterns:" << std::endl;
    for (const auto& pattern : patterns) {
        std::cout << "  " << pattern << std::endl;
    }
    
    return 0;
}

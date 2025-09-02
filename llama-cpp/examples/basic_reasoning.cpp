
#include "opencog_llama.h"
#include <iostream>
#include <vector>

int main() {
    using namespace opencog::llama;
    
    // Initialize the OpenCog-LLaMA system
    OpenCogLLaMA cognitive_system;
    
    // Load a model (you'll need to provide the path to your model)
    std::string model_path = "../models/llama-7b-q4_0.gguf";
    
    if (!cognitive_system.initialize(model_path)) {
        std::cerr << "Failed to initialize cognitive system" << std::endl;
        return 1;
    }
    
    std::cout << "OpenCog-LLaMA Cognitive System initialized!" << std::endl;
    
    // Example 1: Basic text generation
    std::cout << "\n=== Basic Text Generation ===" << std::endl;
    std::string prompt = "What is artificial intelligence?";
    std::string response = cognitive_system.generate_text(prompt, 150);
    std::cout << "Q: " << prompt << std::endl;
    std::cout << "A: " << response << std::endl;
    
    // Example 2: Concept reasoning
    std::cout << "\n=== Concept Reasoning ===" << std::endl;
    std::vector<std::string> concepts = {"intelligence", "learning", "reasoning", "knowledge"};
    std::string reasoning_result = cognitive_system.reason_about_concepts(concepts);
    std::cout << "Reasoning about concepts: ";
    for (const auto& concept : concepts) {
        std::cout << concept << " ";
    }
    std::cout << std::endl;
    std::cout << "Result: " << reasoning_result << std::endl;
    
    // Example 3: Pattern matching
    std::cout << "\n=== Pattern Matching ===" << std::endl;
    std::string pattern = "cognitive science";
    std::string text1 = "The study of mind and intelligence in artificial systems";
    std::string text2 = "Cooking recipes for dinner";
    
    bool match1 = cognitive_system.match_patterns(pattern, text1);
    bool match2 = cognitive_system.match_patterns(pattern, text2);
    
    std::cout << "Pattern: '" << pattern << "'" << std::endl;
    std::cout << "Text 1: '" << text1 << "' -> Match: " << (match1 ? "Yes" : "No") << std::endl;
    std::cout << "Text 2: '" << text2 << "' -> Match: " << (match2 ? "Yes" : "No") << std::endl;
    
    // Example 4: Concept extraction
    std::cout << "\n=== Concept Extraction ===" << std::endl;
    std::string complex_text = "Machine learning algorithms can process large datasets to identify patterns and make predictions about future events.";
    std::vector<std::string> extracted_concepts = cognitive_system.extract_concepts(complex_text);
    
    std::cout << "Text: " << complex_text << std::endl;
    std::cout << "Extracted concepts: ";
    for (const auto& concept : extracted_concepts) {
        std::cout << concept << " ";
    }
    std::cout << std::endl;
    
    // Example 5: AtomSpace query processing
    std::cout << "\n=== AtomSpace Query Processing ===" << std::endl;
    std::string query = "What is the relationship between learning and intelligence?";
    bool query_success = cognitive_system.process_atomspace_query(query);
    std::cout << "Query: " << query << std::endl;
    std::cout << "Processing successful: " << (query_success ? "Yes" : "No") << std::endl;
    
    std::cout << "\n=== Cognitive System Demo Complete ===" << std::endl;
    
    return 0;
}

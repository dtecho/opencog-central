
#include "opencog_llama.h"
#include <iostream>
#include <string>
#include <sstream>

class CognitiveShell {
private:
    opencog::llama::OpenCogLLaMA cognitive_system_;
    bool running_;

public:
    CognitiveShell() : running_(false) {}
    
    bool initialize(const std::string& model_path) {
        std::cout << "Initializing OpenCog-LLaMA Cognitive Shell..." << std::endl;
        if (!cognitive_system_.initialize(model_path)) {
            std::cerr << "Failed to initialize cognitive system" << std::endl;
            return false;
        }
        running_ = true;
        std::cout << "Cognitive Shell ready!" << std::endl;
        return true;
    }
    
    void run() {
        if (!running_) {
            std::cerr << "Shell not initialized" << std::endl;
            return;
        }
        
        print_help();
        
        std::string input;
        while (running_) {
            std::cout << "\ncognitive> ";
            std::getline(std::cin, input);
            
            if (input.empty()) continue;
            
            process_command(input);
        }
    }
    
private:
    void print_help() {
        std::cout << "\n=== OpenCog-LLaMA Cognitive Shell ===" << std::endl;
        std::cout << "Commands:" << std::endl;
        std::cout << "  generate <text>     - Generate text continuation" << std::endl;
        std::cout << "  reason <concepts>   - Reason about space-separated concepts" << std::endl;
        std::cout << "  match <pattern> <text> - Check if pattern matches text" << std::endl;
        std::cout << "  extract <text>      - Extract concepts from text" << std::endl;
        std::cout << "  query <question>    - Process AtomSpace query" << std::endl;
        std::cout << "  embeddings <text>   - Get text embeddings" << std::endl;
        std::cout << "  help               - Show this help" << std::endl;
        std::cout << "  exit               - Exit shell" << std::endl;
    }
    
    void process_command(const std::string& input) {
        std::istringstream iss(input);
        std::string command;
        iss >> command;
        
        if (command == "exit" || command == "quit") {
            running_ = false;
            std::cout << "Goodbye!" << std::endl;
        }
        else if (command == "help") {
            print_help();
        }
        else if (command == "generate") {
            std::string text;
            std::getline(iss, text);
            if (!text.empty()) {
                text = text.substr(1); // Remove leading space
                std::string response = cognitive_system_.generate_text(text, 150);
                std::cout << "Generated: " << response << std::endl;
            } else {
                std::cout << "Usage: generate <text>" << std::endl;
            }
        }
        else if (command == "reason") {
            std::vector<std::string> concepts;
            std::string concept;
            while (iss >> concept) {
                concepts.push_back(concept);
            }
            if (!concepts.empty()) {
                std::string result = cognitive_system_.reason_about_concepts(concepts);
                std::cout << "Reasoning result: " << result << std::endl;
            } else {
                std::cout << "Usage: reason <concept1> <concept2> ..." << std::endl;
            }
        }
        else if (command == "match") {
            std::string pattern, text;
            iss >> pattern;
            std::getline(iss, text);
            if (!pattern.empty() && !text.empty()) {
                text = text.substr(1); // Remove leading space
                bool matches = cognitive_system_.match_patterns(pattern, text);
                std::cout << "Match result: " << (matches ? "Yes" : "No") << std::endl;
            } else {
                std::cout << "Usage: match <pattern> <text>" << std::endl;
            }
        }
        else if (command == "extract") {
            std::string text;
            std::getline(iss, text);
            if (!text.empty()) {
                text = text.substr(1); // Remove leading space
                std::vector<std::string> concepts = cognitive_system_.extract_concepts(text);
                std::cout << "Extracted concepts: ";
                for (const auto& concept : concepts) {
                    std::cout << concept << " ";
                }
                std::cout << std::endl;
            } else {
                std::cout << "Usage: extract <text>" << std::endl;
            }
        }
        else if (command == "query") {
            std::string query;
            std::getline(iss, query);
            if (!query.empty()) {
                query = query.substr(1); // Remove leading space
                bool success = cognitive_system_.process_atomspace_query(query);
                std::cout << "Query processing: " << (success ? "Success" : "Failed") << std::endl;
            } else {
                std::cout << "Usage: query <question>" << std::endl;
            }
        }
        else if (command == "embeddings") {
            std::string text;
            std::getline(iss, text);
            if (!text.empty()) {
                text = text.substr(1); // Remove leading space
                std::vector<float> embeddings = cognitive_system_.get_embeddings(text);
                std::cout << "Embeddings (first 10 dimensions): ";
                for (size_t i = 0; i < std::min(embeddings.size(), size_t(10)); ++i) {
                    std::cout << embeddings[i] << " ";
                }
                std::cout << "... (" << embeddings.size() << " total)" << std::endl;
            } else {
                std::cout << "Usage: embeddings <text>" << std::endl;
            }
        }
        else {
            std::cout << "Unknown command: " << command << std::endl;
            std::cout << "Type 'help' for available commands." << std::endl;
        }
    }
};

int main(int argc, char* argv[]) {
    std::string model_path = "../models/llama-7b-q4_0.gguf";
    
    if (argc > 1) {
        model_path = argv[1];
    }
    
    CognitiveShell shell;
    if (!shell.initialize(model_path)) {
        return 1;
    }
    
    shell.run();
    return 0;
}


#include "rwkv_wrapper.h"
#include <iostream>
#include <string>
#include <memory>

int main(int argc, char* argv[]) {
    if (argc < 2) {
        std::cerr << "Usage: " << argv[0] << " <model_path> [n_threads] [n_gpu_layers]" << std::endl;
        return 1;
    }
    
    std::string model_path = argv[1];
    uint32_t n_threads = argc > 2 ? std::stoi(argv[2]) : 4;
    uint32_t n_gpu_layers = argc > 3 ? std::stoi(argv[3]) : 0;
    
    try {
        // Load model
        std::cout << "Loading RWKV model..." << std::endl;
        auto model = std::make_shared<rwkv_cpp::RWKVModel>(model_path, n_threads, n_gpu_layers);
        
        // Create text generator
        rwkv_cpp::TextGenerator generator(model);
        
        std::cout << "\n=== RWKV Chat Interface ===" << std::endl;
        std::cout << "Type 'quit' to exit" << std::endl;
        std::cout << "System info: " << rwkv_cpp::RWKVModel::get_system_info() << std::endl;
        std::cout << "============================\n" << std::endl;
        
        std::string input;
        while (true) {
            std::cout << "You: ";
            std::getline(std::cin, input);
            
            if (input == "quit" || input == "exit") {
                break;
            }
            
            if (input.empty()) {
                continue;
            }
            
            std::cout << "AI: ";
            std::string response = generator.generate(input, 50, 0.8f, 0.9f);
            std::cout << response << std::endl << std::endl;
        }
        
    } catch (const std::exception& e) {
        std::cerr << "Error: " << e.what() << std::endl;
        return 1;
    }
    
    return 0;
}

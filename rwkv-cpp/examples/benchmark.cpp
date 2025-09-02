
#include "rwkv_wrapper.h"
#include <iostream>
#include <chrono>
#include <vector>

int main(int argc, char* argv[]) {
    if (argc < 2) {
        std::cerr << "Usage: " << argv[0] << " <model_path> [n_threads] [n_tokens]" << std::endl;
        return 1;
    }
    
    std::string model_path = argv[1];
    uint32_t n_threads = argc > 2 ? std::stoi(argv[2]) : 4;
    size_t n_tokens = argc > 3 ? std::stoi(argv[3]) : 100;
    
    try {
        std::cout << "Loading model for benchmark..." << std::endl;
        rwkv_cpp::RWKVModel model(model_path, n_threads, 0);
        
        // Prepare test data
        std::vector<uint32_t> test_tokens(n_tokens);
        for (size_t i = 0; i < n_tokens; ++i) {
            test_tokens[i] = i % model.get_vocab_size();
        }
        
        std::vector<float> state_buffer(model.get_state_size(), 0.0f);
        std::vector<float> logits_buffer(model.get_logits_size());
        
        std::cout << "\n=== Benchmark Configuration ===" << std::endl;
        std::cout << "Threads: " << n_threads << std::endl;
        std::cout << "Tokens: " << n_tokens << std::endl;
        std::cout << "Model layers: " << model.get_layer_count() << std::endl;
        
        // Warmup
        std::cout << "\nWarming up..." << std::endl;
        model.eval({test_tokens[0]}, nullptr, state_buffer.data(), logits_buffer.data());
        
        // Benchmark token evaluation
        std::cout << "Running benchmark..." << std::endl;
        auto start = std::chrono::high_resolution_clock::now();
        
        for (size_t i = 0; i < n_tokens; ++i) {
            bool success = model.eval({test_tokens[i]}, 
                                     i == 0 ? nullptr : state_buffer.data(),
                                     state_buffer.data(), 
                                     logits_buffer.data());
            if (!success) {
                std::cerr << "Evaluation failed at token " << i << std::endl;
                return 1;
            }
        }
        
        auto end = std::chrono::high_resolution_clock::now();
        auto duration = std::chrono::duration_cast<std::chrono::milliseconds>(end - start);
        
        std::cout << "\n=== Benchmark Results ===" << std::endl;
        std::cout << "Total time: " << duration.count() << " ms" << std::endl;
        std::cout << "Tokens/second: " << (n_tokens * 1000.0 / duration.count()) << std::endl;
        std::cout << "Time per token: " << (duration.count() / double(n_tokens)) << " ms" << std::endl;
        
    } catch (const std::exception& e) {
        std::cerr << "Error: " << e.what() << std::endl;
        return 1;
    }
    
    return 0;
}


#include "rwkv_wrapper.h"
#include <iostream>
#include <iomanip>

int main(int argc, char* argv[]) {
    if (argc < 2) {
        std::cerr << "Usage: " << argv[0] << " <model_path>" << std::endl;
        return 1;
    }
    
    std::string model_path = argv[1];
    
    try {
        std::cout << "Loading model: " << model_path << std::endl;
        rwkv_cpp::RWKVModel model(model_path, 1, 0); // Single thread, no GPU for info only
        
        std::cout << "\n=== Model Information ===" << std::endl;
        std::cout << std::left << std::setw(20) << "Vocabulary size:" << model.get_vocab_size() << std::endl;
        std::cout << std::left << std::setw(20) << "Embedding size:" << model.get_embed_size() << std::endl;
        std::cout << std::left << std::setw(20) << "Layer count:" << model.get_layer_count() << std::endl;
        std::cout << std::left << std::setw(20) << "State size:" << model.get_state_size() << " floats" << std::endl;
        std::cout << std::left << std::setw(20) << "Logits size:" << model.get_logits_size() << " floats" << std::endl;
        
        size_t state_memory = model.get_state_size() * sizeof(float);
        size_t logits_memory = model.get_logits_size() * sizeof(float);
        
        std::cout << std::left << std::setw(20) << "State memory:" << (state_memory / 1024.0 / 1024.0) << " MB" << std::endl;
        std::cout << std::left << std::setw(20) << "Logits memory:" << (logits_memory / 1024.0 / 1024.0) << " MB" << std::endl;
        
        std::cout << "\n=== System Information ===" << std::endl;
        std::cout << rwkv_cpp::RWKVModel::get_system_info() << std::endl;
        
    } catch (const std::exception& e) {
        std::cerr << "Error: " << e.what() << std::endl;
        return 1;
    }
    
    return 0;
}

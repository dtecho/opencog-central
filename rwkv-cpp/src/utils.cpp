
#include "rwkv_wrapper.h"
#include <fstream>
#include <iostream>
#include <sstream>

namespace rwkv_cpp {

namespace utils {

bool file_exists(const std::string& path) {
    std::ifstream file(path);
    return file.good();
}

size_t get_file_size(const std::string& path) {
    std::ifstream file(path, std::ios::binary | std::ios::ate);
    if (!file.is_open()) {
        return 0;
    }
    return static_cast<size_t>(file.tellg());
}

std::string read_file(const std::string& path) {
    std::ifstream file(path);
    if (!file.is_open()) {
        return "";
    }
    
    std::stringstream buffer;
    buffer << file.rdbuf();
    return buffer.str();
}

bool write_file(const std::string& path, const std::string& content) {
    std::ofstream file(path);
    if (!file.is_open()) {
        return false;
    }
    
    file << content;
    return file.good();
}

void print_model_info(const RWKVModel& model) {
    if (!model.is_loaded()) {
        std::cout << "Model not loaded." << std::endl;
        return;
    }
    
    std::cout << "=== RWKV Model Information ===" << std::endl;
    std::cout << "Vocabulary size: " << model.get_vocab_size() << std::endl;
    std::cout << "Embedding size: " << model.get_embed_size() << std::endl;
    std::cout << "Layer count: " << model.get_layer_count() << std::endl;
    std::cout << "State buffer size: " << model.get_state_size() << std::endl;
    std::cout << "Logits buffer size: " << model.get_logits_size() << std::endl;
    std::cout << "=============================" << std::endl;
}

} // namespace utils

} // namespace rwkv_cpp

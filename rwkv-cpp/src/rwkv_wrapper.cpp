
#include "rwkv_wrapper.h"
#include <iostream>
#include <stdexcept>
#include <cstring>

namespace rwkv_cpp {

RWKVModel::RWKVModel(const std::string& model_path, uint32_t n_threads, uint32_t n_gpu_layers)
    : ctx_(nullptr), model_path_(model_path), n_threads_(n_threads), n_gpu_layers_(n_gpu_layers) {
    
    // Initialize RWKV context
    ctx_ = rwkv_init_from_file(model_path.c_str(), n_threads, n_gpu_layers);
    
    if (!ctx_) {
        throw std::runtime_error("Failed to load RWKV model from: " + model_path);
    }
    
    std::cout << "RWKV model loaded successfully:" << std::endl;
    std::cout << "  Vocab size: " << get_vocab_size() << std::endl;
    std::cout << "  Embed size: " << get_embed_size() << std::endl;
    std::cout << "  Layers: " << get_layer_count() << std::endl;
    std::cout << "  State size: " << get_state_size() << std::endl;
    std::cout << "  GPU layers: " << n_gpu_layers << std::endl;
}

RWKVModel::~RWKVModel() {
    if (ctx_) {
        rwkv_free(ctx_);
        ctx_ = nullptr;
    }
}

bool RWKVModel::eval(const std::vector<uint32_t>& tokens, 
                     const float* state_in, 
                     float* state_out, 
                     float* logits_out) {
    if (!ctx_) {
        return false;
    }
    
    for (size_t i = 0; i < tokens.size(); ++i) {
        bool success = rwkv_eval(ctx_, tokens[i], state_in, state_out, logits_out);
        if (!success) {
            return false;
        }
        // For multi-token sequences, output state becomes input state for next token
        state_in = state_out;
    }
    
    return true;
}

size_t RWKVModel::get_vocab_size() const {
    return ctx_ ? rwkv_get_n_vocab(ctx_) : 0;
}

size_t RWKVModel::get_embed_size() const {
    return ctx_ ? rwkv_get_n_embed(ctx_) : 0;
}

size_t RWKVModel::get_layer_count() const {
    return ctx_ ? rwkv_get_n_layer(ctx_) : 0;
}

size_t RWKVModel::get_state_size() const {
    return ctx_ ? rwkv_get_state_len(ctx_) : 0;
}

size_t RWKVModel::get_logits_size() const {
    return ctx_ ? rwkv_get_logits_len(ctx_) : 0;
}

std::string RWKVModel::get_system_info() {
    const char* info = rwkv_get_system_info_string();
    return info ? std::string(info) : "";
}

} // namespace rwkv_cpp

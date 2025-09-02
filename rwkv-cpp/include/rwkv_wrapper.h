
#pragma once

#include <string>
#include <vector>
#include <memory>
#include <functional>

extern "C" {
    #include "rwkv.h"
}

namespace rwkv_cpp {

/**
 * @brief RWKV Model wrapper class for C++ interface
 */
class RWKVModel {
public:
    /**
     * @brief Construct a new RWKV Model object
     * 
     * @param model_path Path to the RWKV model file
     * @param n_threads Number of threads to use
     * @param n_gpu_layers Number of layers to offload to GPU
     */
    RWKVModel(const std::string& model_path, uint32_t n_threads = 4, uint32_t n_gpu_layers = 0);
    
    /**
     * @brief Destroy the RWKV Model object
     */
    ~RWKVModel();
    
    /**
     * @brief Evaluate tokens and update model state
     * 
     * @param tokens Input tokens
     * @param state_in Input state (nullptr for initial state)
     * @param state_out Output state buffer
     * @param logits_out Output logits buffer
     * @return true if successful
     */
    bool eval(const std::vector<uint32_t>& tokens, 
              const float* state_in, 
              float* state_out, 
              float* logits_out);
    
    /**
     * @brief Get vocabulary size
     */
    size_t get_vocab_size() const;
    
    /**
     * @brief Get embedding size
     */
    size_t get_embed_size() const;
    
    /**
     * @brief Get number of layers
     */
    size_t get_layer_count() const;
    
    /**
     * @brief Get state buffer size
     */
    size_t get_state_size() const;
    
    /**
     * @brief Get logits buffer size
     */
    size_t get_logits_size() const;
    
    /**
     * @brief Check if model is loaded successfully
     */
    bool is_loaded() const { return ctx_ != nullptr; }
    
    /**
     * @brief Get system info string
     */
    static std::string get_system_info();

private:
    struct rwkv_context* ctx_;
    std::string model_path_;
    uint32_t n_threads_;
    uint32_t n_gpu_layers_;
};

/**
 * @brief Text generation utilities
 */
class TextGenerator {
public:
    TextGenerator(std::shared_ptr<RWKVModel> model);
    
    /**
     * @brief Generate text from prompt
     */
    std::string generate(const std::string& prompt, 
                        size_t max_tokens = 100,
                        float temperature = 1.0f,
                        float top_p = 0.9f);
    
    /**
     * @brief Set tokenizer (placeholder for future implementation)
     */
    void set_tokenizer(const std::string& tokenizer_path);

private:
    std::shared_ptr<RWKVModel> model_;
    std::vector<float> state_buffer_;
    std::vector<float> logits_buffer_;
    
    // Simple tokenization (to be replaced with proper tokenizer)
    std::vector<uint32_t> tokenize(const std::string& text);
    std::string detokenize(const std::vector<uint32_t>& tokens);
    uint32_t sample_token(const float* logits, float temperature, float top_p);
};

} // namespace rwkv_cpp

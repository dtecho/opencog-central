
#include "rwkv_wrapper.h"
#include <random>
#include <algorithm>
#include <sstream>
#include <iostream>

namespace rwkv_cpp {

TextGenerator::TextGenerator(std::shared_ptr<RWKVModel> model) 
    : model_(model) {
    if (!model_ || !model_->is_loaded()) {
        throw std::runtime_error("Invalid or unloaded RWKV model");
    }
    
    // Initialize buffers
    state_buffer_.resize(model_->get_state_size());
    logits_buffer_.resize(model_->get_logits_size());
    
    // Initialize state to zeros (initial state)
    std::fill(state_buffer_.begin(), state_buffer_.end(), 0.0f);
}

std::string TextGenerator::generate(const std::string& prompt, 
                                   size_t max_tokens,
                                   float temperature,
                                   float top_p) {
    if (!model_->is_loaded()) {
        return "";
    }
    
    // Tokenize prompt
    auto prompt_tokens = tokenize(prompt);
    if (prompt_tokens.empty()) {
        return "";
    }
    
    std::vector<uint32_t> generated_tokens = prompt_tokens;
    
    // Process prompt tokens
    bool success = model_->eval(prompt_tokens, nullptr, 
                               state_buffer_.data(), logits_buffer_.data());
    if (!success) {
        std::cerr << "Failed to evaluate prompt tokens" << std::endl;
        return "";
    }
    
    // Generate tokens
    for (size_t i = 0; i < max_tokens; ++i) {
        // Sample next token
        uint32_t next_token = sample_token(logits_buffer_.data(), temperature, top_p);
        generated_tokens.push_back(next_token);
        
        // Check for end token (simple check)
        if (next_token == 0) {
            break;
        }
        
        // Evaluate next token
        std::vector<uint32_t> single_token = {next_token};
        success = model_->eval(single_token, state_buffer_.data(), 
                              state_buffer_.data(), logits_buffer_.data());
        if (!success) {
            std::cerr << "Failed to evaluate generated token" << std::endl;
            break;
        }
    }
    
    return detokenize(generated_tokens);
}

void TextGenerator::set_tokenizer(const std::string& tokenizer_path) {
    // TODO: Implement proper tokenizer loading
    std::cout << "Tokenizer loading not yet implemented: " << tokenizer_path << std::endl;
}

std::vector<uint32_t> TextGenerator::tokenize(const std::string& text) {
    // Simple character-based tokenization (placeholder)
    // In a real implementation, you would use a proper tokenizer
    std::vector<uint32_t> tokens;
    for (char c : text) {
        tokens.push_back(static_cast<uint32_t>(c));
    }
    return tokens;
}

std::string TextGenerator::detokenize(const std::vector<uint32_t>& tokens) {
    // Simple character-based detokenization (placeholder)
    std::string text;
    for (uint32_t token : tokens) {
        if (token < 256) { // ASCII range
            text += static_cast<char>(token);
        }
    }
    return text;
}

uint32_t TextGenerator::sample_token(const float* logits, float temperature, float top_p) {
    size_t vocab_size = model_->get_vocab_size();
    
    // Apply temperature
    std::vector<float> probs(vocab_size);
    float max_logit = *std::max_element(logits, logits + vocab_size);
    
    float sum = 0.0f;
    for (size_t i = 0; i < vocab_size; ++i) {
        probs[i] = std::exp((logits[i] - max_logit) / temperature);
        sum += probs[i];
    }
    
    // Normalize
    for (size_t i = 0; i < vocab_size; ++i) {
        probs[i] /= sum;
    }
    
    // Top-p sampling
    std::vector<std::pair<float, uint32_t>> prob_indices;
    for (size_t i = 0; i < vocab_size; ++i) {
        prob_indices.emplace_back(probs[i], i);
    }
    
    std::sort(prob_indices.rbegin(), prob_indices.rend());
    
    float cumulative_prob = 0.0f;
    size_t top_k = 0;
    for (size_t i = 0; i < vocab_size; ++i) {
        cumulative_prob += prob_indices[i].first;
        top_k = i + 1;
        if (cumulative_prob >= top_p) {
            break;
        }
    }
    
    // Sample from top-k
    static std::random_device rd;
    static std::mt19937 gen(rd());
    std::uniform_real_distribution<float> dis(0.0f, cumulative_prob);
    
    float sample = dis(gen);
    cumulative_prob = 0.0f;
    for (size_t i = 0; i < top_k; ++i) {
        cumulative_prob += prob_indices[i].first;
        if (sample <= cumulative_prob) {
            return prob_indices[i].second;
        }
    }
    
    return prob_indices[0].second; // Fallback to most likely token
}

} // namespace rwkv_cpp

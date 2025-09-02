
#include "opencog_llama.h"
#include "atomspace_llama.h"
#include <iostream>
#include <fstream>
#include <sstream>
#include <algorithm>

namespace opencog {
namespace llama {

OpenCogLLaMA::OpenCogLLaMA() 
    : ctx_(nullptr), model_(nullptr), initialized_(false) {
    atomspace_ = std::make_unique<AtomSpaceInterface>();
    cognitive_model_ = std::make_unique<CognitiveModel>(this);
}

OpenCogLLaMA::~OpenCogLLaMA() {
    shutdown();
}

bool OpenCogLLaMA::initialize(const std::string& model_path) {
    if (initialized_) {
        return true;
    }

    // Initialize llama backend
    llama_backend_init();
    
    // Load model
    llama_model_params model_params = llama_model_default_params();
    model_params.n_gpu_layers = 0; // CPU only for now
    
    model_ = llama_load_model_from_file(model_path.c_str(), model_params);
    if (!model_) {
        std::cerr << "Failed to load model: " << model_path << std::endl;
        return false;
    }

    // Create context
    llama_context_params ctx_params = llama_context_default_params();
    ctx_params.n_ctx = 2048;
    ctx_params.seed = 42;
    
    ctx_ = llama_new_context_with_model(model_, ctx_params);
    if (!ctx_) {
        std::cerr << "Failed to create context" << std::endl;
        llama_free_model(model_);
        model_ = nullptr;
        return false;
    }

    initialized_ = true;
    std::cout << "OpenCog-LLaMA initialized successfully" << std::endl;
    return true;
}

void OpenCogLLaMA::shutdown() {
    if (ctx_) {
        llama_free(ctx_);
        ctx_ = nullptr;
    }
    if (model_) {
        llama_free_model(model_);
        model_ = nullptr;
    }
    llama_backend_free();
    initialized_ = false;
}

std::string OpenCogLLaMA::generate_text(const std::string& prompt, int max_tokens) {
    if (!initialized_) {
        return "Error: Model not initialized";
    }

    // Tokenize prompt
    std::vector<llama_token> tokens;
    tokens.resize(prompt.length() + 1);
    int n_tokens = llama_tokenize(model_, prompt.c_str(), prompt.length(), 
                                  tokens.data(), tokens.size(), true, true);
    tokens.resize(n_tokens);

    // Generate response
    std::string response;
    llama_batch batch = llama_batch_init(tokens.size(), 0, 1);
    
    // Add tokens to batch
    for (size_t i = 0; i < tokens.size(); i++) {
        llama_batch_add(batch, tokens[i], i, {0}, false);
    }
    batch.logits[batch.n_tokens - 1] = true;

    // Decode
    if (llama_decode(ctx_, batch) != 0) {
        llama_batch_free(batch);
        return "Error: Failed to decode";
    }

    // Sample next tokens
    for (int i = 0; i < max_tokens; i++) {
        llama_token new_token_id = llama_sample_token_greedy(ctx_, nullptr);
        
        if (llama_token_is_eog(model_, new_token_id)) {
            break;
        }

        char buf[128];
        int n_chars = llama_token_to_piece(model_, new_token_id, buf, sizeof(buf), 0, true);
        if (n_chars > 0) {
            response.append(buf, n_chars);
        }

        // Add to batch for next iteration
        llama_batch_clear(batch);
        llama_batch_add(batch, new_token_id, tokens.size() + i, {0}, true);
        
        if (llama_decode(ctx_, batch) != 0) {
            break;
        }
    }

    llama_batch_free(batch);
    return response;
}

std::vector<float> OpenCogLLaMA::get_embeddings(const std::string& text) {
    if (!initialized_) {
        return {};
    }

    // Tokenize text
    std::vector<llama_token> tokens;
    tokens.resize(text.length() + 1);
    int n_tokens = llama_tokenize(model_, text.c_str(), text.length(), 
                                  tokens.data(), tokens.size(), true, true);
    tokens.resize(n_tokens);

    // Get embeddings (simplified approach)
    std::vector<float> embeddings;
    int n_embd = llama_n_embd(model_);
    embeddings.resize(n_embd);

    // Create batch and decode
    llama_batch batch = llama_batch_init(tokens.size(), 0, 1);
    for (size_t i = 0; i < tokens.size(); i++) {
        llama_batch_add(batch, tokens[i], i, {0}, false);
    }
    batch.logits[batch.n_tokens - 1] = true;

    if (llama_decode(ctx_, batch) == 0) {
        // Get the embeddings from the last layer
        float* embd = llama_get_embeddings(ctx_);
        if (embd) {
            std::copy(embd, embd + n_embd, embeddings.begin());
        }
    }

    llama_batch_free(batch);
    return embeddings;
}

bool OpenCogLLaMA::process_atomspace_query(const std::string& query) {
    if (!atomspace_) {
        return false;
    }

    // Format query for reasoning
    std::string formatted_query = utils::format_prompt_for_reasoning(query);
    
    // Generate response using LLaMA
    std::string llama_response = generate_text(formatted_query, 200);
    
    // Process response through AtomSpace
    std::vector<std::string> concepts = utils::tokenize_for_opencog(llama_response);
    
    // Store results in AtomSpace
    for (const auto& concept : concepts) {
        atomspace_->create_atom_from_text(concept, "ConceptNode");
    }
    
    return utils::validate_cognitive_response(llama_response);
}

std::string OpenCogLLaMA::reason_about_concepts(const std::vector<std::string>& concepts) {
    if (!cognitive_model_) {
        return "Error: Cognitive model not available";
    }

    // Use the cognitive model for reasoning
    std::string reasoning_result = cognitive_model_->reason_inductively(concepts);
    
    // Store learned knowledge
    atomspace_->store_generated_knowledge(reasoning_result);
    
    return reasoning_result;
}

bool OpenCogLLaMA::match_patterns(const std::string& pattern, const std::string& text) {
    // Generate embeddings for both pattern and text
    std::vector<float> pattern_emb = get_embeddings(pattern);
    std::vector<float> text_emb = get_embeddings(text);
    
    if (pattern_emb.empty() || text_emb.empty() || pattern_emb.size() != text_emb.size()) {
        return false;
    }
    
    // Calculate cosine similarity
    float dot_product = 0.0f;
    float norm_pattern = 0.0f;
    float norm_text = 0.0f;
    
    for (size_t i = 0; i < pattern_emb.size(); ++i) {
        dot_product += pattern_emb[i] * text_emb[i];
        norm_pattern += pattern_emb[i] * pattern_emb[i];
        norm_text += text_emb[i] * text_emb[i];
    }
    
    float similarity = dot_product / (std::sqrt(norm_pattern) * std::sqrt(norm_text));
    
    // Threshold for pattern matching
    return similarity > 0.8f;
}

std::vector<std::string> OpenCogLLaMA::extract_concepts(const std::string& text) {
    // Use LLaMA to identify key concepts
    std::string concept_prompt = "Extract key concepts from: " + text + "\nConcepts:";
    std::string response = generate_text(concept_prompt, 100);
    
    return utils::tokenize_for_opencog(response);
}

// Utility functions
namespace utils {

std::string format_prompt_for_reasoning(const std::string& query) {
    return "Think step by step about: " + query + "\nReasoning:";
}

std::vector<std::string> tokenize_for_opencog(const std::string& text) {
    std::vector<std::string> tokens;
    std::istringstream iss(text);
    std::string token;
    
    while (iss >> token) {
        // Clean token (remove punctuation, convert to lowercase, etc.)
        token.erase(std::remove_if(token.begin(), token.end(), 
                   [](char c) { return !std::isalnum(c); }), token.end());
        
        if (!token.empty()) {
            std::transform(token.begin(), token.end(), token.begin(), ::tolower);
            tokens.push_back(token);
        }
    }
    
    return tokens;
}

bool validate_cognitive_response(const std::string& response) {
    // Basic validation - check if response is non-empty and meaningful
    return !response.empty() && response.length() > 10;
}

} // namespace utils

} // namespace llama
} // namespace opencog

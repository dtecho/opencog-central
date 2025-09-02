
#ifndef OPENCOG_LLAMA_H
#define OPENCOG_LLAMA_H

#include "llama.h"
#include "ggml.h"
#include <string>
#include <vector>
#include <memory>

namespace opencog {
namespace llama {

// Forward declarations
class AtomSpaceInterface;
class CognitiveModel;

/**
 * Main OpenCog-LLaMA integration class
 */
class OpenCogLLaMA {
public:
    OpenCogLLaMA();
    ~OpenCogLLaMA();

    // Initialization
    bool initialize(const std::string& model_path);
    void shutdown();

    // Core inference
    std::string generate_text(const std::string& prompt, int max_tokens = 100);
    std::vector<float> get_embeddings(const std::string& text);
    
    // Cognitive processing
    bool process_atomspace_query(const std::string& query);
    std::string reason_about_concepts(const std::vector<std::string>& concepts);
    
    // Pattern matching integration
    bool match_patterns(const std::string& pattern, const std::string& text);
    std::vector<std::string> extract_concepts(const std::string& text);

private:
    struct llama_context* ctx_;
    struct llama_model* model_;
    std::unique_ptr<AtomSpaceInterface> atomspace_;
    std::unique_ptr<CognitiveModel> cognitive_model_;
    
    bool initialized_;
};

/**
 * Utility functions for OpenCog-LLaMA integration
 */
namespace utils {
    std::string format_prompt_for_reasoning(const std::string& query);
    std::vector<std::string> tokenize_for_opencog(const std::string& text);
    bool validate_cognitive_response(const std::string& response);
}

} // namespace llama
} // namespace opencog

#endif // OPENCOG_LLAMA_H


#ifndef OPENCOG_LLAMA_H
#define OPENCOG_LLAMA_H

#include <string>
#include <vector>
#include <memory>
#include <functional>
#include <map>

// Forward declarations for OpenCog types
namespace opencog {
    class AtomSpace;
    class Handle;
    class Atom;
    class TruthValue;
}

// Forward declarations for llama.cpp types
struct llama_context;
struct llama_model;
struct llama_model_params;
struct llama_context_params;

namespace opencog {
namespace llama {

/**
 * Main interface for OpenCog-Llama integration
 * Provides cognitive reasoning capabilities using llama.cpp backend
 */
class OpenCogLlama {
public:
    // Constructor/Destructor
    OpenCogLlama();
    ~OpenCogLlama();
    
    // Initialization
    bool initialize(const std::string& model_path, 
                   const std::string& atomspace_config = "");
    void shutdown();
    
    // Core cognitive functions
    std::string reason(const std::string& query, 
                      const std::vector<Handle>& context = {});
    std::string generate_response(const std::string& prompt);
    std::string explain_reasoning(const Handle& atom);
    
    // AtomSpace integration
    bool load_atomspace(const std::string& atomspace_file);
    bool save_atomspace(const std::string& atomspace_file);
    Handle create_concept(const std::string& name, const TruthValue& tv);
    Handle create_relationship(const Handle& source, const Handle& target, 
                              const std::string& relation_type);
    
    // Pattern matching and inference
    std::vector<Handle> pattern_match(const Handle& pattern);
    Handle forward_inference(const Handle& premise, const std::string& rule);
    Handle backward_inference(const Handle& goal);
    
    // Learning and adaptation
    void learn_from_interaction(const std::string& input, const std::string& output);
    void update_knowledge(const Handle& atom, const TruthValue& new_tv);
    double get_confidence(const Handle& atom);
    
    // Cognitive metrics
    double get_reasoning_confidence() const;
    size_t get_knowledge_base_size() const;
    std::string get_system_status() const;
    
    // Advanced cognitive operations
    std::string analogical_reasoning(const Handle& source_domain, 
                                   const Handle& target_domain);
    std::string causal_reasoning(const Handle& cause, const Handle& effect);
    std::string temporal_reasoning(const std::vector<Handle>& events);
    
    // Configuration
    void set_reasoning_depth(int depth);
    void set_creativity_level(double level);
    void set_logical_strictness(double strictness);
    
    // Callbacks for cognitive events
    using ReasoningCallback = std::function<void(const std::string&, double)>;
    using LearningCallback = std::function<void(const Handle&, const TruthValue&)>;
    
    void set_reasoning_callback(ReasoningCallback callback);
    void set_learning_callback(LearningCallback callback);

private:
    // Internal implementation
    class Impl;
    std::unique_ptr<Impl> pImpl;
    
    // Helper methods
    std::string atomspace_to_prompt(const std::vector<Handle>& atoms);
    Handle prompt_to_atomspace(const std::string& response);
    void initialize_cognitive_rules();
    void process_llama_output(const std::string& output);
};

/**
 * Cognitive Shell for interactive reasoning
 */
class CognitiveShell {
public:
    CognitiveShell(OpenCogLlama& llama_engine);
    
    void start_interactive_session();
    void execute_command(const std::string& command);
    void load_script(const std::string& script_path);
    
    // Command handlers
    void handle_query(const std::string& query);
    void handle_learn(const std::string& knowledge);
    void handle_analyze(const std::string& concept);
    void handle_compare(const std::string& concept1, const std::string& concept2);
    
private:
    OpenCogLlama& llama_;
    std::map<std::string, std::function<void(const std::string&)>> commands_;
    void initialize_commands();
};

/**
 * Utility functions for cognitive processing
 */
namespace utils {
    std::string format_atomspace_knowledge(const std::vector<Handle>& atoms);
    std::vector<std::string> tokenize_reasoning_steps(const std::string& reasoning);
    double calculate_semantic_similarity(const Handle& atom1, const Handle& atom2);
    Handle find_most_relevant_atom(const std::string& query, const std::vector<Handle>& candidates);
    
    // Cognitive metrics
    struct CognitiveMetrics {
        double reasoning_accuracy;
        double knowledge_coverage;
        double inference_speed;
        size_t active_concepts;
        size_t learned_patterns;
    };
    
    CognitiveMetrics calculate_cognitive_metrics(const OpenCogLlama& engine);
}

/**
 * Exception classes for error handling
 */
class LlamaInitializationError : public std::runtime_error {
public:
    explicit LlamaInitializationError(const std::string& msg) 
        : std::runtime_error(msg) {}
};

class AtomSpaceError : public std::runtime_error {
public:
    explicit AtomSpaceError(const std::string& msg) 
        : std::runtime_error(msg) {}
};

class ReasoningError : public std::runtime_error {
public:
    explicit ReasoningError(const std::string& msg) 
        : std::runtime_error(msg) {}
};

} // namespace llama
} // namespace opencog

#endif // OPENCOG_LLAMA_H

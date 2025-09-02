
#ifndef ATOMSPACE_LLAMA_H
#define ATOMSPACE_LLAMA_H

#include "opencog_llama.h"
#include <map>
#include <functional>

namespace opencog {
namespace llama {

/**
 * Interface between AtomSpace and LLaMA models
 */
class AtomSpaceInterface {
public:
    AtomSpaceInterface();
    ~AtomSpaceInterface();

    // Atom manipulation
    bool create_atom_from_text(const std::string& text, const std::string& type);
    std::string get_atom_as_text(const std::string& atom_id);
    
    // Knowledge queries
    std::vector<std::string> query_related_atoms(const std::string& concept);
    bool update_atom_relationships(const std::string& subject, 
                                  const std::string& predicate, 
                                  const std::string& object);
    
    // Inference integration
    std::string perform_logical_inference(const std::string& premise);
    bool validate_logical_consistency(const std::vector<std::string>& statements);
    
    // Memory management
    void store_generated_knowledge(const std::string& knowledge);
    std::vector<std::string> retrieve_relevant_knowledge(const std::string& query);

private:
    std::map<std::string, std::string> atom_cache_;
    std::map<std::string, std::vector<std::string>> relationship_graph_;
    
    // Internal methods
    void initialize_atomspace();
    void cleanup_atomspace();
    std::string generate_atom_id(const std::string& content);
};

/**
 * Cognitive model that combines LLaMA with symbolic reasoning
 */
class CognitiveModel {
public:
    CognitiveModel(OpenCogLLaMA* llama_instance);
    ~CognitiveModel();

    // High-level cognitive functions
    std::string reason_deductively(const std::string& premise1, const std::string& premise2);
    std::string reason_inductively(const std::vector<std::string>& examples);
    std::string reason_abductively(const std::string& observation);
    
    // Pattern recognition
    std::vector<std::string> identify_patterns(const std::vector<std::string>& data);
    bool classify_concept(const std::string& concept, const std::string& category);
    
    // Learning and adaptation
    void learn_from_interaction(const std::string& input, const std::string& output);
    void update_knowledge_base(const std::vector<std::string>& new_facts);

private:
    OpenCogLLaMA* llama_;
    std::map<std::string, float> concept_weights_;
    std::vector<std::string> learned_patterns_;
    
    // Cognitive processing helpers
    std::string combine_symbolic_and_neural(const std::string& symbolic_input,
                                          const std::string& neural_input);
    float calculate_confidence(const std::string& reasoning_chain);
};

} // namespace llama
} // namespace opencog

#endif // ATOMSPACE_LLAMA_H


#ifndef ATOMSPACE_LLAMA_H
#define ATOMSPACE_LLAMA_H

#include <opencog/atomspace/AtomSpace.h>
#include <opencog/atoms/base/Handle.h>
#include <opencog/atoms/base/Node.h>
#include <opencog/atoms/base/Link.h>
#include <opencog/atoms/truthvalue/TruthValue.h>
#include <opencog/query/BindLinkAPI.h>

#include <string>
#include <vector>
#include <memory>

namespace opencog {
namespace llama {

/**
 * AtomSpace bridge for llama.cpp integration
 * Handles conversion between AtomSpace knowledge representation and LLM prompts
 */
class AtomSpaceLlama {
public:
    explicit AtomSpaceLlama(AtomSpace& atomspace);
    ~AtomSpaceLlama();
    
    // AtomSpace to LLM conversion
    std::string atoms_to_natural_language(const HandleSeq& atoms);
    std::string atom_to_description(const Handle& atom);
    std::string truthvalue_to_confidence(const TruthValue& tv);
    
    // LLM to AtomSpace conversion
    Handle natural_language_to_atoms(const std::string& text);
    HandleSeq parse_reasoning_chain(const std::string& reasoning);
    TruthValue parse_confidence(const std::string& confidence_text);
    
    // Knowledge extraction and representation
    HandleSeq extract_concepts(const std::string& text);
    HandleSeq extract_relationships(const std::string& text);
    Handle create_inference_link(const Handle& premise, const Handle& conclusion, 
                                const TruthValue& strength);
    
    // Pattern matching with LLM assistance
    HandleSeq llm_guided_pattern_match(const Handle& pattern);
    Handle find_similar_concept(const std::string& description);
    HandleSeq find_related_atoms(const Handle& atom, int max_depth = 3);
    
    // Reasoning support
    std::string explain_atom_relationships(const Handle& atom);
    std::string generate_hypothesis(const HandleSeq& evidence);
    HandleSeq validate_reasoning_chain(const HandleSeq& steps);
    
    // Learning and knowledge acquisition
    void learn_from_example(const std::string& example, const HandleSeq& relevant_atoms);
    void update_concept_knowledge(const Handle& concept, const std::string& new_info);
    void strengthen_associations(const HandleSeq& atoms);
    
    // Query processing
    std::string process_natural_query(const std::string& query);
    HandleSeq find_query_relevant_atoms(const std::string& query);
    std::string format_query_response(const HandleSeq& results);
    
    // Cognitive architectures support
    void integrate_with_pln(const std::string& pln_rules_path);
    void integrate_with_moses(const std::string& moses_config);
    void integrate_with_attention(double min_sti_threshold);
    
    // Serialization and persistence
    std::string serialize_knowledge_subset(const HandleSeq& atoms);
    bool load_knowledge_from_text(const std::string& knowledge_text);
    void export_reasoning_trace(const std::string& filename);
    
    // Metrics and analysis
    double calculate_knowledge_coherence();
    std::vector<Handle> identify_knowledge_gaps();
    std::string generate_knowledge_summary();
    
    // Configuration
    void set_verbosity_level(int level);
    void set_reasoning_timeout(int seconds);
    void enable_experimental_features(bool enable);
    
private:
    AtomSpace& atomspace_;
    
    // Internal helper methods
    std::string handle_to_string(const Handle& h);
    Type get_atom_type_from_string(const std::string& type_name);
    std::string normalize_text(const std::string& text);
    std::vector<std::string> tokenize_sentence(const std::string& sentence);
    
    // Pattern recognition helpers
    bool is_concept_word(const std::string& word);
    bool is_relationship_phrase(const std::string& phrase);
    std::string extract_relationship_type(const std::string& sentence);
    
    // Reasoning validation
    bool is_valid_inference(const Handle& premise, const Handle& conclusion);
    double calculate_inference_strength(const HandleSeq& premises, const Handle& conclusion);
    
    // Configuration state
    int verbosity_level_;
    int reasoning_timeout_;
    bool experimental_features_;
    
    // Statistics
    size_t queries_processed_;
    size_t atoms_created_;
    size_t inferences_made_;
};

/**
 * Specialized classes for different cognitive operations
 */

/**
 * Handles analogical reasoning using AtomSpace and LLM
 */
class AnalogicalReasoner {
public:
    AnalogicalReasoner(AtomSpace& atomspace, AtomSpaceLlama& llama_bridge);
    
    Handle find_analogy(const Handle& source_domain, const Handle& target_domain);
    std::string explain_analogy(const Handle& analogy_atom);
    double calculate_analogy_strength(const Handle& analogy);
    
private:
    AtomSpace& atomspace_;
    AtomSpaceLlama& llama_bridge_;
};

/**
 * Handles causal reasoning
 */
class CausalReasoner {
public:
    CausalReasoner(AtomSpace& atomspace, AtomSpaceLlama& llama_bridge);
    
    Handle infer_causation(const Handle& cause, const Handle& effect);
    HandleSeq find_causal_chain(const Handle& initial_cause, const Handle& final_effect);
    std::string explain_causation(const Handle& causal_link);
    
private:
    AtomSpace& atomspace_;
    AtomSpaceLlama& llama_bridge_;
};

/**
 * Handles temporal reasoning
 */
class TemporalReasoner {
public:
    TemporalReasoner(AtomSpace& atomspace, AtomSpaceLlama& llama_bridge);
    
    HandleSeq order_events_temporally(const HandleSeq& events);
    Handle predict_next_event(const HandleSeq& event_sequence);
    std::string explain_temporal_relationship(const Handle& event1, const Handle& event2);
    
private:
    AtomSpace& atomspace_;
    AtomSpaceLlama& llama_bridge_;
};

} // namespace llama
} // namespace opencog

#endif // ATOMSPACE_LLAMA_H

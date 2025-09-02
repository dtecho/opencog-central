
#pragma once

#include <string>
#include <thread>
#include <memory>
#include <vector>
#include <map>
#include <mutex>
#include <queue>

struct CognitiveContext {
    std::string conversation_id;
    std::vector<std::string> memory_stack;
    std::map<std::string, float> attention_weights;
    float coherence_score;
    std::string current_goal;
};

struct AtomSpaceQuery {
    std::string query_type;
    std::string query_content;
    std::map<std::string, std::string> parameters;
    std::string callback_id;
};

class KogServerBridge {
public:
    KogServerBridge();
    ~KogServerBridge();
    
    void initialize(const std::string& model_path, int port, int context_size, int gpu_layers);
    void start_server();
    void shutdown_server();
    
    // Text generation with cognitive enhancement
    std::string generate_text(const std::string& prompt, int max_tokens = 256);
    std::string generate_with_context(const std::string& prompt, const CognitiveContext& context, int max_tokens = 256);
    
    // AtomSpace integration
    void process_atomspace_query(const std::string& query);
    void execute_pln_inference(const std::string& premises, const std::string& target);
    void update_attention_allocation(const std::map<std::string, float>& weights);
    
    // Memory and learning
    void store_episodic_memory(const std::string& episode, const std::string& context);
    std::vector<std::string> retrieve_relevant_memories(const std::string& query, int limit = 5);
    void reinforce_learning_pattern(const std::string& pattern, float reward);
    
    // Cognitive assessment
    float evaluate_response_coherence(const std::string& response, const std::string& context);
    void adjust_generation_parameters(float coherence_threshold);
    
    // Real-time cognitive monitoring
    void start_cognitive_monitoring();
    void stop_cognitive_monitoring();
    std::map<std::string, float> get_cognitive_metrics();
    
private:
    std::string model_path;
    int port;
    int context_size;
    int gpu_layers;
    
    std::thread server_thread;
    std::thread cognitive_monitor_thread;
    bool monitoring_active;
    
    // Cognitive state management
    std::map<std::string, CognitiveContext> active_contexts;
    std::queue<AtomSpaceQuery> query_queue;
    std::mutex context_mutex;
    std::mutex query_mutex;
    
    // Memory systems
    std::vector<std::string> episodic_memory;
    std::map<std::string, std::vector<std::string>> semantic_memory;
    std::map<std::string, float> learned_patterns;
    
    // Core processing methods
    void run_server_loop();
    void run_cognitive_monitor();
    void process_query_queue();
    void update_cognitive_state(const std::string& input, const std::string& output);
    
    // AtomSpace interface
    void connect_to_atomspace();
    void sync_with_atomspace();
    std::string query_atomspace(const std::string& query);
    void insert_atom(const std::string& atom_expression);
    
    // PLN reasoning
    void setup_pln_rules();
    std::string execute_reasoning_chain(const std::string& query);
    float calculate_truth_value(const std::string& proposition);
    
    // Attention and salience
    void update_attention_focus(const std::vector<std::string>& stimuli);
    float calculate_salience(const std::string& stimulus);
    void decay_attention_weights();
    
    // Learning and adaptation
    void analyze_interaction_patterns();
    void adjust_model_parameters();
    void update_knowledge_graph(const std::string& new_knowledge);
};

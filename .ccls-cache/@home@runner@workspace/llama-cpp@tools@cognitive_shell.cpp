
#include <iostream>
#include <string>
#include <sstream>
#include <map>
#include <vector>
#include <fstream>

#include "../include/opencog_llama.h"

using namespace opencog;
using namespace opencog::llama;

class CognitiveShell {
private:
    OpenCogLlama& llama_engine_;
    std::map<std::string, std::function<void(const std::string&)>> commands_;
    bool running_;
    
public:
    explicit CognitiveShell(OpenCogLlama& engine) : llama_engine_(engine), running_(true) {
        initialize_commands();
    }
    
    void initialize_commands() {
        commands_["help"] = [this](const std::string&) { show_help(); };
        commands_["status"] = [this](const std::string&) { show_status(); };
        commands_["query"] = [this](const std::string& args) { handle_query(args); };
        commands_["reason"] = [this](const std::string& args) { handle_reason(args); };
        commands_["learn"] = [this](const std::string& args) { handle_learn(args); };
        commands_["explain"] = [this](const std::string& args) { handle_explain(args); };
        commands_["create"] = [this](const std::string& args) { handle_create(args); };
        commands_["list"] = [this](const std::string& args) { handle_list(args); };
        commands_["save"] = [this](const std::string& args) { handle_save(args); };
        commands_["load"] = [this](const std::string& args) { handle_load(args); };
        commands_["config"] = [this](const std::string& args) { handle_config(args); };
        commands_["analogy"] = [this](const std::string& args) { handle_analogy(args); };
        commands_["causal"] = [this](const std::string& args) { handle_causal(args); };
        commands_["temporal"] = [this](const std::string& args) { handle_temporal(args); };
        commands_["metrics"] = [this](const std::string&) { show_metrics(); };
        commands_["clear"] = [this](const std::string&) { clear_screen(); };
        commands_["exit"] = [this](const std::string&) { running_ = false; };
        commands_["quit"] = [this](const std::string&) { running_ = false; };
    }
    
    void start_interactive_session() {
        std::cout << "=== OpenCog-Llama Cognitive Shell ===" << std::endl;
        std::cout << "Type 'help' for available commands" << std::endl;
        std::cout << "Type 'exit' or 'quit' to exit" << std::endl;
        std::cout << "=====================================" << std::endl;
        
        std::string input;
        while (running_) {
            std::cout << "\ncog> ";
            std::getline(std::cin, input);
            
            if (input.empty()) continue;
            
            execute_command(input);
        }
        
        std::cout << "Goodbye!" << std::endl;
    }
    
    void execute_command(const std::string& command_line) {
        std::istringstream iss(command_line);
        std::string command;
        iss >> command;
        
        std::string args;
        std::getline(iss, args);
        if (!args.empty() && args[0] == ' ') {
            args = args.substr(1); // Remove leading space
        }
        
        auto it = commands_.find(command);
        if (it != commands_.end()) {
            try {
                it->second(args);
            } catch (const std::exception& e) {
                std::cerr << "Error executing command: " << e.what() << std::endl;
            }
        } else {
            std::cout << "Unknown command: " << command << std::endl;
            std::cout << "Type 'help' for available commands" << std::endl;
        }
    }
    
    void show_help() {
        std::cout << "\nAvailable Commands:" << std::endl;
        std::cout << "==================" << std::endl;
        std::cout << "help                    - Show this help message" << std::endl;
        std::cout << "status                  - Show system status" << std::endl;
        std::cout << "query <question>        - Ask a natural language question" << std::endl;
        std::cout << "reason <context>        - Perform reasoning with given context" << std::endl;
        std::cout << "learn <knowledge>       - Learn new knowledge from text" << std::endl;
        std::cout << "explain <concept>       - Explain a concept or relationship" << std::endl;
        std::cout << "create <type> <name>    - Create new concept or relationship" << std::endl;
        std::cout << "list <type>             - List atoms of specified type" << std::endl;
        std::cout << "save <filename>         - Save knowledge base to file" << std::endl;
        std::cout << "load <filename>         - Load knowledge base from file" << std::endl;
        std::cout << "config <param> <value>  - Configure system parameters" << std::endl;
        std::cout << "analogy <A> <B>         - Find analogies between concepts A and B" << std::endl;
        std::cout << "causal <cause> <effect> - Analyze causal relationships" << std::endl;
        std::cout << "temporal <events>       - Analyze temporal sequences" << std::endl;
        std::cout << "metrics                 - Show cognitive performance metrics" << std::endl;
        std::cout << "clear                   - Clear screen" << std::endl;
        std::cout << "exit/quit               - Exit the shell" << std::endl;
    }
    
    void show_status() {
        std::cout << "\n" << llama_engine_.get_system_status() << std::endl;
    }
    
    void handle_query(const std::string& question) {
        if (question.empty()) {
            std::cout << "Usage: query <your question>" << std::endl;
            return;
        }
        
        std::cout << "\nProcessing query: " << question << std::endl;
        std::cout << "Thinking..." << std::endl;
        
        try {
            std::string response = llama_engine_.reason(question);
            std::cout << "\nResponse:\n" << response << std::endl;
        } catch (const std::exception& e) {
            std::cerr << "Query failed: " << e.what() << std::endl;
        }
    }
    
    void handle_reason(const std::string& context) {
        if (context.empty()) {
            std::cout << "Usage: reason <reasoning context>" << std::endl;
            return;
        }
        
        std::cout << "\nPerforming reasoning with context: " << context << std::endl;
        
        try {
            // For simplicity, use empty context vector in this example
            std::vector<Handle> empty_context;
            std::string result = llama_engine_.reason(context, empty_context);
            std::cout << "\nReasoning Result:\n" << result << std::endl;
        } catch (const std::exception& e) {
            std::cerr << "Reasoning failed: " << e.what() << std::endl;
        }
    }
    
    void handle_learn(const std::string& knowledge) {
        if (knowledge.empty()) {
            std::cout << "Usage: learn <new knowledge to learn>" << std::endl;
            return;
        }
        
        std::cout << "\nLearning: " << knowledge << std::endl;
        
        try {
            llama_engine_.learn_from_interaction("Learn this:", knowledge);
            std::cout << "Knowledge learned successfully!" << std::endl;
        } catch (const std::exception& e) {
            std::cerr << "Learning failed: " << e.what() << std::endl;
        }
    }
    
    void handle_explain(const std::string& concept_name) {
        if (concept_name.empty()) {
            std::cout << "Usage: explain <concept name>" << std::endl;
            return;
        }
        
        std::cout << "\nExplaining concept: " << concept_name << std::endl;
        
        try {
            // Create a temporary concept to explain
            Handle concept = llama_engine_.create_concept(concept_name, 
                SimpleTruthValue::createTV(0.8, 0.9));
            std::string explanation = llama_engine_.explain_reasoning(concept);
            std::cout << "\nExplanation:\n" << explanation << std::endl;
        } catch (const std::exception& e) {
            std::cerr << "Explanation failed: " << e.what() << std::endl;
        }
    }
    
    void handle_create(const std::string& args) {
        std::istringstream iss(args);
        std::string type, name;
        iss >> type >> name;
        
        if (type.empty() || name.empty()) {
            std::cout << "Usage: create <concept|relation> <name>" << std::endl;
            return;
        }
        
        try {
            if (type == "concept") {
                Handle concept = llama_engine_.create_concept(name, 
                    SimpleTruthValue::createTV(0.8, 0.9));
                std::cout << "Created concept: " << name << std::endl;
            } else if (type == "relation") {
                std::cout << "Relation creation requires source and target concepts." << std::endl;
                std::cout << "Usage: create relation <relation_name> <source> <target>" << std::endl;
            } else {
                std::cout << "Unknown type: " << type << std::endl;
                std::cout << "Supported types: concept, relation" << std::endl;
            }
        } catch (const std::exception& e) {
            std::cerr << "Creation failed: " << e.what() << std::endl;
        }
    }
    
    void handle_list(const std::string& type) {
        if (type.empty()) {
            std::cout << "Usage: list <concepts|relations|all>" << std::endl;
            return;
        }
        
        std::cout << "\nListing " << type << ":" << std::endl;
        std::cout << "Knowledge base size: " << llama_engine_.get_knowledge_base_size() << " atoms" << std::endl;
        
        // In a real implementation, would iterate through AtomSpace and filter by type
        std::cout << "(Detailed listing not implemented in this example)" << std::endl;
    }
    
    void handle_save(const std::string& filename) {
        if (filename.empty()) {
            std::cout << "Usage: save <filename>" << std::endl;
            return;
        }
        
        std::cout << "\nSaving knowledge base to: " << filename << std::endl;
        
        if (llama_engine_.save_atomspace(filename)) {
            std::cout << "Knowledge base saved successfully!" << std::endl;
        } else {
            std::cerr << "Failed to save knowledge base" << std::endl;
        }
    }
    
    void handle_load(const std::string& filename) {
        if (filename.empty()) {
            std::cout << "Usage: load <filename>" << std::endl;
            return;
        }
        
        std::cout << "\nLoading knowledge base from: " << filename << std::endl;
        
        if (llama_engine_.load_atomspace(filename)) {
            std::cout << "Knowledge base loaded successfully!" << std::endl;
        } else {
            std::cerr << "Failed to load knowledge base" << std::endl;
        }
    }
    
    void handle_config(const std::string& args) {
        std::istringstream iss(args);
        std::string param, value;
        iss >> param >> value;
        
        if (param.empty()) {
            std::cout << "Usage: config <parameter> <value>" << std::endl;
            std::cout << "Available parameters:" << std::endl;
            std::cout << "  reasoning_depth <1-20>" << std::endl;
            std::cout << "  creativity_level <0.0-1.0>" << std::endl;
            std::cout << "  logical_strictness <0.0-1.0>" << std::endl;
            return;
        }
        
        try {
            if (param == "reasoning_depth" && !value.empty()) {
                int depth = std::stoi(value);
                llama_engine_.set_reasoning_depth(depth);
                std::cout << "Reasoning depth set to: " << depth << std::endl;
            } else if (param == "creativity_level" && !value.empty()) {
                double level = std::stod(value);
                llama_engine_.set_creativity_level(level);
                std::cout << "Creativity level set to: " << level << std::endl;
            } else if (param == "logical_strictness" && !value.empty()) {
                double strictness = std::stod(value);
                llama_engine_.set_logical_strictness(strictness);
                std::cout << "Logical strictness set to: " << strictness << std::endl;
            } else {
                std::cout << "Unknown parameter or missing value: " << param << std::endl;
            }
        } catch (const std::exception& e) {
            std::cerr << "Configuration failed: " << e.what() << std::endl;
        }
    }
    
    void handle_analogy(const std::string& args) {
        std::istringstream iss(args);
        std::string concept_a, concept_b;
        iss >> concept_a >> concept_b;
        
        if (concept_a.empty() || concept_b.empty()) {
            std::cout << "Usage: analogy <concept_A> <concept_B>" << std::endl;
            return;
        }
        
        try {
            Handle a = llama_engine_.create_concept(concept_a, SimpleTruthValue::createTV(0.8, 0.9));
            Handle b = llama_engine_.create_concept(concept_b, SimpleTruthValue::createTV(0.8, 0.9));
            
            std::string result = llama_engine_.analogical_reasoning(a, b);
            std::cout << "\nAnalogical Reasoning Result:\n" << result << std::endl;
        } catch (const std::exception& e) {
            std::cerr << "Analogical reasoning failed: " << e.what() << std::endl;
        }
    }
    
    void handle_causal(const std::string& args) {
        std::istringstream iss(args);
        std::string cause, effect;
        iss >> cause >> effect;
        
        if (cause.empty() || effect.empty()) {
            std::cout << "Usage: causal <cause> <effect>" << std::endl;
            return;
        }
        
        try {
            Handle cause_atom = llama_engine_.create_concept(cause, SimpleTruthValue::createTV(0.8, 0.9));
            Handle effect_atom = llama_engine_.create_concept(effect, SimpleTruthValue::createTV(0.8, 0.9));
            
            std::string result = llama_engine_.causal_reasoning(cause_atom, effect_atom);
            std::cout << "\nCausal Reasoning Result:\n" << result << std::endl;
        } catch (const std::exception& e) {
            std::cerr << "Causal reasoning failed: " << e.what() << std::endl;
        }
    }
    
    void handle_temporal(const std::string& args) {
        if (args.empty()) {
            std::cout << "Usage: temporal <event1> <event2> <event3> ..." << std::endl;
            return;
        }
        
        std::istringstream iss(args);
        std::vector<Handle> events;
        std::string event;
        
        while (iss >> event) {
            Handle event_atom = llama_engine_.create_concept(event, SimpleTruthValue::createTV(0.8, 0.9));
            events.push_back(event_atom);
        }
        
        if (events.empty()) {
            std::cout << "No events provided for temporal reasoning" << std::endl;
            return;
        }
        
        try {
            std::string result = llama_engine_.temporal_reasoning(events);
            std::cout << "\nTemporal Reasoning Result:\n" << result << std::endl;
        } catch (const std::exception& e) {
            std::cerr << "Temporal reasoning failed: " << e.what() << std::endl;
        }
    }
    
    void show_metrics() {
        std::cout << "\n=== Cognitive Performance Metrics ===" << std::endl;
        
        try {
            auto metrics = utils::calculate_cognitive_metrics(llama_engine_);
            
            std::cout << "Reasoning Accuracy:     " << (metrics.reasoning_accuracy * 100) << "%" << std::endl;
            std::cout << "Knowledge Coverage:     " << (metrics.knowledge_coverage * 100) << "%" << std::endl;
            std::cout << "Inference Speed:        " << metrics.inference_speed << " inf/sec" << std::endl;
            std::cout << "Active Concepts:        " << metrics.active_concepts << std::endl;
            std::cout << "Learned Patterns:       " << metrics.learned_patterns << std::endl;
            std::cout << "Overall Confidence:     " << (llama_engine_.get_reasoning_confidence() * 100) << "%" << std::endl;
            
        } catch (const std::exception& e) {
            std::cerr << "Failed to calculate metrics: " << e.what() << std::endl;
        }
    }
    
    void clear_screen() {
        #ifdef _WIN32
            system("cls");
        #else
            system("clear");
        #endif
    }
};

int main(int argc, char* argv[]) {
    try {
        // Initialize the OpenCog-Llama system
        OpenCogLlama llama_engine;
        
        std::string model_path = "models/llama-7b.gguf";
        if (argc > 1) {
            model_path = argv[1];
        }
        
        std::cout << "Initializing OpenCog-Llama system..." << std::endl;
        if (!llama_engine.initialize(model_path)) {
            std::cerr << "Failed to initialize system with model: " << model_path << std::endl;
            return 1;
        }
        
        // Start the interactive shell
        CognitiveShell shell(llama_engine);
        
        // Check if we should execute a script file
        if (argc > 2) {
            std::string script_file = argv[2];
            std::cout << "Executing script: " << script_file << std::endl;
            
            std::ifstream file(script_file);
            if (file.is_open()) {
                std::string line;
                while (std::getline(file, line)) {
                    if (!line.empty() && line[0] != '#') { // Skip comments
                        std::cout << "cog> " << line << std::endl;
                        shell.execute_command(line);
                    }
                }
                file.close();
            } else {
                std::cerr << "Could not open script file: " << script_file << std::endl;
            }
        }
        
        // Start interactive session
        shell.start_interactive_session();
        
    } catch (const std::exception& e) {
        std::cerr << "Error: " << e.what() << std::endl;
        return 1;
    }
    
    return 0;
}

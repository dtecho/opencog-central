
#pragma once

#include <string>
#include <thread>
#include <memory>

class KogServerBridge {
public:
    KogServerBridge();
    ~KogServerBridge();
    
    void initialize(const std::string& model_path, int port, int context_size, int gpu_layers);
    void start_server();
    
    std::string generate_text(const std::string& prompt, int max_tokens = 256);
    void process_atomspace_query(const std::string& query);
    
private:
    std::string model_path;
    int port;
    int context_size;
    int gpu_layers;
    
    std::thread server_thread;
    
    void run_server_loop();
};

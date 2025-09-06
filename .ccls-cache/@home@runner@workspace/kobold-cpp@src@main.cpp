
#include <iostream>
#include <string>
#include <memory>
#include "kogserver_bridge.h"

int main(int argc, char** argv) {
    std::cout << "KoboldCpp OpenCog Integration Server" << std::endl;
    
    KogServerBridge bridge;
    
    // Default configuration
    std::string model_path;
    int port = 5001;
    int context_size = 2048;
    int gpu_layers = 0;
    
    // Parse command line arguments
    for (int i = 1; i < argc; i++) {
        std::string arg = argv[i];
        if (arg == "--model" && i + 1 < argc) {
            model_path = argv[++i];
        } else if (arg == "--port" && i + 1 < argc) {
            port = std::stoi(argv[++i]);
        } else if (arg == "--context" && i + 1 < argc) {
            context_size = std::stoi(argv[++i]);
        } else if (arg == "--gpu-layers" && i + 1 < argc) {
            gpu_layers = std::stoi(argv[++i]);
        } else if (arg == "--help") {
            std::cout << "Usage: " << argv[0] << " [options]\n"
                      << "Options:\n"
                      << "  --model PATH      Path to GGUF model file\n"
                      << "  --port PORT       Server port (default: 5001)\n"
                      << "  --context SIZE    Context size (default: 2048)\n"
                      << "  --gpu-layers N    Number of GPU layers (default: 0)\n"
                      << "  --help            Show this help message\n";
            return 0;
        }
    }
    
    if (model_path.empty()) {
        std::cerr << "Error: Model path is required. Use --model PATH\n";
        return 1;
    }
    
    try {
        bridge.initialize(model_path, port, context_size, gpu_layers);
        bridge.start_server();
    } catch (const std::exception& e) {
        std::cerr << "Error: " << e.what() << std::endl;
        return 1;
    }
    
    return 0;
}

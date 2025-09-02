
#include "rwkv_wrapper.h"
#include "text_generator.h"
#include "streaming_generator.h"
#include "tokenizer.h"
#include "config.h"
#include <iostream>
#include <memory>
#include <string>
#include <vector>

class ChatSession {
private:
    std::shared_ptr<rwkv_cpp::RWKVModel> model_;
    std::shared_ptr<rwkv_cpp::Tokenizer> tokenizer_;
    std::shared_ptr<rwkv_cpp::StreamingGenerator> generator_;
    std::vector<float> state_;
    std::string chat_template_;
    
public:
    ChatSession(const std::string& model_path, const std::string& tokenizer_path) {
        model_ = std::make_shared<rwkv_cpp::RWKVModel>(model_path, 4, 0);
        if (!model_->is_loaded()) {
            throw std::runtime_error("Failed to load model");
        }
        
        tokenizer_ = std::make_shared<rwkv_cpp::Tokenizer>(tokenizer_path);
        generator_ = std::make_shared<rwkv_cpp::StreamingGenerator>(model_, tokenizer_);
        
        state_.resize(model_->get_state_size(), 0.0f);
        chat_template_ = "User: {user}\n\nAssistant: {assistant}\n\n";
    }
    
    void chat_loop() {
        std::cout << "RWKV Chat Interface (type 'quit' to exit)\n";
        std::cout << "=========================================\n\n";
        
        std::string input;
        while (true) {
            std::cout << "You: ";
            std::getline(std::cin, input);
            
            if (input == "quit" || input == "exit") {
                break;
            }
            
            if (input.empty()) {
                continue;
            }
            
            std::cout << "Assistant: ";
            
            generator_->generate_stream(
                input,
                [](const std::string& token, bool is_final) {
                    std::cout << token;
                    std::cout.flush();
                    if (is_final) {
                        std::cout << "\n\n";
                    }
                },
                200,  // max tokens
                0.7f, // temperature
                0.9f  // top_p
            );
        }
    }
};

int main(int argc, char* argv[]) {
    try {
        std::string model_path = argc > 1 ? argv[1] : "models/rwkv-4-pile-169m-q5_1.bin";
        std::string tokenizer_path = argc > 2 ? argv[2] : "models/20B_tokenizer.json";
        
        ChatSession session(model_path, tokenizer_path);
        session.chat_loop();
        
    } catch (const std::exception& e) {
        std::cerr << "Error: " << e.what() << std::endl;
        return 1;
    }
    
    return 0;
}

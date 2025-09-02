
#pragma once

#include "rwkv_wrapper.h"
#include "tokenizer.h"
#include <functional>
#include <memory>
#include <string>

namespace rwkv_cpp {

class StreamingGenerator {
public:
    using TokenCallback = std::function<void(const std::string&, bool)>;
    
    StreamingGenerator(std::shared_ptr<RWKVModel> model, 
                      std::shared_ptr<Tokenizer> tokenizer);
    
    void generate_stream(const std::string& prompt,
                        TokenCallback callback,
                        uint32_t max_tokens = 100,
                        float temperature = 0.8f,
                        float top_p = 0.9f);
    
    void stop_generation();

private:
    std::shared_ptr<RWKVModel> model_;
    std::shared_ptr<Tokenizer> tokenizer_;
    bool stop_requested_;
};

} // namespace rwkv_cpp

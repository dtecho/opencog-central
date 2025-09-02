
#pragma once

#include <string>
#include <vector>
#include <unordered_map>
#include <memory>

namespace rwkv_cpp {

class Tokenizer {
public:
    explicit Tokenizer(const std::string& vocab_path);
    ~Tokenizer() = default;

    std::vector<uint32_t> encode(const std::string& text) const;
    std::string decode(const std::vector<uint32_t>& tokens) const;
    std::string decode_single(uint32_t token) const;
    
    size_t vocab_size() const { return vocab_size_; }
    uint32_t bos_token() const { return bos_token_; }
    uint32_t eos_token() const { return eos_token_; }
    uint32_t pad_token() const { return pad_token_; }

private:
    void load_vocab(const std::string& vocab_path);
    
    std::unordered_map<std::string, uint32_t> str_to_token_;
    std::unordered_map<uint32_t, std::string> token_to_str_;
    size_t vocab_size_;
    uint32_t bos_token_;
    uint32_t eos_token_;
    uint32_t pad_token_;
};

} // namespace rwkv_cpp

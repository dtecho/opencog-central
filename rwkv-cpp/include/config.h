
#pragma once

#include <string>
#include <unordered_map>
#include <variant>

namespace rwkv_cpp {

using ConfigValue = std::variant<bool, int, float, std::string>;

class Config {
public:
    static Config& instance();
    
    void load_from_file(const std::string& config_path);
    void save_to_file(const std::string& config_path) const;
    
    template<typename T>
    T get(const std::string& key, const T& default_value = T{}) const;
    
    template<typename T>
    void set(const std::string& key, const T& value);
    
    bool has(const std::string& key) const;
    void remove(const std::string& key);

private:
    Config() = default;
    std::unordered_map<std::string, ConfigValue> values_;
};

// Convenience macros
#define RWKV_CONFIG Config::instance()
#define RWKV_GET_CONFIG(key, default_val) RWKV_CONFIG.get(key, default_val)
#define RWKV_SET_CONFIG(key, val) RWKV_CONFIG.set(key, val)

} // namespace rwkv_cpp

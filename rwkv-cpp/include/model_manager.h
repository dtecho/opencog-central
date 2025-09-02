
#pragma once

#include <string>
#include <vector>
#include <map>

namespace rwkv_cpp {

struct ModelInfo {
    std::string name;
    std::string url;
    std::string description;
    size_t size_bytes;
    std::string hash;
};

class ModelManager {
public:
    ModelManager(const std::string& models_dir = "./models");
    
    bool download_model(const std::string& model_name);
    bool is_model_available(const std::string& model_name) const;
    std::string get_model_path(const std::string& model_name) const;
    std::vector<ModelInfo> list_available_models() const;
    std::vector<std::string> list_downloaded_models() const;
    
    void add_model_source(const std::string& name, const ModelInfo& info);

private:
    std::string models_dir_;
    std::map<std::string, ModelInfo> available_models_;
    
    bool verify_model_hash(const std::string& file_path, const std::string& expected_hash) const;
    bool download_file(const std::string& url, const std::string& output_path) const;
};

} // namespace rwkv_cpp

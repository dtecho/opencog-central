
#pragma once

#include "rwkv_wrapper.h"
#include "atomspace_bridge.h"
#include <string>
#include <vector>
#include <map>

namespace rwkv {
namespace cognitive {

enum class CognitiveMode {
    REASONING,
    LEARNING,
    ATTENTION_ALLOCATION,
    PATTERN_MINING,
    NATURAL_LANGUAGE
};

class CognitiveProcessor {
public:
    CognitiveProcessor(std::shared_ptr<RWKVModel> model);
    
    // PLN (Probabilistic Logic Networks) integration
    std::string performLogicalInference(const std::string& premises, 
                                      const std::string& query);
    
    // ECAN (Economic Attention Network) integration  
    std::vector<std::string> allocateAttention(const std::vector<std::string>& stimuli,
                                              double attention_budget = 1.0);
    
    // Pattern mining with semantic understanding
    std::vector<std::string> mineSemanticPatterns(const std::vector<std::string>& corpus,
                                                 int min_support = 2);
    
    // Ghost chatbot integration
    std::string processGhostDialog(const std::string& input, 
                                  const std::string& context = "");
    
    // OpenPsi goal-oriented behavior
    std::string generateGoalDirectedResponse(const std::string& goal,
                                           const std::string& current_state);

private:
    std::shared_ptr<RWKVModel> model_;
    std::unique_ptr<opencog::AtomSpaceBridge> atomspace_bridge_;
    std::map<CognitiveMode, double> mode_weights_;
};

} // namespace cognitive
} // namespace rwkv


#pragma once

#include "rwkv_wrapper.h"
#include <string>
#include <vector>
#include <chrono>

namespace rwkv {
namespace memory {

// Episodic memory for temporal sequences
class EpisodicMemory {
public:
    struct Episode {
        std::string content;
        std::chrono::system_clock::time_point timestamp;
        double salience;
        std::vector<float> embedding;
    };
    
    void storeEpisode(const std::string& content, double salience = 1.0);
    std::vector<Episode> retrieveEpisodes(const std::string& query, int max_results = 10);
    void updateSalience(const std::string& episode_id, double new_salience);
};

// Procedural memory for learned behaviors
class ProceduralMemory {
public:
    struct Procedure {
        std::string name;
        std::string condition;
        std::string action;
        double success_rate;
    };
    
    void learnProcedure(const std::string& name, const std::string& condition,
                       const std::string& action);
    std::vector<Procedure> matchProcedures(const std::string& situation);
};

// Declarative memory for facts and concepts
class DeclarativeMemory {
public:
    void storeFact(const std::string& fact, double confidence = 1.0);
    std::vector<std::string> queryFacts(const std::string& query);
    double getConfidence(const std::string& fact);
};

} // namespace memory
} // namespace rwkv

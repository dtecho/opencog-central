
#include <gtest/gtest.h>
#include "cognitive_processor.h"
#include "atomspace_bridge.h"
#include "memory_systems.h"

class OpenCogIntegrationTest : public ::testing::Test {
protected:
    void SetUp() override {
        model_ = std::make_shared<rwkv::RWKVModel>();
        // Use mock model for testing
        processor_ = std::make_unique<rwkv::cognitive::CognitiveProcessor>(model_);
    }
    
    std::shared_ptr<rwkv::RWKVModel> model_;
    std::unique_ptr<rwkv::cognitive::CognitiveProcessor> processor_;
};

TEST_F(OpenCogIntegrationTest, PLNInferenceBasic) {
    std::string premises = "All birds can fly. Tweety is a bird.";
    std::string query = "Can Tweety fly?";
    std::string result = processor_->performLogicalInference(premises, query);
    
    EXPECT_FALSE(result.empty());
    EXPECT_NE(result.find("yes"), std::string::npos);
}

TEST_F(OpenCogIntegrationTest, AttentionAllocation) {
    std::vector<std::string> stimuli = {
        "fire alarm ringing",
        "gentle music playing",
        "interesting book"
    };
    
    auto results = processor_->allocateAttention(stimuli, 1.0);
    EXPECT_EQ(results.size(), 3);
    EXPECT_EQ(results[0], "fire alarm ringing"); // Should have highest attention
}

TEST_F(OpenCogIntegrationTest, SemanticPatternMining) {
    std::vector<std::string> corpus = {
        "cats like fish",
        "dogs like bones", 
        "birds like seeds"
    };
    
    auto patterns = processor_->mineSemanticPatterns(corpus, 1);
    EXPECT_FALSE(patterns.empty());
    
    // Should find the pattern: "X like Y"
    bool found_pattern = false;
    for (const auto& pattern : patterns) {
        if (pattern.find("like") != std::string::npos) {
            found_pattern = true;
            break;
        }
    }
    EXPECT_TRUE(found_pattern);
}

TEST_F(OpenCogIntegrationTest, EpisodicMemory) {
    rwkv::memory::EpisodicMemory episodic;
    
    episodic.storeEpisode("Met John at the coffee shop", 0.8);
    episodic.storeEpisode("Discussed AI research with Sarah", 0.9);
    episodic.storeEpisode("Had lunch at the university", 0.6);
    
    auto episodes = episodic.retrieveEpisodes("research discussion", 2);
    EXPECT_GE(episodes.size(), 1);
    EXPECT_NE(episodes[0].content.find("Sarah"), std::string::npos);
}

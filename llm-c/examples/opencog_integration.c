
#include "../include/llm_core.h"
#include <stdio.h>
#include <stdlib.h>
#include <string.h>

int main() {
    printf("LLM.C OpenCog Integration Demo\n");
    printf("==============================\n\n");
    
    // 1. Initialize AtomSpace
    printf("1. Creating AtomSpace...\n");
    AtomSpace* atomspace = create_atomspace(1000);
    
    // Add some concepts
    add_concept_node(atomspace, "human", 0.9f, 0.8f);
    add_concept_node(atomspace, "mortal", 0.8f, 0.9f);
    add_concept_node(atomspace, "socrates", 0.95f, 0.95f);
    add_predicate_node(atomspace, "is_a", 0.9f, 0.9f);
    
    printf("   Added concepts: human, mortal, socrates\n");
    printf("   Added predicate: is_a\n\n");
    
    // 2. Initialize ECAN attention system
    printf("2. Creating ECAN Attention Bank...\n");
    AttentionBank* attention = create_attention_bank(1000);
    
    // Simulate attention updates
    update_attention(attention, "socrates", 0.8f);
    update_attention(attention, "human", 0.6f);
    update_attention(attention, "mortal", 0.4f);
    
    printf("   Updated attention values for concepts\n");
    manage_attention_economy(attention);
    printf("\n");
    
    // 3. Initialize Scheme environment
    printf("3. Creating Scheme Environment...\n");
    SchemeEnvironment* scheme = create_scheme_env(100);
    
    // Evaluate some Scheme expressions
    char* result1 = eval_scheme(scheme, "(+ 5 3)");
    char* result2 = eval_scheme(scheme, "(cog-new-node ConceptNode \"test\")");
    
    printf("   Scheme result 1: %s\n", result1);
    printf("   Scheme result 2: %s\n", result2);
    printf("\n");
    
    // 4. Initialize pattern miner
    printf("4. Creating Pattern Miner...\n");
    PatternMiner* miner = create_pattern_miner(500, 2, 0.1f);
    
    // Sample corpus for pattern mining
    char* corpus[] = {
        "socrates is human",
        "humans are mortal", 
        "socrates is mortal",
        "plato is human",
        "aristotle is human",
        "humans can think",
        "thinking is cognitive"
    };
    int corpus_size = 7;
    
    mine_patterns(miner, corpus, corpus_size);
    printf("   Completed pattern mining on sample corpus\n\n");
    
    // 5. Initialize MOSES evolution
    printf("5. Creating MOSES Population...\n");
    Population* population = create_population(50);
    
    // Configure MOSES parameters
    struct {
        int max_generations;
        float mutation_rate;
        float crossover_rate;
        int population_size;
        int elitism_count;
    } moses_config = {
        .max_generations = 20,
        .mutation_rate = 0.1f,
        .crossover_rate = 0.7f,
        .population_size = 30,
        .elitism_count = 5
    };
    
    // Sample training data
    float* training_data[4];
    for (int i = 0; i < 4; i++) {
        training_data[i] = malloc(3 * sizeof(float));
    }
    // XOR training data
    float xor_data[4][3] = {{0,0,0}, {0,1,1}, {1,0,1}, {1,1,0}};
    for (int i = 0; i < 4; i++) {
        memcpy(training_data[i], xor_data[i], 3 * sizeof(float));
    }
    
    run_moses_evolution(population, moses_config, training_data, 4);
    printf("   Completed MOSES evolution\n\n");
    
    // 6. Demonstrate cognitive integration
    printf("6. Cognitive Integration Demo...\n");
    printf("   AtomSpace contains knowledge representation\n");
    printf("   ECAN manages attention allocation\n");
    printf("   PLN provides probabilistic reasoning\n");
    printf("   MOSES evolves optimal solutions\n");
    printf("   Pattern mining discovers structures\n");
    printf("   Scheme provides dynamic scripting\n\n");
    
    printf("7. Integration Success!\n");
    printf("   This demonstrates how LLM.C can integrate with OpenCog\n");
    printf("   cognitive architecture components for AGI applications.\n\n");
    
    // Cleanup
    cleanup_atomspace(atomspace);
    cleanup_scheme_env(scheme);
    cleanup_pattern_miner(miner);
    cleanup_population(population);
    
    for (int i = 0; i < 4; i++) {
        free(training_data[i]);
    }
    
    printf("Demo completed successfully!\n");
    return 0;
}

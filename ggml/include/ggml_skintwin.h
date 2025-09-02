
#ifndef GGML_SKINTWIN_H
#define GGML_SKINTWIN_H

#include "ggml.h"
#include <stdint.h>
#include <stdbool.h>

#ifdef __cplusplus
extern "C" {
#endif

// SkinTwin-ASI specific structures
struct ggml_skintwin_context {
    struct ggml_context * ggml_ctx;
    
    // Multiscale model components
    struct ggml_tensor * molecular_state;
    struct ggml_tensor * cellular_state;
    struct ggml_tensor * tissue_state;
    struct ggml_tensor * organ_state;
    
    // Simulation parameters
    float dt;                    // Time step
    int num_molecules;          // Number of molecular components
    int num_cells;              // Number of cellular components
    int num_tissue_layers;      // Number of tissue layers
    
    // Model metadata
    bool initialized;
    size_t memory_size;
};

struct ggml_skintwin_molecule {
    char name[64];
    char formula[32];
    float molecular_weight;
    float concentration;
    float diffusion_coefficient;
    struct ggml_tensor * properties;
};

struct ggml_skintwin_cell {
    char type[32];
    int id;
    float x, y, z;              // Position
    float volume;
    float membrane_permeability;
    struct ggml_tensor * state_vector;
};

struct ggml_skintwin_tissue {
    char name[64];
    int layer_id;
    float thickness;
    float porosity;
    int num_cells;
    int * cell_ids;
    struct ggml_tensor * mechanical_properties;
};

// Core API functions
struct ggml_skintwin_context * ggml_skintwin_init(size_t memory_size);
void ggml_skintwin_free(struct ggml_skintwin_context * ctx);

// Molecular modeling
int ggml_skintwin_add_molecule(
    struct ggml_skintwin_context * ctx,
    const char * name,
    const char * formula,
    float molecular_weight,
    float initial_concentration
);

struct ggml_tensor * ggml_skintwin_simulate_diffusion(
    struct ggml_skintwin_context * ctx,
    int molecule_id,
    float time_duration,
    int num_steps
);

// Cellular modeling
int ggml_skintwin_add_cell(
    struct ggml_skintwin_context * ctx,
    const char * type,
    float x, float y, float z,
    float volume
);

struct ggml_tensor * ggml_skintwin_simulate_cellular_dynamics(
    struct ggml_skintwin_context * ctx,
    int cell_id,
    float time_duration,
    int num_steps
);

// Tissue modeling
int ggml_skintwin_add_tissue_layer(
    struct ggml_skintwin_context * ctx,
    const char * name,
    float thickness,
    float porosity
);

struct ggml_tensor * ggml_skintwin_simulate_tissue_mechanics(
    struct ggml_skintwin_context * ctx,
    int tissue_id,
    float applied_stress,
    float time_duration
);

// Multiscale integration
struct ggml_tensor * ggml_skintwin_couple_molecular_cellular(
    struct ggml_skintwin_context * ctx,
    int molecule_id,
    int cell_id,
    float coupling_strength
);

struct ggml_tensor * ggml_skintwin_couple_cellular_tissue(
    struct ggml_skintwin_context * ctx,
    int cell_id,
    int tissue_id,
    float coupling_strength
);

// Advanced simulations
struct ggml_tensor * ggml_skintwin_simulate_permeation(
    struct ggml_skintwin_context * ctx,
    int molecule_id,
    float barrier_thickness,
    float partition_coefficient,
    float time_duration
);

struct ggml_tensor * ggml_skintwin_simulate_aging(
    struct ggml_skintwin_context * ctx,
    float aging_factor,
    float time_duration
);

struct ggml_tensor * ggml_skintwin_simulate_wound_healing(
    struct ggml_skintwin_context * ctx,
    float wound_size,
    float healing_rate,
    float time_duration
);

// Analysis and export
void ggml_skintwin_export_state(
    struct ggml_skintwin_context * ctx,
    const char * filename
);

void ggml_skintwin_print_summary(struct ggml_skintwin_context * ctx);

// Utility functions
bool ggml_skintwin_validate_context(struct ggml_skintwin_context * ctx);
size_t ggml_skintwin_get_memory_usage(struct ggml_skintwin_context * ctx);

#ifdef __cplusplus
}
#endif

#endif // GGML_SKINTWIN_H

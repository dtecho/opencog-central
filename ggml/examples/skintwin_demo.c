
#include "ggml_skintwin.h"
#include <stdio.h>
#include <stdlib.h>
#include <math.h>

static void demo_molecular_modeling(struct ggml_skintwin_context * ctx);
static void demo_cellular_modeling(struct ggml_skintwin_context * ctx);
static void demo_tissue_modeling(struct ggml_skintwin_context * ctx);
static void demo_multiscale_coupling(struct ggml_skintwin_context * ctx);
static void demo_advanced_simulations(struct ggml_skintwin_context * ctx);

int main() {
    printf("=== SkinTwin-ASI GGML Comprehensive Demo ===\n\n");
    
    // Initialize SkinTwin context with 16MB memory
    size_t memory_size = 16 * 1024 * 1024;
    struct ggml_skintwin_context * ctx = ggml_skintwin_init(memory_size);
    
    if (!ctx) {
        printf("Failed to initialize SkinTwin context\n");
        return 1;
    }
    
    // Validate context
    if (!ggml_skintwin_validate_context(ctx)) {
        printf("Context validation failed\n");
        ggml_skintwin_free(ctx);
        return 1;
    }
    
    // Print initial system summary
    ggml_skintwin_print_summary(ctx);
    
    // Run comprehensive demonstrations
    demo_molecular_modeling(ctx);
    demo_cellular_modeling(ctx);
    demo_tissue_modeling(ctx);
    demo_multiscale_coupling(ctx);
    demo_advanced_simulations(ctx);
    
    // Final system summary
    printf("\n=== Final System State ===\n");
    ggml_skintwin_print_summary(ctx);
    
    // Export final state
    ggml_skintwin_export_state(ctx, "skintwin_final_state.txt");
    
    // Cleanup
    ggml_skintwin_free(ctx);
    
    printf("✓ SkinTwin-ASI demo completed successfully!\n");
    return 0;
}

static void demo_molecular_modeling(struct ggml_skintwin_context * ctx) {
    printf("=== Molecular Modeling Demo ===\n");
    
    // Add key skin molecules
    int water_id = ggml_skintwin_add_molecule(ctx, "water", "H2O", 18.015f, 55.6f);
    int ceramide_id = ggml_skintwin_add_molecule(ctx, "ceramide_ns", "C34H67NO4", 537.9f, 0.001f);
    int cholesterol_id = ggml_skintwin_add_molecule(ctx, "cholesterol", "C27H46O", 386.7f, 0.002f);
    int hyaluronic_id = ggml_skintwin_add_molecule(ctx, "hyaluronic_acid", "C14H21NO11", 379.3f, 0.0005f);
    int collagen_id = ggml_skintwin_add_molecule(ctx, "collagen_fragment", "C4H7NO4", 133.1f, 0.01f);
    int urea_id = ggml_skintwin_add_molecule(ctx, "urea", "CH4N2O", 60.06f, 0.1f);
    
    // Simulate diffusion for water
    if (water_id >= 0) {
        struct ggml_tensor * water_diffusion = ggml_skintwin_simulate_diffusion(
            ctx, water_id, 1.0f, 50
        );
        
        if (water_diffusion) {
            printf("  Water diffusion tensor: [%lld x %lld]\n",
                   water_diffusion->ne[0], water_diffusion->ne[1]);
        }
    }
    
    // Simulate permeation for urea (common permeation marker)
    if (urea_id >= 0) {
        struct ggml_tensor * urea_permeation = ggml_skintwin_simulate_permeation(
            ctx, urea_id, 0.02f, 0.5f, 3600.0f  // 20μm barrier, 1 hour
        );
        
        if (urea_permeation) {
            printf("  Urea permeation tensor: [%lld x %lld]\n",
                   urea_permeation->ne[0], urea_permeation->ne[1]);
        }
    }
    
    printf("✓ Molecular modeling demo completed\n\n");
}

static void demo_cellular_modeling(struct ggml_skintwin_context * ctx) {
    printf("=== Cellular Modeling Demo ===\n");
    
    // Add different skin cell types
    int keratinocyte_ids[20];
    int fibroblast_ids[10];
    int melanocyte_ids[5];
    
    // Create keratinocytes (epidermis)
    for (int i = 0; i < 20; i++) {
        float x = (float)(i % 5) * 0.01f;
        float y = (float)(i / 5) * 0.01f;
        float z = 0.0f;  // Surface layer
        
        keratinocyte_ids[i] = ggml_skintwin_add_cell(
            ctx, "keratinocyte", x, y, z, 1000.0f  // 1000 μm³
        );
    }
    
    // Create fibroblasts (dermis)
    for (int i = 0; i < 10; i++) {
        float x = (float)(i % 3) * 0.02f;
        float y = (float)(i / 3) * 0.02f;
        float z = -0.1f;  // Dermal layer
        
        fibroblast_ids[i] = ggml_skintwin_add_cell(
            ctx, "fibroblast", x, y, z, 2000.0f  // 2000 μm³
        );
    }
    
    // Create melanocytes
    for (int i = 0; i < 5; i++) {
        float x = (float)i * 0.02f;
        float y = 0.0f;
        float z = -0.05f;  // Basal layer
        
        melanocyte_ids[i] = ggml_skintwin_add_cell(
            ctx, "melanocyte", x, y, z, 800.0f  // 800 μm³
        );
    }
    
    // Simulate dynamics for a representative keratinocyte
    if (keratinocyte_ids[0] >= 0) {
        struct ggml_tensor * cell_dynamics = ggml_skintwin_simulate_cellular_dynamics(
            ctx, keratinocyte_ids[0], 24.0f, 100  // 24 hours, 100 steps
        );
        
        if (cell_dynamics) {
            printf("  Keratinocyte dynamics tensor: [%lld x %lld x %lld]\n",
                   cell_dynamics->ne[0], cell_dynamics->ne[1], cell_dynamics->ne[2]);
        }
    }
    
    printf("✓ Cellular modeling demo completed\n\n");
}

static void demo_tissue_modeling(struct ggml_skintwin_context * ctx) {
    printf("=== Tissue Modeling Demo ===\n");
    
    // Add skin tissue layers (from surface to deep)
    int stratum_corneum = ggml_skintwin_add_tissue_layer(
        ctx, "stratum_corneum", 0.00001f, 0.1f  // 10μm, low porosity
    );
    
    int stratum_granulosum = ggml_skintwin_add_tissue_layer(
        ctx, "stratum_granulosum", 0.000005f, 0.3f  // 5μm, moderate porosity
    );
    
    int stratum_spinosum = ggml_skintwin_add_tissue_layer(
        ctx, "stratum_spinosum", 0.00005f, 0.4f  // 50μm, moderate porosity
    );
    
    int stratum_basale = ggml_skintwin_add_tissue_layer(
        ctx, "stratum_basale", 0.00001f, 0.5f  // 10μm, high porosity
    );
    
    int papillary_dermis = ggml_skintwin_add_tissue_layer(
        ctx, "papillary_dermis", 0.0002f, 0.6f  // 200μm, high porosity
    );
    
    int reticular_dermis = ggml_skintwin_add_tissue_layer(
        ctx, "reticular_dermis", 0.003f, 0.4f  // 3mm, moderate porosity
    );
    
    // Simulate mechanical response of stratum corneum
    if (stratum_corneum >= 0) {
        struct ggml_tensor * mechanics = ggml_skintwin_simulate_tissue_mechanics(
            ctx, stratum_corneum, 0.1f, 10.0f  // 0.1 MPa stress, 10 seconds
        );
        
        if (mechanics) {
            printf("  Stratum corneum mechanics tensor: [%lld x %lld]\n",
                   mechanics->ne[0], mechanics->ne[1]);
        }
    }
    
    // Simulate mechanical response of dermis
    if (reticular_dermis >= 0) {
        struct ggml_tensor * dermis_mechanics = ggml_skintwin_simulate_tissue_mechanics(
            ctx, reticular_dermis, 0.05f, 20.0f  // 0.05 MPa stress, 20 seconds
        );
        
        if (dermis_mechanics) {
            printf("  Reticular dermis mechanics tensor: [%lld x %lld]\n",
                   dermis_mechanics->ne[0], dermis_mechanics->ne[1]);
        }
    }
    
    printf("✓ Tissue modeling demo completed\n\n");
}

static void demo_multiscale_coupling(struct ggml_skintwin_context * ctx) {
    printf("=== Multiscale Coupling Demo ===\n");
    
    // Demonstrate molecular-cellular coupling
    if (ctx->num_molecules > 0 && ctx->num_cells > 0) {
        struct ggml_tensor * mol_cell_coupling = ggml_skintwin_couple_molecular_cellular(
            ctx, 0, 0, 0.8f  // Strong coupling
        );
        
        if (mol_cell_coupling) {
            printf("  Molecular-cellular coupling tensor: [%lld]\n",
                   mol_cell_coupling->ne[0]);
        }
    }
    
    // Demonstrate cellular-tissue coupling
    if (ctx->num_cells > 0 && ctx->num_tissue_layers > 0) {
        struct ggml_tensor * cell_tissue_coupling = ggml_skintwin_couple_cellular_tissue(
            ctx, 0, 0, 0.6f  // Moderate coupling
        );
        
        if (cell_tissue_coupling) {
            printf("  Cellular-tissue coupling established\n");
        }
    }
    
    printf("✓ Multiscale coupling demo completed\n\n");
}

static void demo_advanced_simulations(struct ggml_skintwin_context * ctx) {
    printf("=== Advanced Simulations Demo ===\n");
    
    // Aging simulation
    struct ggml_tensor * aging_results = ggml_skintwin_simulate_aging(
        ctx, 0.001f, 365.0f * 24.0f * 3600.0f  // 1 year of aging
    );
    
    if (aging_results) {
        printf("  Aging simulation tensor: [%lld x %lld]\n",
               aging_results->ne[0], aging_results->ne[1]);
        
        // Sample some aging data
        float * aging_data = (float *)aging_results->data;
        printf("  Year-end collagen integrity: %.3f\n", aging_data[99 * 32 + 0]);
        printf("  Year-end elastin integrity: %.3f\n", aging_data[99 * 32 + 1]);
        printf("  Year-end oxidative stress: %.3f\n", aging_data[99 * 32 + 4]);
    }
    
    // Wound healing simulation
    struct ggml_tensor * healing_results = ggml_skintwin_simulate_wound_healing(
        ctx, 0.005f, 0.1f, 7.0f * 24.0f * 3600.0f  // 5mm wound, 1 week
    );
    
    if (healing_results) {
        printf("  Wound healing simulation completed\n");
    }
    
    printf("✓ Advanced simulations demo completed\n\n");
}

// Placeholder for wound healing implementation
struct ggml_tensor * ggml_skintwin_simulate_wound_healing(
    struct ggml_skintwin_context * ctx,
    float wound_size,
    float healing_rate,
    float time_duration
) {
    if (!ctx || !ctx->initialized) {
        return NULL;
    }
    
    printf("Simulating wound healing (size: %.3f, rate: %.3f, duration: %.1f)...\n",
           wound_size, healing_rate, time_duration);
    
    // Create healing simulation tensor
    struct ggml_tensor * result = ggml_new_tensor_2d(ctx->ggml_ctx, GGML_TYPE_F32, 100, 16);
    float * result_data = (float *)result->data;
    
    for (int t = 0; t < 100; t++) {
        float time = (float)t / 100.0f * time_duration;
        float healing_progress = 1.0f - exp(-healing_rate * time);
        
        result_data[t * 16 + 0] = wound_size * (1.0f - healing_progress);     // Wound size
        result_data[t * 16 + 1] = healing_progress;                          // Healing fraction
        result_data[t * 16 + 2] = healing_progress * 2.0f;                   // Cell proliferation
        result_data[t * 16 + 3] = sin(time * 0.1f) * 0.2f + 0.3f;          // Inflammation
        result_data[t * 16 + 4] = healing_progress * 1.5f;                   // Angiogenesis
        result_data[t * 16 + 5] = healing_progress * healing_progress;       // Remodeling
        
        // Fill remaining parameters
        for (int i = 6; i < 16; i++) {
            result_data[t * 16 + i] = healing_progress * (float)i * 0.1f;
        }
    }
    
    printf("✓ Wound healing simulation completed\n");
    
    return result;
}

// Placeholder for cellular-tissue coupling
struct ggml_tensor * ggml_skintwin_couple_cellular_tissue(
    struct ggml_skintwin_context * ctx,
    int cell_id,
    int tissue_id,
    float coupling_strength
) {
    if (!ctx || !ctx->initialized ||
        cell_id < 0 || cell_id >= ctx->num_cells ||
        tissue_id < 0 || tissue_id >= ctx->num_tissue_layers) {
        return NULL;
    }
    
    printf("Coupling cell %d with tissue %d (strength: %.3f)...\n",
           cell_id, tissue_id, coupling_strength);
    
    // Create coupling tensor
    struct ggml_tensor * coupling = ggml_new_tensor_1d(ctx->ggml_ctx, GGML_TYPE_F32, 20);
    float * coupling_data = (float *)coupling->data;
    
    // Simple coupling model
    for (int i = 0; i < 20; i++) {
        coupling_data[i] = coupling_strength * (1.0f + sin((float)i * 0.3f) * 0.1f);
    }
    
    printf("✓ Cellular-tissue coupling established\n");
    
    return coupling;
}

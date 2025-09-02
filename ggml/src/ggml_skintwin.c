
#include "ggml_skintwin.h"
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <math.h>
#include <assert.h>

// Internal helper functions
static struct ggml_tensor * create_molecular_tensor(
    struct ggml_context * ctx, 
    int num_molecules, 
    int properties_dim
);

static struct ggml_tensor * create_cellular_tensor(
    struct ggml_context * ctx,
    int num_cells,
    int state_dim
);

static struct ggml_tensor * create_tissue_tensor(
    struct ggml_context * ctx,
    int num_layers,
    int mechanical_properties_dim
);

// Core implementation
struct ggml_skintwin_context * ggml_skintwin_init(size_t memory_size) {
    struct ggml_skintwin_context * ctx = malloc(sizeof(struct ggml_skintwin_context));
    if (!ctx) {
        return NULL;
    }
    
    // Initialize GGML context
    struct ggml_init_params params = {
        .mem_size = memory_size,
        .mem_buffer = NULL,
        .no_alloc = false,
    };
    
    ctx->ggml_ctx = ggml_init(params);
    if (!ctx->ggml_ctx) {
        free(ctx);
        return NULL;
    }
    
    // Initialize SkinTwin parameters
    ctx->dt = 0.001f;                    // 1ms time step
    ctx->num_molecules = 0;
    ctx->num_cells = 0;
    ctx->num_tissue_layers = 0;
    ctx->memory_size = memory_size;
    
    // Create initial tensors for multiscale states
    ctx->molecular_state = create_molecular_tensor(ctx->ggml_ctx, 1000, 8);
    ctx->cellular_state = create_cellular_tensor(ctx->ggml_ctx, 500, 12);
    ctx->tissue_state = create_tissue_tensor(ctx->ggml_ctx, 6, 16);
    ctx->organ_state = ggml_new_tensor_2d(ctx->ggml_ctx, GGML_TYPE_F32, 64, 32);
    
    if (!ctx->molecular_state || !ctx->cellular_state || 
        !ctx->tissue_state || !ctx->organ_state) {
        ggml_free(ctx->ggml_ctx);
        free(ctx);
        return NULL;
    }
    
    // Initialize tensors with default values
    ggml_set_zero(ctx->molecular_state);
    ggml_set_zero(ctx->cellular_state);
    ggml_set_zero(ctx->tissue_state);
    ggml_set_zero(ctx->organ_state);
    
    ctx->initialized = true;
    
    printf("✓ SkinTwin-ASI GGML context initialized\n");
    printf("  Memory size: %zu bytes\n", memory_size);
    printf("  Molecular tensor: [%lld, %lld]\n", 
           ctx->molecular_state->ne[0], ctx->molecular_state->ne[1]);
    printf("  Cellular tensor: [%lld, %lld]\n",
           ctx->cellular_state->ne[0], ctx->cellular_state->ne[1]);
    printf("  Tissue tensor: [%lld, %lld]\n",
           ctx->tissue_state->ne[0], ctx->tissue_state->ne[1]);
    
    return ctx;
}

void ggml_skintwin_free(struct ggml_skintwin_context * ctx) {
    if (!ctx) return;
    
    if (ctx->ggml_ctx) {
        ggml_free(ctx->ggml_ctx);
    }
    
    free(ctx);
    printf("✓ SkinTwin-ASI context freed\n");
}

int ggml_skintwin_add_molecule(
    struct ggml_skintwin_context * ctx,
    const char * name,
    const char * formula,
    float molecular_weight,
    float initial_concentration
) {
    if (!ctx || !ctx->initialized || !name || !formula) {
        return -1;
    }
    
    if (ctx->num_molecules >= 1000) {
        printf("Error: Maximum number of molecules (1000) reached\n");
        return -1;
    }
    
    int molecule_id = ctx->num_molecules++;
    
    // Update molecular state tensor
    float * data = (float *)ctx->molecular_state->data;
    int stride = ctx->molecular_state->ne[1];
    
    data[molecule_id * stride + 0] = molecular_weight;
    data[molecule_id * stride + 1] = initial_concentration;
    data[molecule_id * stride + 2] = 1.0f;  // Diffusion coefficient (default)
    data[molecule_id * stride + 3] = 0.5f;  // Partition coefficient (default)
    data[molecule_id * stride + 4] = 1.0f;  // Activity (default)
    data[molecule_id * stride + 5] = 0.0f;  // Binding affinity
    data[molecule_id * stride + 6] = 0.0f;  // Metabolic rate
    data[molecule_id * stride + 7] = 1.0f;  // Stability factor
    
    printf("✓ Added molecule '%s' (ID: %d, MW: %.2f, C0: %.4f)\n",
           name, molecule_id, molecular_weight, initial_concentration);
    
    return molecule_id;
}

struct ggml_tensor * ggml_skintwin_simulate_diffusion(
    struct ggml_skintwin_context * ctx,
    int molecule_id,
    float time_duration,
    int num_steps
) {
    if (!ctx || !ctx->initialized || molecule_id < 0 || molecule_id >= ctx->num_molecules) {
        return NULL;
    }
    
    printf("Simulating diffusion for molecule %d...\n", molecule_id);
    
    // Create result tensor for concentration over time
    struct ggml_tensor * result = ggml_new_tensor_2d(ctx->ggml_ctx, GGML_TYPE_F32, num_steps, 64);
    
    // Get molecular properties
    float * mol_data = (float *)ctx->molecular_state->data;
    int mol_stride = ctx->molecular_state->ne[1];
    
    float initial_conc = mol_data[molecule_id * mol_stride + 1];
    float diff_coeff = mol_data[molecule_id * mol_stride + 2];
    
    float dt = time_duration / num_steps;
    float * result_data = (float *)result->data;
    
    // Simple diffusion simulation using finite differences
    for (int t = 0; t < num_steps; t++) {
        for (int x = 0; x < 64; x++) {
            float position = (float)x / 64.0f;
            float time = t * dt;
            
            // Analytical solution for 1D diffusion from point source
            float concentration = initial_conc / sqrt(4.0f * M_PI * diff_coeff * (time + 0.001f)) *
                                exp(-position * position / (4.0f * diff_coeff * (time + 0.001f)));
            
            result_data[t * 64 + x] = concentration;
        }
    }
    
    printf("✓ Diffusion simulation completed (%d steps, %.3f duration)\n", num_steps, time_duration);
    
    return result;
}

int ggml_skintwin_add_cell(
    struct ggml_skintwin_context * ctx,
    const char * type,
    float x, float y, float z,
    float volume
) {
    if (!ctx || !ctx->initialized || !type) {
        return -1;
    }
    
    if (ctx->num_cells >= 500) {
        printf("Error: Maximum number of cells (500) reached\n");
        return -1;
    }
    
    int cell_id = ctx->num_cells++;
    
    // Update cellular state tensor
    float * data = (float *)ctx->cellular_state->data;
    int stride = ctx->cellular_state->ne[1];
    
    data[cell_id * stride + 0] = x;                    // Position X
    data[cell_id * stride + 1] = y;                    // Position Y
    data[cell_id * stride + 2] = z;                    // Position Z
    data[cell_id * stride + 3] = volume;               // Cell volume
    data[cell_id * stride + 4] = 1.0f;                 // Viability
    data[cell_id * stride + 5] = 0.8f;                 // Membrane integrity
    data[cell_id * stride + 6] = 1.0f;                 // Metabolic activity
    data[cell_id * stride + 7] = 0.0f;                 // Stress level
    data[cell_id * stride + 8] = 0.5f;                 // Proliferation rate
    data[cell_id * stride + 9] = 0.1f;                 // Apoptosis rate
    data[cell_id * stride + 10] = 1.0f;                // Protein synthesis
    data[cell_id * stride + 11] = 0.0f;                // Damage level
    
    printf("✓ Added cell '%s' (ID: %d, pos: [%.2f,%.2f,%.2f], vol: %.3f)\n",
           type, cell_id, x, y, z, volume);
    
    return cell_id;
}

struct ggml_tensor * ggml_skintwin_simulate_cellular_dynamics(
    struct ggml_skintwin_context * ctx,
    int cell_id,
    float time_duration,
    int num_steps
) {
    if (!ctx || !ctx->initialized || cell_id < 0 || cell_id >= ctx->num_cells) {
        return NULL;
    }
    
    printf("Simulating cellular dynamics for cell %d...\n", cell_id);
    
    // Create result tensor for cellular state evolution
    struct ggml_tensor * result = ggml_new_tensor_3d(ctx->ggml_ctx, GGML_TYPE_F32, 12, num_steps, 1);
    
    float * cell_data = (float *)ctx->cellular_state->data;
    int cell_stride = ctx->cellular_state->ne[1];
    float * result_data = (float *)result->data;
    
    float dt = time_duration / num_steps;
    
    // Copy initial state
    for (int i = 0; i < 12; i++) {
        result_data[i] = cell_data[cell_id * cell_stride + i];
    }
    
    // Simulate cellular evolution
    for (int t = 1; t < num_steps; t++) {
        for (int i = 0; i < 12; i++) {
            float prev_value = result_data[(t-1) * 12 + i];
            float change = 0.0f;
            
            switch (i) {
                case 4: // Viability
                    change = -0.01f * dt * prev_value; // Slow decay
                    break;
                case 6: // Metabolic activity
                    change = 0.1f * dt * (1.0f - prev_value); // Approach steady state
                    break;
                case 7: // Stress level
                    change = 0.05f * dt * sin(t * dt * 2.0f * M_PI); // Oscillatory stress
                    break;
                case 8: // Proliferation rate
                    change = 0.02f * dt * prev_value * (1.0f - prev_value); // Logistic growth
                    break;
                default:
                    change = 0.0f;
            }
            
            result_data[t * 12 + i] = prev_value + change;
            
            // Clamp values to reasonable ranges
            if (result_data[t * 12 + i] < 0.0f) result_data[t * 12 + i] = 0.0f;
            if (result_data[t * 12 + i] > 2.0f) result_data[t * 12 + i] = 2.0f;
        }
    }
    
    printf("✓ Cellular dynamics simulation completed\n");
    
    return result;
}

int ggml_skintwin_add_tissue_layer(
    struct ggml_skintwin_context * ctx,
    const char * name,
    float thickness,
    float porosity
) {
    if (!ctx || !ctx->initialized || !name) {
        return -1;
    }
    
    if (ctx->num_tissue_layers >= 6) {
        printf("Error: Maximum number of tissue layers (6) reached\n");
        return -1;
    }
    
    int tissue_id = ctx->num_tissue_layers++;
    
    // Update tissue state tensor
    float * data = (float *)ctx->tissue_state->data;
    int stride = ctx->tissue_state->ne[1];
    
    data[tissue_id * stride + 0] = thickness;          // Layer thickness
    data[tissue_id * stride + 1] = porosity;           // Porosity
    data[tissue_id * stride + 2] = 1.0f;               // Elastic modulus (normalized)
    data[tissue_id * stride + 3] = 0.3f;               // Poisson ratio
    data[tissue_id * stride + 4] = 1.0f;               // Permeability
    data[tissue_id * stride + 5] = 0.8f;               // Hydration level
    data[tissue_id * stride + 6] = 1.0f;               // Collagen density
    data[tissue_id * stride + 7] = 0.5f;               // Elastin density
    data[tissue_id * stride + 8] = 0.2f;               // Glycosaminoglycan density
    data[tissue_id * stride + 9] = 1.0f;               // Barrier function
    data[tissue_id * stride + 10] = 0.0f;              // Inflammation level
    data[tissue_id * stride + 11] = 1.0f;              // Vascularization
    data[tissue_id * stride + 12] = 0.8f;              // Innervation
    data[tissue_id * stride + 13] = 1.0f;              // pH level (normalized)
    data[tissue_id * stride + 14] = 0.5f;              // Temperature (normalized)
    data[tissue_id * stride + 15] = 1.0f;              // Integrity
    
    printf("✓ Added tissue layer '%s' (ID: %d, thickness: %.3f, porosity: %.3f)\n",
           name, tissue_id, thickness, porosity);
    
    return tissue_id;
}

struct ggml_tensor * ggml_skintwin_simulate_tissue_mechanics(
    struct ggml_skintwin_context * ctx,
    int tissue_id,
    float applied_stress,
    float time_duration
) {
    if (!ctx || !ctx->initialized || tissue_id < 0 || tissue_id >= ctx->num_tissue_layers) {
        return NULL;
    }
    
    printf("Simulating tissue mechanics for layer %d (stress: %.3f)...\n", tissue_id, applied_stress);
    
    // Create result tensor for mechanical response
    struct ggml_tensor * result = ggml_new_tensor_2d(ctx->ggml_ctx, GGML_TYPE_F32, 100, 16);
    
    float * tissue_data = (float *)ctx->tissue_state->data;
    int tissue_stride = ctx->tissue_state->ne[1];
    float * result_data = (float *)result->data;
    
    float elastic_modulus = tissue_data[tissue_id * tissue_stride + 2];
    float poisson_ratio = tissue_data[tissue_id * tissue_stride + 3];
    
    // Simulate viscoelastic response
    for (int t = 0; t < 100; t++) {
        float time = (float)t / 100.0f * time_duration;
        
        // Stress-strain relationship with viscoelastic effects
        float instantaneous_strain = applied_stress / elastic_modulus;
        float creep_strain = applied_stress * time * 0.1f; // Simple creep model
        float total_strain = instantaneous_strain + creep_strain;
        
        // Store mechanical properties evolution
        result_data[t * 16 + 0] = total_strain;                               // Total strain
        result_data[t * 16 + 1] = applied_stress;                            // Applied stress
        result_data[t * 16 + 2] = elastic_modulus * (1.0f - 0.1f * time);    // Modulus degradation
        result_data[t * 16 + 3] = poisson_ratio;                             // Poisson ratio
        result_data[t * 16 + 4] = total_strain * elastic_modulus;             // Elastic energy
        result_data[t * 16 + 5] = 0.05f * applied_stress * applied_stress;   // Damage accumulation
        
        // Copy other tissue properties
        for (int i = 6; i < 16; i++) {
            result_data[t * 16 + i] = tissue_data[tissue_id * tissue_stride + i];
        }
    }
    
    printf("✓ Tissue mechanics simulation completed\n");
    
    return result;
}

struct ggml_tensor * ggml_skintwin_simulate_permeation(
    struct ggml_skintwin_context * ctx,
    int molecule_id,
    float barrier_thickness,
    float partition_coefficient,
    float time_duration
) {
    if (!ctx || !ctx->initialized || molecule_id < 0 || molecule_id >= ctx->num_molecules) {
        return NULL;
    }
    
    printf("Simulating permeation for molecule %d through barrier...\n", molecule_id);
    
    // Create result tensor for concentration profile
    struct ggml_tensor * result = ggml_new_tensor_2d(ctx->ggml_ctx, GGML_TYPE_F32, 100, 100);
    
    float * mol_data = (float *)ctx->molecular_state->data;
    int mol_stride = ctx->molecular_state->ne[1];
    float * result_data = (float *)result->data;
    
    float diff_coeff = mol_data[molecule_id * mol_stride + 2];
    float initial_conc = mol_data[molecule_id * mol_stride + 1];
    
    // Simulate 2D diffusion through barrier
    for (int t = 0; t < 100; t++) {
        float time = (float)t / 100.0f * time_duration;
        
        for (int x = 0; x < 100; x++) {
            float position = (float)x / 100.0f * barrier_thickness;
            
            // Solution for diffusion through membrane with partition coefficient
            float normalized_pos = position / barrier_thickness;
            float tau = diff_coeff * time / (barrier_thickness * barrier_thickness);
            
            float concentration;
            if (tau < 0.1f) {
                // Early time solution
                concentration = initial_conc * partition_coefficient * 
                               (1.0f - normalized_pos) * sqrt(tau / M_PI);
            } else {
                // Steady state approach
                concentration = initial_conc * partition_coefficient * 
                               (1.0f - normalized_pos) * (1.0f - exp(-tau));
            }
            
            result_data[t * 100 + x] = concentration;
        }
    }
    
    printf("✓ Permeation simulation completed\n");
    
    return result;
}

struct ggml_tensor * ggml_skintwin_couple_molecular_cellular(
    struct ggml_skintwin_context * ctx,
    int molecule_id,
    int cell_id,
    float coupling_strength
) {
    if (!ctx || !ctx->initialized || 
        molecule_id < 0 || molecule_id >= ctx->num_molecules ||
        cell_id < 0 || cell_id >= ctx->num_cells) {
        return NULL;
    }
    
    printf("Coupling molecule %d with cell %d (strength: %.3f)...\n", 
           molecule_id, cell_id, coupling_strength);
    
    // Create coupling tensor
    struct ggml_tensor * coupling = ggml_new_tensor_1d(ctx->ggml_ctx, GGML_TYPE_F32, 16);
    float * coupling_data = (float *)coupling->data;
    
    float * mol_data = (float *)ctx->molecular_state->data;
    float * cell_data = (float *)ctx->cellular_state->data;
    
    int mol_stride = ctx->molecular_state->ne[1];
    int cell_stride = ctx->cellular_state->ne[1];
    
    // Calculate molecular-cellular interactions
    float mol_conc = mol_data[molecule_id * mol_stride + 1];
    float cell_viability = cell_data[cell_id * cell_stride + 4];
    float cell_membrane = cell_data[cell_id * cell_stride + 5];
    
    // Interaction effects
    coupling_data[0] = mol_conc * coupling_strength;                    // Uptake rate
    coupling_data[1] = mol_conc * cell_membrane * 0.1f;               // Membrane transport
    coupling_data[2] = mol_conc * mol_conc * 0.01f;                   // Binding saturation
    coupling_data[3] = coupling_strength * cell_viability;            // Metabolic effect
    coupling_data[4] = mol_conc * (1.0f - cell_viability) * 0.05f;   // Toxicity
    coupling_data[5] = coupling_strength * 0.5f;                      // Signal transduction
    
    // Secondary effects
    for (int i = 6; i < 16; i++) {
        coupling_data[i] = coupling_strength * sin((float)i * 0.5f) * 0.1f;
    }
    
    printf("✓ Molecular-cellular coupling established\n");
    
    return coupling;
}

struct ggml_tensor * ggml_skintwin_simulate_aging(
    struct ggml_skintwin_context * ctx,
    float aging_factor,
    float time_duration
) {
    if (!ctx || !ctx->initialized) {
        return NULL;
    }
    
    printf("Simulating aging effects (factor: %.3f, duration: %.3f)...\n", 
           aging_factor, time_duration);
    
    // Create aging simulation result
    struct ggml_tensor * result = ggml_new_tensor_2d(ctx->ggml_ctx, GGML_TYPE_F32, 100, 32);
    float * result_data = (float *)result->data;
    
    for (int t = 0; t < 100; t++) {
        float time = (float)t / 100.0f * time_duration;
        float aging_progress = aging_factor * time;
        
        // Aging effects on different components
        result_data[t * 32 + 0] = 1.0f - aging_progress * 0.1f;           // Collagen integrity
        result_data[t * 32 + 1] = 1.0f - aging_progress * 0.15f;          // Elastin integrity
        result_data[t * 32 + 2] = 1.0f - aging_progress * 0.08f;          // Hyaluronic acid
        result_data[t * 32 + 3] = 1.0f - aging_progress * 0.12f;          // Cellular metabolism
        result_data[t * 32 + 4] = aging_progress * 0.2f;                  // Oxidative stress
        result_data[t * 32 + 5] = aging_progress * 0.1f;                  // Inflammation
        result_data[t * 32 + 6] = 1.0f - aging_progress * 0.05f;          // Barrier function
        result_data[t * 32 + 7] = 1.0f - aging_progress * 0.18f;          // Skin thickness
        
        // Additional aging markers
        for (int i = 8; i < 32; i++) {
            result_data[t * 32 + i] = 1.0f - aging_progress * (0.05f + (float)i * 0.01f);
        }
    }
    
    printf("✓ Aging simulation completed\n");
    
    return result;
}

void ggml_skintwin_export_state(
    struct ggml_skintwin_context * ctx,
    const char * filename
) {
    if (!ctx || !ctx->initialized || !filename) {
        return;
    }
    
    FILE * file = fopen(filename, "w");
    if (!file) {
        printf("Error: Could not open file '%s' for writing\n", filename);
        return;
    }
    
    fprintf(file, "# SkinTwin-ASI State Export\n");
    fprintf(file, "# Generated by GGML SkinTwin implementation\n\n");
    
    fprintf(file, "System Status:\n");
    fprintf(file, "  Molecules: %d\n", ctx->num_molecules);
    fprintf(file, "  Cells: %d\n", ctx->num_cells);
    fprintf(file, "  Tissue Layers: %d\n", ctx->num_tissue_layers);
    fprintf(file, "  Memory Usage: %zu bytes\n", ctx->memory_size);
    fprintf(file, "  Time Step: %.6f\n\n", ctx->dt);
    
    // Export molecular data summary
    if (ctx->num_molecules > 0) {
        fprintf(file, "Molecular Components:\n");
        float * mol_data = (float *)ctx->molecular_state->data;
        int mol_stride = ctx->molecular_state->ne[1];
        
        for (int i = 0; i < ctx->num_molecules && i < 10; i++) {
            fprintf(file, "  Molecule %d: MW=%.2f, C=%.4f, D=%.3f\n",
                   i,
                   mol_data[i * mol_stride + 0],  // Molecular weight
                   mol_data[i * mol_stride + 1],  // Concentration
                   mol_data[i * mol_stride + 2]); // Diffusion coefficient
        }
        fprintf(file, "\n");
    }
    
    // Export cellular data summary
    if (ctx->num_cells > 0) {
        fprintf(file, "Cellular Components:\n");
        float * cell_data = (float *)ctx->cellular_state->data;
        int cell_stride = ctx->cellular_state->ne[1];
        
        for (int i = 0; i < ctx->num_cells && i < 10; i++) {
            fprintf(file, "  Cell %d: pos=[%.2f,%.2f,%.2f], vol=%.3f, viab=%.3f\n",
                   i,
                   cell_data[i * cell_stride + 0],  // X position
                   cell_data[i * cell_stride + 1],  // Y position
                   cell_data[i * cell_stride + 2],  // Z position
                   cell_data[i * cell_stride + 3],  // Volume
                   cell_data[i * cell_stride + 4]); // Viability
        }
        fprintf(file, "\n");
    }
    
    // Export tissue data summary
    if (ctx->num_tissue_layers > 0) {
        fprintf(file, "Tissue Layers:\n");
        float * tissue_data = (float *)ctx->tissue_state->data;
        int tissue_stride = ctx->tissue_state->ne[1];
        
        for (int i = 0; i < ctx->num_tissue_layers; i++) {
            fprintf(file, "  Layer %d: thickness=%.3f, porosity=%.3f, elasticity=%.3f\n",
                   i,
                   tissue_data[i * tissue_stride + 0],  // Thickness
                   tissue_data[i * tissue_stride + 1],  // Porosity
                   tissue_data[i * tissue_stride + 2]); // Elastic modulus
        }
    }
    
    fclose(file);
    printf("✓ State exported to '%s'\n", filename);
}

void ggml_skintwin_print_summary(struct ggml_skintwin_context * ctx) {
    if (!ctx || !ctx->initialized) {
        printf("SkinTwin context not initialized\n");
        return;
    }
    
    printf("\n=== SkinTwin-ASI System Summary ===\n");
    printf("System Status: %s\n", ctx->initialized ? "Active" : "Inactive");
    printf("Memory Allocated: %zu bytes\n", ctx->memory_size);
    printf("Time Step: %.6f seconds\n", ctx->dt);
    printf("\nModel Components:\n");
    printf("  Molecular Components: %d/1000\n", ctx->num_molecules);
    printf("  Cellular Components: %d/500\n", ctx->num_cells);
    printf("  Tissue Layers: %d/6\n", ctx->num_tissue_layers);
    
    printf("\nTensor Dimensions:\n");
    printf("  Molecular State: [%lld x %lld]\n", 
           ctx->molecular_state->ne[0], ctx->molecular_state->ne[1]);
    printf("  Cellular State: [%lld x %lld]\n",
           ctx->cellular_state->ne[0], ctx->cellular_state->ne[1]);
    printf("  Tissue State: [%lld x %lld]\n",
           ctx->tissue_state->ne[0], ctx->tissue_state->ne[1]);
    printf("  Organ State: [%lld x %lld]\n",
           ctx->organ_state->ne[0], ctx->organ_state->ne[1]);
    printf("=====================================\n\n");
}

// Helper function implementations
static struct ggml_tensor * create_molecular_tensor(
    struct ggml_context * ctx, 
    int num_molecules, 
    int properties_dim
) {
    return ggml_new_tensor_2d(ctx, GGML_TYPE_F32, num_molecules, properties_dim);
}

static struct ggml_tensor * create_cellular_tensor(
    struct ggml_context * ctx,
    int num_cells,
    int state_dim
) {
    return ggml_new_tensor_2d(ctx, GGML_TYPE_F32, num_cells, state_dim);
}

static struct ggml_tensor * create_tissue_tensor(
    struct ggml_context * ctx,
    int num_layers,
    int mechanical_properties_dim
) {
    return ggml_new_tensor_2d(ctx, GGML_TYPE_F32, num_layers, mechanical_properties_dim);
}

bool ggml_skintwin_validate_context(struct ggml_skintwin_context * ctx) {
    if (!ctx) return false;
    if (!ctx->initialized) return false;
    if (!ctx->ggml_ctx) return false;
    if (!ctx->molecular_state || !ctx->cellular_state || 
        !ctx->tissue_state || !ctx->organ_state) return false;
    
    return true;
}

size_t ggml_skintwin_get_memory_usage(struct ggml_skintwin_context * ctx) {
    if (!ctx || !ctx->initialized) {
        return 0;
    }
    
    return ggml_used_mem(ctx->ggml_ctx);
}

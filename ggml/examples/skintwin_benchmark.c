
#include "ggml_skintwin.h"
#include <stdio.h>
#include <stdlib.h>
#include <time.h>
#include <sys/time.h>

static double get_time_ms() {
    struct timeval tv;
    gettimeofday(&tv, NULL);
    return tv.tv_sec * 1000.0 + tv.tv_usec / 1000.0;
}

static void benchmark_molecular_operations(struct ggml_skintwin_context * ctx);
static void benchmark_cellular_operations(struct ggml_skintwin_context * ctx);
static void benchmark_tissue_operations(struct ggml_skintwin_context * ctx);
static void benchmark_multiscale_coupling(struct ggml_skintwin_context * ctx);

int main() {
    printf("=== SkinTwin-ASI GGML Performance Benchmark ===\n\n");
    
    // Initialize with larger memory for benchmarking
    size_t memory_size = 64 * 1024 * 1024;  // 64MB
    struct ggml_skintwin_context * ctx = ggml_skintwin_init(memory_size);
    
    if (!ctx) {
        printf("Failed to initialize SkinTwin context\n");
        return 1;
    }
    
    printf("Running performance benchmarks...\n\n");
    
    benchmark_molecular_operations(ctx);
    benchmark_cellular_operations(ctx);
    benchmark_tissue_operations(ctx);
    benchmark_multiscale_coupling(ctx);
    
    // Memory usage analysis
    size_t memory_used = ggml_skintwin_get_memory_usage(ctx);
    printf("Memory Analysis:\n");
    printf("  Allocated: %zu MB\n", memory_size / (1024 * 1024));
    printf("  Used: %zu MB\n", memory_used / (1024 * 1024));
    printf("  Efficiency: %.1f%%\n\n", (double)memory_used / memory_size * 100.0);
    
    ggml_skintwin_free(ctx);
    
    printf("✓ Benchmark completed successfully!\n");
    return 0;
}

static void benchmark_molecular_operations(struct ggml_skintwin_context * ctx) {
    printf("=== Molecular Operations Benchmark ===\n");
    
    double start_time = get_time_ms();
    
    // Add many molecules
    int num_molecules = 100;
    for (int i = 0; i < num_molecules; i++) {
        char name[32];
        snprintf(name, sizeof(name), "molecule_%d", i);
        
        ggml_skintwin_add_molecule(
            ctx, name, "C6H12O6", 
            180.0f + (float)i, 
            0.001f * (float)(i + 1)
        );
    }
    
    double molecule_creation_time = get_time_ms() - start_time;
    
    // Benchmark diffusion simulations
    start_time = get_time_ms();
    
    for (int i = 0; i < 10; i++) {
        struct ggml_tensor * diffusion = ggml_skintwin_simulate_diffusion(
            ctx, i, 1.0f, 100
        );
        (void)diffusion; // Suppress unused variable warning
    }
    
    double diffusion_time = get_time_ms() - start_time;
    
    // Benchmark permeation simulations
    start_time = get_time_ms();
    
    for (int i = 0; i < 5; i++) {
        struct ggml_tensor * permeation = ggml_skintwin_simulate_permeation(
            ctx, i, 0.02f, 0.5f, 1000.0f
        );
        (void)permeation; // Suppress unused variable warning
    }
    
    double permeation_time = get_time_ms() - start_time;
    
    // Results
    printf("Molecular Benchmark Results:\n");
    printf("  Created %d molecules in %.2f ms (%.1f molecules/ms)\n",
           num_molecules, molecule_creation_time, num_molecules / molecule_creation_time);
    printf("  10 diffusion sims in %.2f ms (%.2f ms/sim)\n",
           diffusion_time, diffusion_time / 10.0);
    printf("  5 permeation sims in %.2f ms (%.2f ms/sim)\n\n",
           permeation_time, permeation_time / 5.0);
}

static void benchmark_cellular_operations(struct ggml_skintwin_context * ctx) {
    printf("=== Cellular Operations Benchmark ===\n");
    
    double start_time = get_time_ms();
    
    // Add many cells
    int num_cells = 200;
    for (int i = 0; i < num_cells; i++) {
        float x = (float)(i % 20) * 0.01f;
        float y = (float)(i / 20) * 0.01f;
        float z = (float)(i % 3) * 0.05f;
        
        ggml_skintwin_add_cell(
            ctx, "test_cell", x, y, z, 1000.0f + (float)i * 10.0f
        );
    }
    
    double cell_creation_time = get_time_ms() - start_time;
    
    // Benchmark cellular dynamics
    start_time = get_time_ms();
    
    for (int i = 0; i < 10; i++) {
        struct ggml_tensor * dynamics = ggml_skintwin_simulate_cellular_dynamics(
            ctx, i, 24.0f, 50
        );
        (void)dynamics; // Suppress unused variable warning
    }
    
    double dynamics_time = get_time_ms() - start_time;
    
    printf("Cellular Benchmark Results:\n");
    printf("  Created %d cells in %.2f ms (%.1f cells/ms)\n",
           num_cells, cell_creation_time, num_cells / cell_creation_time);
    printf("  10 dynamics sims in %.2f ms (%.2f ms/sim)\n\n",
           dynamics_time, dynamics_time / 10.0);
}

static void benchmark_tissue_operations(struct ggml_skintwin_context * ctx) {
    printf("=== Tissue Operations Benchmark ===\n");
    
    double start_time = get_time_ms();
    
    // Add tissue layers (already done in previous demo, but measure time)
    const char * layer_names[] = {"layer_1", "layer_2", "layer_3", "layer_4", "layer_5"};
    
    for (int i = 0; i < 5; i++) {
        ggml_skintwin_add_tissue_layer(
            ctx, layer_names[i], 
            0.001f * (float)(i + 1), 
            0.1f + (float)i * 0.1f
        );
    }
    
    double tissue_creation_time = get_time_ms() - start_time;
    
    // Benchmark tissue mechanics
    start_time = get_time_ms();
    
    for (int i = 0; i < ctx->num_tissue_layers && i < 5; i++) {
        struct ggml_tensor * mechanics = ggml_skintwin_simulate_tissue_mechanics(
            ctx, i, 0.1f * (float)(i + 1), 5.0f
        );
        (void)mechanics; // Suppress unused variable warning
    }
    
    double mechanics_time = get_time_ms() - start_time;
    
    printf("Tissue Benchmark Results:\n");
    printf("  Created 5 tissue layers in %.2f ms\n", tissue_creation_time);
    printf("  %d mechanics sims in %.2f ms (%.2f ms/sim)\n\n",
           ctx->num_tissue_layers, mechanics_time, 
           mechanics_time / (double)ctx->num_tissue_layers);
}

static void benchmark_multiscale_coupling(struct ggml_skintwin_context * ctx) {
    printf("=== Multiscale Coupling Benchmark ===\n");
    
    double start_time = get_time_ms();
    
    // Benchmark molecular-cellular couplings
    int num_couplings = 50;
    for (int i = 0; i < num_couplings; i++) {
        int mol_id = i % ctx->num_molecules;
        int cell_id = i % ctx->num_cells;
        
        struct ggml_tensor * coupling = ggml_skintwin_couple_molecular_cellular(
            ctx, mol_id, cell_id, 0.5f + (float)i * 0.01f
        );
        (void)coupling; // Suppress unused variable warning
    }
    
    double coupling_time = get_time_ms() - start_time;
    
    printf("Multiscale Coupling Benchmark Results:\n");
    printf("  Created %d couplings in %.2f ms (%.3f ms/coupling)\n\n",
           num_couplings, coupling_time, coupling_time / num_couplings);
}

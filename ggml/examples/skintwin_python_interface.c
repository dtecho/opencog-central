
#include "ggml_skintwin.h"
#include <stdio.h>
#include <stdlib.h>
#include <string.h>

// Python C API interface for SkinTwin-ASI
// This provides a bridge between the GGML implementation and Python

typedef struct {
    struct ggml_skintwin_context * ctx;
    char * export_buffer;
    size_t buffer_size;
} python_skintwin_wrapper;

// Global wrapper instance
static python_skintwin_wrapper * global_wrapper = NULL;

// Python interface functions
int py_skintwin_init(size_t memory_size) {
    if (global_wrapper) {
        printf("SkinTwin already initialized\n");
        return 0;
    }
    
    global_wrapper = malloc(sizeof(python_skintwin_wrapper));
    if (!global_wrapper) {
        return -1;
    }
    
    global_wrapper->ctx = ggml_skintwin_init(memory_size);
    global_wrapper->export_buffer = NULL;
    global_wrapper->buffer_size = 0;
    
    if (!global_wrapper->ctx) {
        free(global_wrapper);
        global_wrapper = NULL;
        return -1;
    }
    
    printf("✓ Python SkinTwin interface initialized\n");
    return 1;
}

void py_skintwin_cleanup() {
    if (!global_wrapper) return;
    
    if (global_wrapper->ctx) {
        ggml_skintwin_free(global_wrapper->ctx);
    }
    
    if (global_wrapper->export_buffer) {
        free(global_wrapper->export_buffer);
    }
    
    free(global_wrapper);
    global_wrapper = NULL;
    
    printf("✓ Python SkinTwin interface cleaned up\n");
}

int py_add_molecule(const char * name, const char * formula, float mw, float conc) {
    if (!global_wrapper || !global_wrapper->ctx) {
        printf("SkinTwin not initialized\n");
        return -1;
    }
    
    return ggml_skintwin_add_molecule(global_wrapper->ctx, name, formula, mw, conc);
}

int py_add_cell(const char * type, float x, float y, float z, float volume) {
    if (!global_wrapper || !global_wrapper->ctx) {
        printf("SkinTwin not initialized\n");
        return -1;
    }
    
    return ggml_skintwin_add_cell(global_wrapper->ctx, type, x, y, z, volume);
}

int py_add_tissue_layer(const char * name, float thickness, float porosity) {
    if (!global_wrapper || !global_wrapper->ctx) {
        printf("SkinTwin not initialized\n");
        return -1;
    }
    
    return ggml_skintwin_add_tissue_layer(global_wrapper->ctx, name, thickness, porosity);
}

int py_simulate_diffusion(int molecule_id, float duration, int steps, float * results, int max_results) {
    if (!global_wrapper || !global_wrapper->ctx) {
        printf("SkinTwin not initialized\n");
        return -1;
    }
    
    struct ggml_tensor * diffusion = ggml_skintwin_simulate_diffusion(
        global_wrapper->ctx, molecule_id, duration, steps
    );
    
    if (!diffusion) {
        return -1;
    }
    
    // Copy results to output array
    float * tensor_data = (float *)diffusion->data;
    int total_elements = diffusion->ne[0] * diffusion->ne[1];
    int copy_elements = total_elements < max_results ? total_elements : max_results;
    
    memcpy(results, tensor_data, copy_elements * sizeof(float));
    
    return copy_elements;
}

int py_simulate_permeation(int molecule_id, float barrier_thickness, float partition_coeff, 
                          float duration, float * results, int max_results) {
    if (!global_wrapper || !global_wrapper->ctx) {
        printf("SkinTwin not initialized\n");
        return -1;
    }
    
    struct ggml_tensor * permeation = ggml_skintwin_simulate_permeation(
        global_wrapper->ctx, molecule_id, barrier_thickness, partition_coeff, duration
    );
    
    if (!permeation) {
        return -1;
    }
    
    // Copy results to output array
    float * tensor_data = (float *)permeation->data;
    int total_elements = permeation->ne[0] * permeation->ne[1];
    int copy_elements = total_elements < max_results ? total_elements : max_results;
    
    memcpy(results, tensor_data, copy_elements * sizeof(float));
    
    return copy_elements;
}

const char * py_export_state_string() {
    if (!global_wrapper || !global_wrapper->ctx) {
        return "SkinTwin not initialized";
    }
    
    // Allocate buffer if needed
    if (!global_wrapper->export_buffer) {
        global_wrapper->buffer_size = 8192;
        global_wrapper->export_buffer = malloc(global_wrapper->buffer_size);
        if (!global_wrapper->export_buffer) {
            return "Memory allocation failed";
        }
    }
    
    // Generate state summary
    snprintf(global_wrapper->export_buffer, global_wrapper->buffer_size,
             "SkinTwin-ASI State Summary:\n"
             "Molecules: %d\n"
             "Cells: %d\n" 
             "Tissue Layers: %d\n"
             "Memory Used: %zu bytes\n"
             "Status: Active",
             global_wrapper->ctx->num_molecules,
             global_wrapper->ctx->num_cells,
             global_wrapper->ctx->num_tissue_layers,
             ggml_skintwin_get_memory_usage(global_wrapper->ctx));
    
    return global_wrapper->export_buffer;
}

void py_print_summary() {
    if (!global_wrapper || !global_wrapper->ctx) {
        printf("SkinTwin not initialized\n");
        return;
    }
    
    ggml_skintwin_print_summary(global_wrapper->ctx);
}

// Test function for standalone execution
int main() {
    printf("=== SkinTwin Python Interface Test ===\n\n");
    
    // Initialize
    if (py_skintwin_init(16 * 1024 * 1024) < 0) {
        printf("Failed to initialize\n");
        return 1;
    }
    
    // Add test components
    int water = py_add_molecule("water", "H2O", 18.015f, 55.6f);
    int cell = py_add_cell("keratinocyte", 0.0f, 0.0f, 0.0f, 1000.0f);
    int tissue = py_add_tissue_layer("test_layer", 0.0001f, 0.3f);
    
    printf("Added: molecule=%d, cell=%d, tissue=%d\n", water, cell, tissue);
    
    // Test simulations
    float diffusion_results[1000];
    int num_results = py_simulate_diffusion(water, 1.0f, 10, diffusion_results, 1000);
    printf("Diffusion simulation returned %d data points\n", num_results);
    
    // Print summary
    py_print_summary();
    
    // Export state
    const char * state = py_export_state_string();
    printf("\nState Export:\n%s\n", state);
    
    // Cleanup
    py_skintwin_cleanup();
    
    printf("✓ Python interface test completed\n");
    return 0;
}

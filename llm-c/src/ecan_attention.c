
#include "../include/llm_core.h"
#include <stdio.h>
#include <stdlib.h>
#include <math.h>

// Economic Attention Networks implementation
typedef struct {
    int sti;    // Short-term importance (-1000 to +1000)
    int lti;    // Long-term importance (0 to +1000)  
    int vlti;   // Very long-term importance (0 to +1000)
} AttentionValue;

typedef struct {
    int sti_funds;
    int lti_funds;
    int sti_wage;
    int lti_wage;
    int sti_rent;
    int lti_rent;
    int max_sti;
    int min_sti;
} ECANConfig;

typedef struct {
    char* atom_id;
    AttentionValue av;
    float activity_level;
    int last_access_time;
} AtomAttention;

typedef struct {
    AtomAttention* atoms;
    size_t count;
    size_t capacity;
    ECANConfig config;
    int current_time;
} AttentionBank;

AttentionBank* create_attention_bank(size_t capacity) {
    AttentionBank* bank = malloc(sizeof(AttentionBank));
    bank->atoms = malloc(sizeof(AtomAttention) * capacity);
    bank->count = 0;
    bank->capacity = capacity;
    bank->current_time = 0;
    
    // Initialize ECAN parameters
    bank->config.sti_funds = 100000;
    bank->config.lti_funds = 100000;
    bank->config.sti_wage = 10;
    bank->config.lti_wage = 2;
    bank->config.sti_rent = 1;
    bank->config.lti_rent = 1;
    bank->config.max_sti = 1000;
    bank->config.min_sti = -1000;
    
    return bank;
}

void update_attention(AttentionBank* bank, const char* atom_id, float activity) {
    bank->current_time++;
    
    for (size_t i = 0; i < bank->count; i++) {
        if (strcmp(bank->atoms[i].atom_id, atom_id) == 0) {
            AtomAttention* atom = &bank->atoms[i];
            
            // Update activity and STI based on usage
            atom->activity_level = activity;
            atom->last_access_time = bank->current_time;
            
            // Pay wage for activity
            int sti_increase = (int)(activity * bank->config.sti_wage);
            atom->av.sti += sti_increase;
            
            // Clamp STI values
            if (atom->av.sti > bank->config.max_sti) {
                atom->av.sti = bank->config.max_sti;
            }
            if (atom->av.sti < bank->config.min_sti) {
                atom->av.sti = bank->config.min_sti;
            }
            
            break;
        }
    }
}

void decay_attention(AttentionBank* bank) {
    for (size_t i = 0; i < bank->count; i++) {
        AtomAttention* atom = &bank->atoms[i];
        
        // Apply rent (decay)
        atom->av.sti -= bank->config.sti_rent;
        atom->av.lti -= bank->config.lti_rent;
        
        // Ensure non-negative LTI
        if (atom->av.lti < 0) atom->av.lti = 0;
        if (atom->av.vlti < 0) atom->av.vlti = 0;
        
        // Clamp STI
        if (atom->av.sti < bank->config.min_sti) {
            atom->av.sti = bank->config.min_sti;
        }
    }
}

// Get atoms in attentional focus (high STI)
int get_attentional_focus(AttentionBank* bank, char** focus_atoms, int threshold) {
    int focus_count = 0;
    for (size_t i = 0; i < bank->count; i++) {
        if (bank->atoms[i].av.sti > threshold) {
            focus_atoms[focus_count++] = bank->atoms[i].atom_id;
        }
    }
    return focus_count;
}

void manage_attention_economy(AttentionBank* bank) {
    decay_attention(bank);
    
    // Implement economic competition for resources
    int total_sti = 0;
    for (size_t i = 0; i < bank->count; i++) {
        total_sti += bank->atoms[i].av.sti;
    }
    
    printf("Total STI in economy: %d\n", total_sti);
    printf("Active atoms in focus: %zu\n", bank->count);
}

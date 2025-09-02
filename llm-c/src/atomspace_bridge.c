
#include "../include/llm_core.h"
#include <stdio.h>
#include <stdlib.h>
#include <string.h>

// AtomSpace bridge for OpenCog integration
typedef struct {
    char* atom_type;
    char* atom_name;
    float truth_value;
    float confidence;
    int attention_value;
} Atom;

typedef struct {
    Atom* atoms;
    size_t count;
    size_t capacity;
} AtomSpace;

AtomSpace* create_atomspace(size_t initial_capacity) {
    AtomSpace* space = malloc(sizeof(AtomSpace));
    space->atoms = malloc(sizeof(Atom) * initial_capacity);
    space->count = 0;
    space->capacity = initial_capacity;
    return space;
}

void add_concept_node(AtomSpace* space, const char* name, float truth, float conf) {
    if (space->count >= space->capacity) {
        space->capacity *= 2;
        space->atoms = realloc(space->atoms, sizeof(Atom) * space->capacity);
    }
    
    Atom* atom = &space->atoms[space->count++];
    atom->atom_type = strdup("ConceptNode");
    atom->atom_name = strdup(name);
    atom->truth_value = truth;
    atom->confidence = conf;
    atom->attention_value = 100;
}

void add_predicate_node(AtomSpace* space, const char* name, float truth, float conf) {
    if (space->count >= space->capacity) {
        space->capacity *= 2;
        space->atoms = realloc(space->atoms, sizeof(Atom) * space->capacity);
    }
    
    Atom* atom = &space->atoms[space->count++];
    atom->atom_type = strdup("PredicateNode");
    atom->atom_name = strdup(name);
    atom->truth_value = truth;
    atom->confidence = conf;
    atom->attention_value = 100;
}

void update_attention_values(AtomSpace* space, const char* name, int new_sti) {
    for (size_t i = 0; i < space->count; i++) {
        if (strcmp(space->atoms[i].atom_name, name) == 0) {
            space->atoms[i].attention_value = new_sti;
            break;
        }
    }
}

void cleanup_atomspace(AtomSpace* space) {
    for (size_t i = 0; i < space->count; i++) {
        free(space->atoms[i].atom_type);
        free(space->atoms[i].atom_name);
    }
    free(space->atoms);
    free(space);
}

// Pattern matcher for cognitive queries
int pattern_match(AtomSpace* space, const char* pattern_type, const char* pattern_name) {
    int matches = 0;
    for (size_t i = 0; i < space->count; i++) {
        if (strcmp(space->atoms[i].atom_type, pattern_type) == 0 && 
            strstr(space->atoms[i].atom_name, pattern_name) != NULL) {
            matches++;
        }
    }
    return matches;
}

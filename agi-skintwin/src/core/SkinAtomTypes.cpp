
#include "SkinAtomTypes.h"
#include <opencog/atoms/atom_types/NameServer.h>

using namespace opencog;
using namespace skintwin;

const std::string SKIN_PREDICATES[] = {
    "has_component",
    "part_of",
    "interacts_with",
    "produces",
    "consumes",
    "regulates",
    "inhibits",
    "activates",
    "transports",
    "permeates",
    "binds_to",
    "metabolizes",
    "synthesizes",
    "degrades"
};

void skintwin::init_skin_atom_types() {
    // Register skin-specific predicates
    NameServer& nameServer = nameserver();
    
    for (const auto& predicate : SKIN_PREDICATES) {
        // Predicates are represented as PredicateNodes
        // They're already handled by the base AtomSpace
    }
    
    // Additional initialization if needed
}

bool skintwin::is_skin_molecule(Type type) {
    return type == MOLECULE_NODE || 
           type == PROTEIN_NODE || 
           type == LIPID_NODE;
}

bool skintwin::is_skin_cell(Type type) {
    return type == CELL_NODE ||
           type == KERATINOCYTE_NODE ||
           type == FIBROBLAST_NODE ||
           type == MELANOCYTE_NODE;
}

bool skintwin::is_skin_tissue(Type type) {
    return type == TISSUE_NODE ||
           type == EPIDERMIS_NODE ||
           type == DERMIS_NODE ||
           type == HYPODERMIS_NODE;
}

bool skintwin::is_skin_interaction(Type type) {
    return type == MOLECULAR_INTERACTION_LINK ||
           type == CELLULAR_INTERACTION_LINK ||
           type == TISSUE_INTERACTION_LINK;
}

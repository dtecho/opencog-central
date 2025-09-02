
#ifndef SKIN_ATOM_TYPES_H
#define SKIN_ATOM_TYPES_H

#include <opencog/atoms/atom_types/atom_types.h>

namespace opencog {

// Molecular level atom types
#define MOLECULE_NODE "MoleculeNode"
#define PROTEIN_NODE "ProteinNode" 
#define LIPID_NODE "LipidNode"
#define WATER_NODE "WaterNode"
#define COLLAGEN_NODE "CollagenNode"
#define ELASTIN_NODE "ElastinNode"

// Cellular level atom types
#define KERATINOCYTE_NODE "KeratinocyteNode"
#define FIBROBLAST_NODE "FibroblastNode"
#define MELANOCYTE_NODE "MelanocyteNode"
#define LANGERHANS_CELL_NODE "LangerhansCell"
#define CELL_MEMBRANE_NODE "CellMembraneNode"

// Tissue level atom types
#define EPIDERMIS_NODE "EpidermisNode"
#define DERMIS_NODE "DermisNode"
#define HYPODERMIS_NODE "HypodermisNode"
#define STRATUM_CORNEUM_NODE "StratumCorneumNode"
#define STRATUM_BASALE_NODE "StratumBasaleNode"

// Organ system level atom types
#define SKIN_BARRIER_NODE "SkinBarrierNode"
#define SEBACEOUS_GLAND_NODE "SebaceousGlandNode"
#define SWEAT_GLAND_NODE "SweatGlandNode"
#define HAIR_FOLLICLE_NODE "HairFollicleNode"

// Process and interaction links
#define MOLECULAR_INTERACTION_LINK "MolecularInteractionLink"
#define CELLULAR_COMMUNICATION_LINK "CellularCommunicationLink"
#define TISSUE_ORGANIZATION_LINK "TissueOrganizationLink"
#define BARRIER_FUNCTION_LINK "BarrierFunctionLink"
#define PERMEABILITY_LINK "PermeabilityLink"
#define ABSORPTION_LINK "AbsorptionLink"

// Multiscale transition links
#define SCALE_TRANSITION_LINK "ScaleTransitionLink"
#define EMERGENT_PROPERTY_LINK "EmergentPropertyLink"
#define UPSCALE_LINK "UpscaleLink"
#define DOWNSCALE_LINK "DownscaleLink"

} // namespace opencog

#endif // SKIN_ATOM_TYPES_H
#ifndef _SKIN_ATOM_TYPES_H
#define _SKIN_ATOM_TYPES_H

#include <opencog/atoms/atom_types/atom_types.h>

namespace skintwin {

// Skin-specific atom types
enum SkinAtomType {
    // Molecular scale types
    MOLECULE_NODE = CONCEPT_NODE,
    PROTEIN_NODE = CONCEPT_NODE,
    LIPID_NODE = CONCEPT_NODE,
    
    // Cellular scale types  
    CELL_NODE = CONCEPT_NODE,
    KERATINOCYTE_NODE = CONCEPT_NODE,
    FIBROBLAST_NODE = CONCEPT_NODE,
    MELANOCYTE_NODE = CONCEPT_NODE,
    
    // Tissue scale types
    TISSUE_NODE = CONCEPT_NODE,
    EPIDERMIS_NODE = CONCEPT_NODE,
    DERMIS_NODE = CONCEPT_NODE,
    HYPODERMIS_NODE = CONCEPT_NODE,
    
    // Interaction types
    MOLECULAR_INTERACTION_LINK = EVALUATION_LINK,
    CELLULAR_INTERACTION_LINK = EVALUATION_LINK,
    TISSUE_INTERACTION_LINK = EVALUATION_LINK,
    
    // Process types
    BIOLOGICAL_PROCESS_LINK = EVALUATION_LINK,
    CHEMICAL_REACTION_LINK = EVALUATION_LINK,
    TRANSPORT_PROCESS_LINK = EVALUATION_LINK
};

// Skin-specific predicate names
extern const std::string SKIN_PREDICATES[];

// Initialize skin-specific atom types
void init_skin_atom_types();

// Helper functions for skin atom type checking
bool is_skin_molecule(opencog::Type type);
bool is_skin_cell(opencog::Type type);
bool is_skin_tissue(opencog::Type type);
bool is_skin_interaction(opencog::Type type);

} // namespace skintwin

#endif // _SKIN_ATOM_TYPES_H

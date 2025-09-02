
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


#include "SkinAtomSpace.h"
#include "SkinAtomTypes.h"
#include <opencog/atoms/base/Link.h>
#include <opencog/atoms/base/Node.h>
#include <opencog/atoms/truthvalue/SimpleTruthValue.h>

namespace opencog {
namespace skin {

SkinAtomSpace::SkinAtomSpace() : _atomspace(createAtomSpace()) {
    // Initialize standard scale contexts
    create_scale_context("molecular");
    create_scale_context("cellular");
    create_scale_context("tissue");
    create_scale_context("organ");
}

SkinAtomSpace::~SkinAtomSpace() {
    _scale_contexts.clear();
}

void SkinAtomSpace::create_scale_context(const std::string& scale_name) {
    Handle context = _atomspace->add_node(CONCEPT_NODE, scale_name + "_context");
    _scale_contexts[scale_name] = context;
}

Handle SkinAtomSpace::get_scale_context(const std::string& scale_name) {
    auto it = _scale_contexts.find(scale_name);
    if (it != _scale_contexts.end()) {
        return it->second;
    }
    return Handle::UNDEFINED;
}

Handle SkinAtomSpace::create_molecule(const std::string& name, const std::string& formula) {
    Handle mol_node = _atomspace->add_node(MOLECULE_NODE, name);
    Handle formula_node = _atomspace->add_node(CONCEPT_NODE, formula);
    Handle molecular_context = get_scale_context("molecular");
    
    // Create molecular formula relationship
    HandleSeq formula_link_seq = {mol_node, formula_node};
    Handle formula_link = _atomspace->add_link(EVALUATION_LINK, formula_link_seq);
    
    // Associate with molecular context
    HandleSeq context_seq = {molecular_context, mol_node};
    _atomspace->add_link(MEMBER_LINK, context_seq);
    
    return mol_node;
}

Handle SkinAtomSpace::create_protein(const std::string& name, const std::string& sequence) {
    Handle protein_node = _atomspace->add_node(PROTEIN_NODE, name);
    Handle sequence_node = _atomspace->add_node(CONCEPT_NODE, sequence);
    Handle molecular_context = get_scale_context("molecular");
    
    // Create sequence relationship
    HandleSeq seq_link_seq = {protein_node, sequence_node};
    Handle seq_link = _atomspace->add_link(EVALUATION_LINK, seq_link_seq);
    
    // Associate with molecular context
    HandleSeq context_seq = {molecular_context, protein_node};
    _atomspace->add_link(MEMBER_LINK, context_seq);
    
    return protein_node;
}

Handle SkinAtomSpace::create_molecular_interaction(const Handle& mol1, const Handle& mol2,
                                                 const std::string& interaction_type) {
    Handle interaction_pred = _atomspace->add_node(PREDICATE_NODE, interaction_type);
    HandleSeq interaction_seq = {interaction_pred, mol1, mol2};
    Handle interaction_link = _atomspace->add_link(MOLECULAR_INTERACTION_LINK, interaction_seq);
    
    // Set truth value based on interaction strength
    TruthValuePtr tv = SimpleTruthValue::createTV(0.8, 0.9);
    interaction_link->setTruthValue(tv);
    
    return interaction_link;
}

Handle SkinAtomSpace::create_cell(const std::string& cell_type, const Handle& location) {
    Handle cell_node;
    
    if (cell_type == "keratinocyte") {
        cell_node = _atomspace->add_node(KERATINOCYTE_NODE, cell_type + "_" + std::to_string(rand()));
    } else if (cell_type == "fibroblast") {
        cell_node = _atomspace->add_node(FIBROBLAST_NODE, cell_type + "_" + std::to_string(rand()));
    } else if (cell_type == "melanocyte") {
        cell_node = _atomspace->add_node(MELANOCYTE_NODE, cell_type + "_" + std::to_string(rand()));
    } else {
        cell_node = _atomspace->add_node(CONCEPT_NODE, cell_type + "_cell_" + std::to_string(rand()));
    }
    
    Handle cellular_context = get_scale_context("cellular");
    
    // Associate with cellular context
    HandleSeq context_seq = {cellular_context, cell_node};
    _atomspace->add_link(MEMBER_LINK, context_seq);
    
    // Set location if provided
    if (location != Handle::UNDEFINED) {
        HandleSeq location_seq = {cell_node, location};
        _atomspace->add_link(AT_LOCATION_LINK, location_seq);
    }
    
    return cell_node;
}

Handle SkinAtomSpace::create_cellular_component(const std::string& component_name,
                                              const Handle& parent_cell) {
    Handle component_node = _atomspace->add_node(CONCEPT_NODE, component_name);
    
    // Create part-of relationship
    HandleSeq part_of_seq = {component_node, parent_cell};
    Handle part_of_link = _atomspace->add_link(PART_OF_LINK, part_of_seq);
    
    return component_node;
}

Handle SkinAtomSpace::create_cell_communication(const Handle& sender, const Handle& receiver,
                                              const std::string& signal_type) {
    Handle signal_pred = _atomspace->add_node(PREDICATE_NODE, signal_type);
    HandleSeq comm_seq = {signal_pred, sender, receiver};
    Handle comm_link = _atomspace->add_link(CELLULAR_COMMUNICATION_LINK, comm_seq);
    
    return comm_link;
}

Handle SkinAtomSpace::create_tissue_layer(const std::string& layer_name,
                                        const std::vector<Handle>& constituent_cells) {
    Handle tissue_node;
    
    if (layer_name == "epidermis") {
        tissue_node = _atomspace->add_node(EPIDERMIS_NODE, layer_name);
    } else if (layer_name == "dermis") {
        tissue_node = _atomspace->add_node(DERMIS_NODE, layer_name);
    } else if (layer_name == "hypodermis") {
        tissue_node = _atomspace->add_node(HYPODERMIS_NODE, layer_name);
    } else {
        tissue_node = _atomspace->add_node(CONCEPT_NODE, layer_name + "_tissue");
    }
    
    Handle tissue_context = get_scale_context("tissue");
    
    // Associate with tissue context
    HandleSeq context_seq = {tissue_context, tissue_node};
    _atomspace->add_link(MEMBER_LINK, context_seq);
    
    // Add constituent cells
    for (const Handle& cell : constituent_cells) {
        HandleSeq composition_seq = {tissue_node, cell};
        _atomspace->add_link(TISSUE_ORGANIZATION_LINK, composition_seq);
    }
    
    return tissue_node;
}

Handle SkinAtomSpace::create_scale_transition(const Handle& lower_scale,
                                            const Handle& higher_scale,
                                            const std::string& transition_type) {
    Handle transition_pred = _atomspace->add_node(PREDICATE_NODE, transition_type);
    HandleSeq transition_seq = {transition_pred, lower_scale, higher_scale};
    Handle transition_link = _atomspace->add_link(SCALE_TRANSITION_LINK, transition_seq);
    
    return transition_link;
}

std::vector<Handle> SkinAtomSpace::get_molecules_in_context(const std::string& context) {
    std::vector<Handle> molecules;
    Handle context_handle = get_scale_context(context);
    
    if (context_handle != Handle::UNDEFINED) {
        HandleSeq member_links = _atomspace->get_incoming_set(context_handle);
        for (const Handle& link : member_links) {
            if (link->get_type() == MEMBER_LINK) {
                HandleSeq outgoing = link->getOutgoingSet();
                if (outgoing.size() == 2 && outgoing[0] == context_handle) {
                    molecules.push_back(outgoing[1]);
                }
            }
        }
    }
    
    return molecules;
}

void SkinAtomSpace::update_concentrations(const std::map<Handle, double>& concentrations) {
    for (const auto& pair : concentrations) {
        Handle conc_pred = _atomspace->add_node(PREDICATE_NODE, "concentration");
        Handle conc_value = _atomspace->add_node(NUMBER_NODE, std::to_string(pair.second));
        
        HandleSeq conc_seq = {conc_pred, pair.first, conc_value};
        Handle conc_link = _atomspace->add_link(EVALUATION_LINK, conc_seq);
        
        TruthValuePtr tv = SimpleTruthValue::createTV(1.0, 1.0);
        conc_link->setTruthValue(tv);
    }
}

} // namespace skin
} // namespace opencog

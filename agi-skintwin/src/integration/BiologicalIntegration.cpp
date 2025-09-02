
#include "BiologicalIntegration.h"
#include "../core/SkinAtomSpace.h"
#include <opencog/atoms/base/Handle.h>
#include <opencog/atoms/base/Node.h>
#include <opencog/atoms/base/Link.h>

using namespace opencog;
using namespace skintwin;

BiologicalIntegration::BiologicalIntegration(SkinAtomSpace* atomspace) 
    : m_atomspace(atomspace) {
}

BiologicalIntegration::~BiologicalIntegration() {
}

Handle BiologicalIntegration::create_protein(const std::string& name, 
                                           const std::string& sequence,
                                           const std::string& structure) {
    // Create protein concept node
    Handle protein_node = m_atomspace->add_node(CONCEPT_NODE, name);
    
    // Add sequence information
    Handle sequence_node = m_atomspace->add_node(CONCEPT_NODE, "sequence:" + sequence);
    Handle sequence_link = m_atomspace->add_link(INHERITANCE_LINK, 
        {protein_node, sequence_node});
    
    // Add structure information if provided
    if (!structure.empty()) {
        Handle structure_node = m_atomspace->add_node(CONCEPT_NODE, "structure:" + structure);
        Handle structure_link = m_atomspace->add_link(INHERITANCE_LINK,
            {protein_node, structure_node});
    }
    
    // Mark as protein type
    Handle protein_type = m_atomspace->add_node(CONCEPT_NODE, "Protein");
    Handle type_link = m_atomspace->add_link(INHERITANCE_LINK,
        {protein_node, protein_type});
    
    return protein_node;
}

Handle BiologicalIntegration::create_cell(const std::string& cell_type,
                                        const std::vector<std::string>& components) {
    // Create cell concept node
    Handle cell_node = m_atomspace->add_node(CONCEPT_NODE, cell_type + "_cell");
    
    // Add cell type classification
    Handle cell_type_node = m_atomspace->add_node(CONCEPT_NODE, cell_type);
    Handle type_link = m_atomspace->add_link(INHERITANCE_LINK,
        {cell_node, cell_type_node});
    
    // Add cellular components
    for (const auto& component : components) {
        Handle component_node = m_atomspace->add_node(CONCEPT_NODE, component);
        Handle has_component = m_atomspace->add_link(EVALUATION_LINK,
            {m_atomspace->add_node(PREDICATE_NODE, "has_component"),
             m_atomspace->add_link(LIST_LINK, {cell_node, component_node})});
    }
    
    return cell_node;
}

Handle BiologicalIntegration::create_tissue(const std::string& tissue_name,
                                          const std::vector<Handle>& cells) {
    // Create tissue concept node
    Handle tissue_node = m_atomspace->add_node(CONCEPT_NODE, tissue_name);
    
    // Link cells to tissue
    for (const auto& cell : cells) {
        Handle part_of = m_atomspace->add_link(EVALUATION_LINK,
            {m_atomspace->add_node(PREDICATE_NODE, "part_of"),
             m_atomspace->add_link(LIST_LINK, {cell, tissue_node})});
    }
    
    // Mark as tissue type
    Handle tissue_type = m_atomspace->add_node(CONCEPT_NODE, "Tissue");
    Handle type_link = m_atomspace->add_link(INHERITANCE_LINK,
        {tissue_node, tissue_type});
    
    return tissue_node;
}

std::vector<Handle> BiologicalIntegration::model_protein_interactions(
    const std::vector<std::pair<Handle, Handle>>& protein_pairs,
    const std::string& interaction_type) {
    
    std::vector<Handle> interactions;
    
    for (const auto& pair : protein_pairs) {
        Handle interaction = m_atomspace->add_link(EVALUATION_LINK,
            {m_atomspace->add_node(PREDICATE_NODE, interaction_type),
             m_atomspace->add_link(LIST_LINK, {pair.first, pair.second})});
        interactions.push_back(interaction);
    }
    
    return interactions;
}

std::vector<Handle> BiologicalIntegration::model_cellular_processes(
    const Handle& cell, const std::vector<std::string>& processes) {
    
    std::vector<Handle> process_links;
    
    for (const auto& process : processes) {
        Handle process_node = m_atomspace->add_node(CONCEPT_NODE, process);
        Handle performs = m_atomspace->add_link(EVALUATION_LINK,
            {m_atomspace->add_node(PREDICATE_NODE, "performs"),
             m_atomspace->add_link(LIST_LINK, {cell, process_node})});
        process_links.push_back(performs);
    }
    
    return process_links;
}

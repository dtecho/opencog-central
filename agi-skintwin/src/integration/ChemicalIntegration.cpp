
#include "ChemicalIntegration.h"
#include "../core/SkinAtomSpace.h"
#include <opencog/atoms/base/Handle.h>
#include <opencog/atoms/base/Node.h>
#include <opencog/atoms/base/Link.h>

using namespace opencog;
using namespace skintwin;

ChemicalIntegration::ChemicalIntegration(SkinAtomSpace* atomspace) 
    : m_atomspace(atomspace) {
}

ChemicalIntegration::~ChemicalIntegration() {
}

Handle ChemicalIntegration::create_molecule(const std::string& name,
                                          const std::string& smiles,
                                          const std::string& formula) {
    // Create molecule concept node
    Handle molecule_node = m_atomspace->add_node(CONCEPT_NODE, name);
    
    // Add SMILES representation
    if (!smiles.empty()) {
        Handle smiles_node = m_atomspace->add_node(CONCEPT_NODE, "SMILES:" + smiles);
        Handle smiles_link = m_atomspace->add_link(INHERITANCE_LINK,
            {molecule_node, smiles_node});
    }
    
    // Add molecular formula
    if (!formula.empty()) {
        Handle formula_node = m_atomspace->add_node(CONCEPT_NODE, "formula:" + formula);
        Handle formula_link = m_atomspace->add_link(INHERITANCE_LINK,
            {molecule_node, formula_node});
    }
    
    // Mark as molecule type
    Handle molecule_type = m_atomspace->add_node(CONCEPT_NODE, "Molecule");
    Handle type_link = m_atomspace->add_link(INHERITANCE_LINK,
        {molecule_node, molecule_type});
    
    return molecule_node;
}

Handle ChemicalIntegration::create_reaction(const std::vector<Handle>& reactants,
                                          const std::vector<Handle>& products,
                                          const std::string& reaction_type) {
    // Create reaction node
    Handle reaction_node = m_atomspace->add_node(CONCEPT_NODE, 
        "reaction_" + std::to_string(reactants.size()) + "_" + std::to_string(products.size()));
    
    // Link reactants
    for (const auto& reactant : reactants) {
        Handle reactant_link = m_atomspace->add_link(EVALUATION_LINK,
            {m_atomspace->add_node(PREDICATE_NODE, "reactant"),
             m_atomspace->add_link(LIST_LINK, {reaction_node, reactant})});
    }
    
    // Link products
    for (const auto& product : products) {
        Handle product_link = m_atomspace->add_link(EVALUATION_LINK,
            {m_atomspace->add_node(PREDICATE_NODE, "product"),
             m_atomspace->add_link(LIST_LINK, {reaction_node, product})});
    }
    
    // Add reaction type
    Handle type_node = m_atomspace->add_node(CONCEPT_NODE, reaction_type);
    Handle type_link = m_atomspace->add_link(INHERITANCE_LINK,
        {reaction_node, type_node});
    
    return reaction_node;
}

std::vector<Handle> ChemicalIntegration::model_molecular_interactions(
    const std::vector<std::pair<Handle, Handle>>& molecule_pairs,
    const std::string& interaction_type) {
    
    std::vector<Handle> interactions;
    
    for (const auto& pair : molecule_pairs) {
        Handle interaction = m_atomspace->add_link(EVALUATION_LINK,
            {m_atomspace->add_node(PREDICATE_NODE, interaction_type),
             m_atomspace->add_link(LIST_LINK, {pair.first, pair.second})});
        interactions.push_back(interaction);
    }
    
    return interactions;
}

Handle ChemicalIntegration::create_chemical_pathway(const std::string& pathway_name,
                                                  const std::vector<Handle>& reactions) {
    // Create pathway node
    Handle pathway_node = m_atomspace->add_node(CONCEPT_NODE, pathway_name);
    
    // Link reactions to pathway
    for (const auto& reaction : reactions) {
        Handle part_of = m_atomspace->add_link(EVALUATION_LINK,
            {m_atomspace->add_node(PREDICATE_NODE, "part_of_pathway"),
             m_atomspace->add_link(LIST_LINK, {reaction, pathway_node})});
    }
    
    // Mark as pathway type
    Handle pathway_type = m_atomspace->add_node(CONCEPT_NODE, "ChemicalPathway");
    Handle type_link = m_atomspace->add_link(INHERITANCE_LINK,
        {pathway_node, pathway_type});
    
    return pathway_node;
}

std::vector<Handle> ChemicalIntegration::calculate_molecular_properties(
    const Handle& molecule, const std::map<std::string, double>& properties) {
    
    std::vector<Handle> property_links;
    
    for (const auto& prop : properties) {
        Handle property_node = m_atomspace->add_node(CONCEPT_NODE, prop.first);
        Handle value_node = m_atomspace->add_node(NUMBER_NODE, std::to_string(prop.second));
        
        Handle property_link = m_atomspace->add_link(EVALUATION_LINK,
            {m_atomspace->add_node(PREDICATE_NODE, "has_property"),
             m_atomspace->add_link(LIST_LINK, {molecule, property_node, value_node})});
        
        property_links.push_back(property_link);
    }
    
    return property_links;
}

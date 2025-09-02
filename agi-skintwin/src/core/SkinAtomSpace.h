
#ifndef SKIN_ATOMSPACE_H
#define SKIN_ATOMSPACE_H

#include <opencog/atomspace/AtomSpace.h>
#include <opencog/atoms/base/Handle.h>
#include <opencog/atoms/base/Node.h>
#include <opencog/atoms/base/Link.h>
#include <memory>
#include <vector>
#include <map>

namespace opencog {
namespace skin {

class SkinAtomSpace {
private:
    AtomSpacePtr _atomspace;
    std::map<std::string, Handle> _scale_contexts;
    
public:
    SkinAtomSpace();
    ~SkinAtomSpace();
    
    // Core AtomSpace operations
    AtomSpacePtr get_atomspace() const { return _atomspace; }
    
    // Multiscale context management
    void create_scale_context(const std::string& scale_name);
    Handle get_scale_context(const std::string& scale_name);
    
    // Molecular level operations
    Handle create_molecule(const std::string& name, const std::string& formula);
    Handle create_protein(const std::string& name, const std::string& sequence);
    Handle create_molecular_interaction(const Handle& mol1, const Handle& mol2, 
                                      const std::string& interaction_type);
    
    // Cellular level operations
    Handle create_cell(const std::string& cell_type, const Handle& location);
    Handle create_cellular_component(const std::string& component_name, 
                                   const Handle& parent_cell);
    Handle create_cell_communication(const Handle& sender, const Handle& receiver,
                                   const std::string& signal_type);
    
    // Tissue level operations
    Handle create_tissue_layer(const std::string& layer_name, 
                             const std::vector<Handle>& constituent_cells);
    Handle create_tissue_structure(const std::string& structure_name,
                                 const std::vector<Handle>& tissue_layers);
    
    // Organ system operations
    Handle create_skin_system(const std::vector<Handle>& tissues,
                            const std::vector<Handle>& appendages);
    Handle create_barrier_function(const Handle& tissue, 
                                  const std::string& barrier_type);
    
    // Scale transition operations
    Handle create_scale_transition(const Handle& lower_scale, 
                                 const Handle& higher_scale,
                                 const std::string& transition_type);
    Handle create_emergent_property(const Handle& system,
                                  const std::string& property_name);
    
    // Query operations
    std::vector<Handle> get_molecules_in_context(const std::string& context);
    std::vector<Handle> get_cells_of_type(const std::string& cell_type);
    std::vector<Handle> get_tissue_components(const Handle& tissue);
    
    // Simulation support
    void update_concentrations(const std::map<Handle, double>& concentrations);
    void propagate_signals(const Handle& source, double signal_strength);
    void compute_barrier_permeability(const Handle& barrier, const Handle& molecule);
};

} // namespace skin
} // namespace opencog

#endif // SKIN_ATOMSPACE_H

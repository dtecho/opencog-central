
#ifndef MULTISCALE_MODEL_H
#define MULTISCALE_MODEL_H

#include <opencog/atomspace/AtomSpace.h>
#include "../core/SkinAtomSpace.h"
#include <memory>
#include <vector>
#include <functional>

namespace opencog {
namespace skin {

struct ScaleLevel {
    std::string name;
    double spatial_scale;  // in meters
    double temporal_scale; // in seconds
    std::vector<std::string> relevant_types;
};

class MultiscaleModel {
private:
    std::shared_ptr<SkinAtomSpace> _skin_atomspace;
    std::vector<ScaleLevel> _scale_levels;
    std::map<std::string, std::function<void()>> _scale_updaters;
    
    // Scale-specific computation methods
    void update_molecular_dynamics();
    void update_cellular_behavior();
    void update_tissue_mechanics();
    void update_organ_physiology();
    
    // Cross-scale interaction methods
    void propagate_molecular_to_cellular();
    void propagate_cellular_to_tissue();
    void propagate_tissue_to_organ();
    
public:
    MultiscaleModel(std::shared_ptr<SkinAtomSpace> skin_atomspace);
    ~MultiscaleModel();
    
    // Scale management
    void add_scale_level(const ScaleLevel& scale);
    void set_scale_updater(const std::string& scale_name,
                          std::function<void()> updater);
    
    // Model initialization
    void initialize_molecular_scale();
    void initialize_cellular_scale();
    void initialize_tissue_scale();
    void initialize_organ_scale();
    
    // Simulation control
    void step_simulation(double dt);
    void step_scale(const std::string& scale_name, double dt);
    void synchronize_scales();
    
    // Data integration
    void integrate_biological_data(const std::string& data_source);
    void integrate_chemical_data(const std::string& chemical_db);
    
    // Model queries
    std::vector<Handle> get_scale_components(const std::string& scale_name);
    Handle get_emergent_property(const Handle& system, const std::string& property);
    double compute_barrier_permeability(const Handle& barrier, const Handle& molecule);
    
    // Validation and verification
    bool validate_scale_consistency();
    std::vector<std::string> check_model_integrity();
};

} // namespace skin
} // namespace opencog

#endif // MULTISCALE_MODEL_H


#ifndef BIOLOGICAL_INTEGRATION_H
#define BIOLOGICAL_INTEGRATION_H

#include <opencog/atomspace/AtomSpace.h>
#include "../core/SkinAtomSpace.h"
#include "../../agi-bio/bioscience/types/BioScienceTypes.cc"
#include <memory>
#include <string>
#include <vector>

namespace opencog {
namespace skin {

class BiologicalIntegration {
private:
    std::shared_ptr<SkinAtomSpace> _skin_atomspace;
    AtomSpacePtr _bio_atomspace;
    
    // Pathway integration
    void integrate_signaling_pathways();
    void integrate_metabolic_pathways();
    void integrate_cell_cycle_pathways();
    
    // Gene expression integration
    void integrate_gene_expression_data();
    void map_genes_to_proteins();
    void create_regulatory_networks();
    
public:
    BiologicalIntegration(std::shared_ptr<SkinAtomSpace> skin_atomspace);
    ~BiologicalIntegration();
    
    // Data integration methods
    void load_pathway_data(const std::string& pathway_file);
    void load_gene_expression_data(const std::string& expression_file);
    void load_protein_interaction_data(const std::string& ppi_file);
    
    // Biological process modeling
    Handle create_signaling_pathway(const std::string& pathway_name,
                                  const std::vector<Handle>& components);
    Handle create_metabolic_reaction(const Handle& substrate, const Handle& product,
                                   const Handle& enzyme);
    Handle create_gene_regulation(const Handle& gene, const Handle& transcription_factor,
                                const std::string& regulation_type);
    
    // Skin-specific biological processes
    void model_differentiation_pathway();
    void model_barrier_formation();
    void model_wound_healing_response();
    void model_aging_processes();
    
    // Query methods
    std::vector<Handle> get_active_pathways_in_cell(const Handle& cell);
    std::vector<Handle> get_expressed_genes_in_tissue(const Handle& tissue);
    double get_pathway_activity(const Handle& pathway, const Handle& context);
    
    // Integration with agi-bio utilities
    void sync_with_bio_atomspace();
    void import_bio_knowledge(const std::string& knowledge_source);
};

} // namespace skin
} // namespace opencog

#endif // BIOLOGICAL_INTEGRATION_H

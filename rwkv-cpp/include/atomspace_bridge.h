
#pragma once

#include "rwkv_wrapper.h"
#include <string>
#include <vector>
#include <memory>

namespace rwkv {
namespace opencog {

// Forward declarations for OpenCog AtomSpace types
class AtomSpace;
class Handle;
class TruthValue;

class AtomSpaceBridge {
public:
    AtomSpaceBridge(std::shared_ptr<RWKVModel> model);
    ~AtomSpaceBridge();

    // Convert RWKV embeddings to AtomSpace structures
    Handle embedText(const std::string& text, AtomSpace* atomspace);
    
    // Generate text from AtomSpace query results
    std::string generateFromAtoms(const std::vector<Handle>& atoms, AtomSpace* atomspace);
    
    // Semantic similarity using RWKV embeddings
    double computeSemanticSimilarity(Handle atom1, Handle atom2, AtomSpace* atomspace);
    
    // Pattern matching with RWKV semantic understanding
    std::vector<Handle> semanticPatternMatch(const std::string& pattern, AtomSpace* atomspace);

private:
    std::shared_ptr<RWKVModel> model_;
    void* atomspace_context_;
};

} // namespace opencog
} // namespace rwkv

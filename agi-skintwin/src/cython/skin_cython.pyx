
# distutils: language = c++
# distutils: sources = ../core/SkinAtomSpace.cpp

from libcpp.vector cimport vector
from libcpp.string cimport string
from libcpp.map cimport map
from opencog.cython.opencog.atomspace cimport *

cdef extern from "../core/SkinAtomSpace.h" namespace "opencog::skin":
    cdef cppclass SkinAtomSpace:
        SkinAtomSpace()
        AtomSpace* get_atomspace()
        void create_scale_context(const string& scale_name)
        cHandle get_scale_context(const string& scale_name)
        
        # Molecular operations
        cHandle create_molecule(const string& name, const string& formula)
        cHandle create_protein(const string& name, const string& sequence)
        cHandle create_molecular_interaction(const cHandle& mol1, const cHandle& mol2,
                                           const string& interaction_type)
        
        # Cellular operations
        cHandle create_cell(const string& cell_type, const cHandle& location)
        cHandle create_cellular_component(const string& component_name,
                                        const cHandle& parent_cell)
        cHandle create_cell_communication(const cHandle& sender, const cHandle& receiver,
                                        const string& signal_type)
        
        # Tissue operations
        cHandle create_tissue_layer(const string& layer_name,
                                  const vector[cHandle]& constituent_cells)
        
        # Scale transition operations
        cHandle create_scale_transition(const cHandle& lower_scale,
                                      const cHandle& higher_scale,
                                      const string& transition_type)
        
        # Query operations
        vector[cHandle] get_molecules_in_context(const string& context)
        
        # Simulation operations
        void update_concentrations(const map[cHandle, double]& concentrations)

cdef class PySkinAtomSpace:
    cdef SkinAtomSpace* c_skin_atomspace
    cdef AtomSpace atomspace
    
    def __cinit__(self):
        self.c_skin_atomspace = new SkinAtomSpace()
        cdef cAtomSpace* c_atomspace_ptr = self.c_skin_atomspace.get_atomspace()
        self.atomspace = AtomSpace()
        self.atomspace.atomspace = c_atomspace_ptr
    
    def __dealloc__(self):
        del self.c_skin_atomspace
    
    def create_scale_context(self, scale_name):
        """Create a new scale context for multiscale modeling"""
        cdef string c_scale_name = scale_name.encode('utf-8')
        self.c_skin_atomspace.create_scale_context(c_scale_name)
    
    def create_molecule(self, name, formula):
        """Create a molecule node with chemical formula"""
        cdef string c_name = name.encode('utf-8')
        cdef string c_formula = formula.encode('utf-8')
        cdef cHandle c_handle = self.c_skin_atomspace.create_molecule(c_name, c_formula)
        return Handle(c_handle.value())
    
    def create_protein(self, name, sequence):
        """Create a protein node with amino acid sequence"""
        cdef string c_name = name.encode('utf-8')
        cdef string c_sequence = sequence.encode('utf-8')
        cdef cHandle c_handle = self.c_skin_atomspace.create_protein(c_name, c_sequence)
        return Handle(c_handle.value())
    
    def create_molecular_interaction(self, mol1, mol2, interaction_type):
        """Create molecular interaction between two molecules"""
        cdef cHandle c_mol1 = deref_handle(mol1)
        cdef cHandle c_mol2 = deref_handle(mol2)
        cdef string c_interaction = interaction_type.encode('utf-8')
        cdef cHandle c_handle = self.c_skin_atomspace.create_molecular_interaction(
            c_mol1, c_mol2, c_interaction)
        return Handle(c_handle.value())
    
    def create_cell(self, cell_type, location=None):
        """Create a cell of specified type at given location"""
        cdef string c_cell_type = cell_type.encode('utf-8')
        cdef cHandle c_location
        
        if location is not None:
            c_location = deref_handle(location)
        else:
            c_location = cHandle_UNDEFINED()
            
        cdef cHandle c_handle = self.c_skin_atomspace.create_cell(c_cell_type, c_location)
        return Handle(c_handle.value())
    
    def create_tissue_layer(self, layer_name, constituent_cells):
        """Create tissue layer from constituent cells"""
        cdef string c_layer_name = layer_name.encode('utf-8')
        cdef vector[cHandle] c_cells
        
        for cell in constituent_cells:
            c_cells.push_back(deref_handle(cell))
            
        cdef cHandle c_handle = self.c_skin_atomspace.create_tissue_layer(c_layer_name, c_cells)
        return Handle(c_handle.value())
    
    def create_scale_transition(self, lower_scale, higher_scale, transition_type):
        """Create transition between different scales"""
        cdef cHandle c_lower = deref_handle(lower_scale)
        cdef cHandle c_higher = deref_handle(higher_scale)
        cdef string c_transition = transition_type.encode('utf-8')
        
        cdef cHandle c_handle = self.c_skin_atomspace.create_scale_transition(
            c_lower, c_higher, c_transition)
        return Handle(c_handle.value())
    
    def get_molecules_in_context(self, context):
        """Query molecules in specified context"""
        cdef string c_context = context.encode('utf-8')
        cdef vector[cHandle] c_molecules = self.c_skin_atomspace.get_molecules_in_context(c_context)
        
        molecules = []
        for i in range(c_molecules.size()):
            molecules.append(Handle(c_molecules[i].value()))
        
        return molecules
    
    def update_concentrations(self, concentrations):
        """Update molecular concentrations"""
        cdef map[cHandle, double] c_concentrations
        
        for handle, concentration in concentrations.items():
            c_concentrations[deref_handle(handle)] = concentration
            
        self.c_skin_atomspace.update_concentrations(c_concentrations)
    
    def get_atomspace(self):
        """Get the underlying AtomSpace"""
        return self.atomspace

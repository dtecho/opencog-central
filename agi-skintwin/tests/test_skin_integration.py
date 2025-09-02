
#!/usr/bin/env python3
"""
Comprehensive test suite for SkinTwin multiscale modeling system.
"""

import unittest
import numpy as np
from skin_twin.cython_integration import SkinModelInterface, SkinSimulationEngine
from opencog.atomspace import AtomSpace
from opencog.type_constructors import *

class TestSkinModelInterface(unittest.TestCase):
    """Test cases for SkinModelInterface."""
    
    def setUp(self):
        """Set up test environment."""
        self.skin_interface = SkinModelInterface()
    
    def test_molecular_system_creation(self):
        """Test creation of molecular systems."""
        molecules = [
            {'name': 'water', 'formula': 'H2O'},
            {'name': 'ceramide', 'formula': 'C18H35NO3'},
            {'name': 'collagen', 'sequence': 'GLYPROALA', 'type': 'protein'}
        ]
        
        handles = self.skin_interface.create_molecular_system(molecules)
        self.assertEqual(len(handles), 3)
        
        # Verify molecules are in molecular context
        molecular_mols = self.skin_interface.skin_atomspace.get_molecules_in_context("molecular")
        self.assertGreaterEqual(len(molecular_mols), 3)
    
    def test_cellular_population_creation(self):
        """Test creation of cellular populations."""
        cell_specs = [
            {
                'type': 'keratinocyte',
                'count': 10,
                'components': ['nucleus', 'mitochondria']
            },
            {
                'type': 'fibroblast',
                'count': 5,
                'components': ['nucleus', 'endoplasmic_reticulum']
            }
        ]
        
        cell_handles = self.skin_interface.create_cellular_population(cell_specs)
        self.assertEqual(len(cell_handles), 15)
    
    def test_tissue_architecture_creation(self):
        """Test creation of tissue architecture."""
        # First create some cells
        cell_specs = [{'type': 'keratinocyte', 'count': 20}]
        cells = self.skin_interface.create_cellular_population(cell_specs)
        
        # Create tissue architecture
        tissue_specs = [
            {'name': 'epidermis', 'cells': cells[:10]},
            {'name': 'dermis', 'cells': cells[10:]}
        ]
        
        tissues = self.skin_interface.create_tissue_architecture(tissue_specs)
        self.assertEqual(len(tissues), 2)
    
    def test_molecular_interactions(self):
        """Test molecular interaction modeling."""
        # Create molecules
        water = self.skin_interface.skin_atomspace.create_molecule("water", "H2O")
        ceramide = self.skin_interface.skin_atomspace.create_molecule("ceramide", "C18H35NO3")
        
        # Create interaction
        interactions = [
            {
                'molecule1': water,
                'molecule2': ceramide,
                'type': 'hydrogen_bonding'
            }
        ]
        
        interaction_handles = self.skin_interface.model_molecular_interactions(interactions)
        self.assertEqual(len(interaction_handles), 1)
    
    def test_permeation_simulation(self):
        """Test permeation simulation."""
        # Create test molecule and barrier
        molecule = self.skin_interface.skin_atomspace.create_molecule("test_drug", "C12H16N2O")
        barrier = self.skin_interface.atomspace.add_node(ConceptNode, "skin_barrier")
        
        # Run simulation
        concentrations = self.skin_interface.simulate_permeation(molecule, barrier, 50)
        
        self.assertEqual(len(concentrations), 50)
        self.assertGreaterEqual(concentrations[-1], 0)
    
    def test_scale_summary(self):
        """Test scale summary functionality."""
        # Create some molecules first
        molecules = [
            {'name': 'test_mol1', 'formula': 'H2O'},
            {'name': 'test_mol2', 'formula': 'C6H12O6'}
        ]
        self.skin_interface.create_molecular_system(molecules)
        
        # Get summary
        summary = self.skin_interface.get_scale_summary('molecular')
        
        self.assertIn('scale', summary)
        self.assertIn('component_count', summary)
        self.assertEqual(summary['scale'], 'molecular')
        self.assertGreaterEqual(summary['component_count'], 2)

class TestSkinSimulationEngine(unittest.TestCase):
    """Test cases for SkinSimulationEngine."""
    
    def setUp(self):
        """Set up test environment."""
        self.skin_interface = SkinModelInterface()
        self.simulation_engine = SkinSimulationEngine(self.skin_interface)
    
    def test_simulation_initialization(self):
        """Test simulation engine initialization."""
        self.assertEqual(self.simulation_engine.simulation_time, 0.0)
        self.assertEqual(self.simulation_engine.time_step, 0.001)
    
    def test_short_simulation_run(self):
        """Test running a short simulation."""
        # Create minimal system
        molecules = [{'name': 'water', 'formula': 'H2O'}]
        self.skin_interface.create_molecular_system(molecules)
        
        # Run short simulation
        results = self.simulation_engine.run_simulation(0.01, 0.005)
        
        self.assertIn('time_points', results)
        self.assertIn('molecular_data', results)
        self.assertGreater(len(results['time_points']), 0)

class TestIntegrationWithAgiBio(unittest.TestCase):
    """Test integration with agi-bio module."""
    
    def setUp(self):
        """Set up test environment."""
        self.skin_interface = SkinModelInterface()
    
    def test_biological_pathway_integration(self):
        """Test integration with biological pathways."""
        # This would test integration with existing agi-bio functionality
        # For now, we'll test basic compatibility
        
        # Create a simple biological process
        gene = self.skin_interface.atomspace.add_node(GeneNode, "COL1A1")
        protein = self.skin_interface.skin_atomspace.create_protein("collagen_1", "GLYPROALA")
        
        # Create gene-protein relationship
        expression_link = self.skin_interface.atomspace.add_link(
            ExpressionLink, [gene, protein]
        )
        
        self.assertIsNotNone(expression_link)

class TestIntegrationWithCheminformatics(unittest.TestCase):
    """Test integration with cheminformatics module."""
    
    def setUp(self):
        """Set up test environment."""
        self.skin_interface = SkinModelInterface()
    
    def test_chemical_structure_integration(self):
        """Test integration with chemical structures."""
        # Create chemical with SMILES notation
        molecule = self.skin_interface.skin_atomspace.create_molecule("caffeine", "CN1C=NC2=C1C(=O)N(C(=O)N2C)C")
        
        # Verify molecule creation
        self.assertIsNotNone(molecule)
        
        # Test chemical property calculation (placeholder)
        # This would integrate with actual cheminformatics calculations
        properties = {
            'molecular_weight': 194.19,
            'logp': -0.07,
            'tpsa': 58.44
        }
        
        # Store properties in AtomSpace
        for prop_name, value in properties.items():
            prop_node = self.skin_interface.atomspace.add_node(ConceptNode, prop_name)
            value_node = self.skin_interface.atomspace.add_node(NumberNode, str(value))
            
            prop_link = self.skin_interface.atomspace.add_link(
                EvaluationLink, [prop_node, molecule, value_node]
            )
            self.assertIsNotNone(prop_link)

def run_performance_benchmarks():
    """Run performance benchmarks for the system."""
    print("Running SkinTwin Performance Benchmarks...")
    
    interface = SkinModelInterface()
    
    # Benchmark molecular system creation
    import time
    start_time = time.time()
    
    large_molecule_set = [
        {'name': f'molecule_{i}', 'formula': 'C6H12O6'} 
        for i in range(1000)
    ]
    
    handles = interface.create_molecular_system(large_molecule_set)
    creation_time = time.time() - start_time
    
    print(f"Created {len(handles)} molecules in {creation_time:.3f} seconds")
    print(f"Rate: {len(handles)/creation_time:.1f} molecules/second")
    
    # Benchmark cellular population creation
    start_time = time.time()
    
    cell_specs = [
        {'type': 'keratinocyte', 'count': 500},
        {'type': 'fibroblast', 'count': 200}
    ]
    
    cells = interface.create_cellular_population(cell_specs)
    cell_creation_time = time.time() - start_time
    
    print(f"Created {len(cells)} cells in {cell_creation_time:.3f} seconds")
    print(f"Rate: {len(cells)/cell_creation_time:.1f} cells/second")

if __name__ == '__main__':
    # Run unit tests
    unittest.main(verbosity=2, exit=False)
    
    # Run performance benchmarks
    run_performance_benchmarks()

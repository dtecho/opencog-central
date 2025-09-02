
#!/usr/bin/env python3
"""
Test suite for SkinTwin Cython integration
"""

import unittest
import numpy as np
import sys
from pathlib import Path

# Add project paths
project_root = Path(__file__).parent.parent
sys.path.insert(0, str(project_root))

try:
    from skin_twin.cython_integration import SkinModelInterface, SkinSimulationEngine
    CYTHON_AVAILABLE = True
except ImportError:
    CYTHON_AVAILABLE = False

@unittest.skipUnless(CYTHON_AVAILABLE, "Cython integration not available")
class TestCythonIntegration(unittest.TestCase):
    
    def setUp(self):
        """Set up test fixtures"""
        self.skin_interface = SkinModelInterface()
    
    def test_molecular_system_creation(self):
        """Test creation of molecular systems"""
        molecules = [
            {'name': 'water', 'formula': 'H2O'},
            {'name': 'ceramide', 'formula': 'C18H35NO3'},
            {'name': 'collagen', 'sequence': 'GPRGDRGEK', 'type': 'protein'}
        ]
        
        handles = self.skin_interface.create_molecular_system(molecules)
        self.assertEqual(len(handles), 3)
        self.assertTrue(all(handle is not None for handle in handles))
    
    def test_cellular_population_creation(self):
        """Test creation of cellular populations"""
        cell_specs = [
            {
                'type': 'keratinocyte',
                'count': 10,
                'components': ['nucleus', 'keratin_filaments']
            },
            {
                'type': 'fibroblast', 
                'count': 5,
                'components': ['nucleus', 'endoplasmic_reticulum']
            }
        ]
        
        handles = self.skin_interface.create_cellular_population(cell_specs)
        self.assertEqual(len(handles), 15)  # 10 + 5 cells
    
    def test_tissue_architecture_creation(self):
        """Test creation of tissue architecture"""
        # First create some cells
        cell_specs = [{'type': 'keratinocyte', 'count': 20, 'components': ['nucleus']}]
        cell_handles = self.skin_interface.create_cellular_population(cell_specs)
        
        tissue_specs = [
            {'name': 'stratum_corneum', 'cells': cell_handles[:10]},
            {'name': 'stratum_basale', 'cells': cell_handles[10:]}
        ]
        
        tissue_handles = self.skin_interface.create_tissue_architecture(tissue_specs)
        self.assertEqual(len(tissue_handles), 2)
    
    def test_molecular_interactions(self):
        """Test molecular interaction modeling"""
        molecules = [
            {'name': 'water', 'formula': 'H2O'},
            {'name': 'ceramide', 'formula': 'C18H35NO3'}
        ]
        
        mol_handles = self.skin_interface.create_molecular_system(molecules)
        
        interactions = [
            {
                'molecule1': mol_handles[0],
                'molecule2': mol_handles[1], 
                'type': 'hydrogen_bonding'
            }
        ]
        
        interaction_handles = self.skin_interface.model_molecular_interactions(interactions)
        self.assertEqual(len(interaction_handles), 1)
    
    def test_simulation_engine(self):
        """Test simulation engine functionality"""
        # Create a simple system
        molecules = [{'name': 'water', 'formula': 'H2O'}]
        mol_handles = self.skin_interface.create_molecular_system(molecules)
        
        # Initialize simulation engine
        sim_engine = SkinSimulationEngine(self.skin_interface)
        
        # Run short simulation
        results = sim_engine.run_simulation(duration=0.01, output_interval=0.005)
        
        self.assertIn('time_points', results)
        self.assertIn('molecular_data', results)
        self.assertTrue(len(results['time_points']) > 0)
    
    def test_permeation_simulation(self):
        """Test permeation simulation"""
        # Create test system
        molecules = [{'name': 'caffeine', 'formula': 'C8H10N4O2'}]
        mol_handles = self.skin_interface.create_molecular_system(molecules)
        
        if mol_handles:
            test_molecule = mol_handles[0]
            barrier = self.skin_interface.atomspace.add_node("ConceptNode", "skin_barrier")
            
            concentrations = self.skin_interface.simulate_permeation(
                test_molecule, barrier, 10)
            
            self.assertEqual(len(concentrations), 10)
            self.assertTrue(all(isinstance(c, float) for c in concentrations))
    
    def test_model_export_import(self):
        """Test model state export and import"""
        # Create test system
        molecules = [{'name': 'test_mol', 'formula': 'C6H12O6'}]
        self.skin_interface.create_molecular_system(molecules)
        
        # Export model state
        export_file = "test_export.scm"
        success = self.skin_interface.export_model_state(export_file)
        self.assertTrue(success)
        
        # Clean up
        Path(export_file).unlink(missing_ok=True)
    
    def tearDown(self):
        """Clean up after tests"""
        # Reset the skin interface
        self.skin_interface = None

if __name__ == '__main__':
    unittest.main()

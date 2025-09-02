
#!/usr/bin/env python3
"""
Test suite for SkinTwin multiscale modeling
"""

import unittest
import sys
from pathlib import Path

# Add project paths
project_root = Path(__file__).parent.parent
sys.path.insert(0, str(project_root))

from skin_twin.multiscale_model import MultiscaleModel
from skin_twin.atomspace_integration import AtomSpaceManager

class TestMultiscaleModel(unittest.TestCase):
    
    def setUp(self):
        """Set up test fixtures"""
        self.atomspace_manager = AtomSpaceManager()
        self.multiscale_model = MultiscaleModel(self.atomspace_manager)
    
    def test_model_initialization(self):
        """Test multiscale model initialization"""
        self.assertIsNotNone(self.multiscale_model)
        self.assertIsNotNone(self.multiscale_model.atomspace_manager)
    
    def test_scale_integration(self):
        """Test integration across scales"""
        # Test molecular to cellular scale transition
        molecular_data = {
            'molecules': ['water', 'ceramide', 'cholesterol'],
            'concentrations': [0.6, 0.2, 0.2]
        }
        
        cellular_result = self.multiscale_model.molecular_to_cellular(molecular_data)
        self.assertIsInstance(cellular_result, dict)
        self.assertIn('cell_states', cellular_result)
    
    def test_tissue_modeling(self):
        """Test tissue-level modeling"""
        tissue_params = {
            'layers': ['stratum_corneum', 'stratum_granulosum', 'stratum_basale'],
            'thickness': [0.02, 0.05, 0.03],  # mm
            'cell_density': [1000, 800, 1200]  # cells/mm³
        }
        
        tissue_model = self.multiscale_model.create_tissue_model(tissue_params)
        self.assertIsInstance(tissue_model, dict)
        self.assertIn('layers', tissue_model)
    
    def test_temporal_dynamics(self):
        """Test temporal evolution of skin model"""
        initial_state = self.multiscale_model.get_current_state()
        
        # Simulate time step
        dt = 0.1  # seconds
        final_state = self.multiscale_model.evolve_state(initial_state, dt)
        
        self.assertIsInstance(final_state, dict)
        self.assertIn('time', final_state)
        self.assertEqual(final_state['time'], dt)
    
    def test_permeation_modeling(self):
        """Test molecular permeation through skin layers"""
        molecule_props = {
            'molecular_weight': 194.19,  # caffeine
            'logP': -0.07,
            'hydrogen_bonds': 3
        }
        
        permeation_data = self.multiscale_model.model_permeation(molecule_props)
        self.assertIsInstance(permeation_data, dict)
        self.assertIn('flux', permeation_data)
        self.assertIn('concentration_profile', permeation_data)
    
    def test_mechanical_properties(self):
        """Test mechanical property modeling"""
        mechanical_params = {
            'elastic_modulus': 1e6,  # Pa
            'strain_rate': 0.01,     # s⁻¹
            'temperature': 310.15    # K
        }
        
        response = self.multiscale_model.calculate_mechanical_response(mechanical_params)
        self.assertIsInstance(response, dict)
        self.assertIn('stress', response)
        self.assertIn('strain', response)

if __name__ == '__main__':
    unittest.main()

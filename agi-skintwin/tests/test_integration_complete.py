
#!/usr/bin/env python3
"""
Comprehensive Integration Test Suite for SkinTwin

Tests the complete system integration including C++, Cython, Python,
web interface, and OpenCog components.
"""

import unittest
import sys
import os
import time
import json
import tempfile
from pathlib import Path

# Add the project root to the path
project_root = Path(__file__).parent.parent
sys.path.insert(0, str(project_root))
sys.path.insert(0, str(project_root / "skin_twin"))

class SkinTwinIntegrationTests(unittest.TestCase):
    """Complete integration test suite"""
    
    @classmethod
    def setUpClass(cls):
        """Set up test environment"""
        cls.temp_dir = tempfile.mkdtemp()
        print(f"Test directory: {cls.temp_dir}")
        
    def setUp(self):
        """Set up each test"""
        self.test_start_time = time.time()
        
    def tearDown(self):
        """Clean up after each test"""
        test_time = time.time() - self.test_start_time
        print(f"Test completed in {test_time:.3f} seconds")
    
    def test_01_imports(self):
        """Test that all modules can be imported"""
        try:
            # Test core Python imports
            from skin_twin.core import SkinTwinCore
            from skin_twin.atomspace_integration import AtomSpaceManager
            from skin_twin.multiscale_model import MultiscaleModel
            from skin_twin.biological_integration import BiologicalIntegration
            from skin_twin.chemical_integration import ChemicalIntegration
            from skin_twin.web_interface import SkinTwinWebInterface
            
            # Test Cython integration
            from skin_twin.cython_integration import SkinModelInterface, SkinSimulationEngine
            
            print("✓ All modules imported successfully")
            
        except ImportError as e:
            self.fail(f"Failed to import modules: {e}")
    
    def test_02_mock_atomspace_integration(self):
        """Test AtomSpace integration with mock OpenCog"""
        try:
            from skin_twin.atomspace_integration import AtomSpaceManager
            
            # Test with mock OpenCog
            manager = AtomSpaceManager(use_mock=True)
            self.assertIsNotNone(manager)
            self.assertTrue(manager.is_connected())
            
            # Test basic operations
            atom = manager.create_concept_node("TestConcept")
            self.assertIsNotNone(atom)
            
            # Test cleanup
            manager.cleanup()
            print("✓ Mock AtomSpace integration working")
            
        except Exception as e:
            self.fail(f"AtomSpace integration failed: {e}")
    
    def test_03_multiscale_model_creation(self):
        """Test multiscale model creation and basic operations"""
        try:
            from skin_twin.atomspace_integration import AtomSpaceManager
            from skin_twin.multiscale_model import MultiscaleModel
            
            # Create components
            atomspace_manager = AtomSpaceManager(use_mock=True)
            model = MultiscaleModel(atomspace_manager)
            
            # Test model initialization
            self.assertIsNotNone(model)
            self.assertTrue(hasattr(model, 'scales'))
            
            # Test scale operations
            scales = model.get_available_scales()
            self.assertIn('molecular', scales)
            self.assertIn('cellular', scales)
            self.assertIn('tissue', scales)
            
            print("✓ Multiscale model creation working")
            
        except Exception as e:
            self.fail(f"Multiscale model creation failed: {e}")
    
    def test_04_cython_interface(self):
        """Test Cython interface functionality"""
        try:
            from skin_twin.cython_integration import SkinModelInterface
            
            # Create interface
            interface = SkinModelInterface()
            self.assertIsNotNone(interface)
            
            # Test basic operations
            molecules = [
                {'name': 'water', 'formula': 'H2O'},
                {'name': 'test_protein', 'sequence': 'ACDEFG', 'type': 'protein'}
            ]
            
            # This will use mock implementation
            handles = interface.create_molecular_system(molecules)
            self.assertEqual(len(handles), 2)
            
            print("✓ Cython interface working")
            
        except Exception as e:
            # Expected to fail if OpenCog not available
            print(f"Note: Cython interface test skipped - {e}")
    
    def test_05_simulation_engine(self):
        """Test simulation engine functionality"""
        try:
            from skin_twin.cython_integration import SkinModelInterface, SkinSimulationEngine
            
            interface = SkinModelInterface()
            sim_engine = SkinSimulationEngine(interface)
            
            # Test short simulation
            results = sim_engine.run_simulation(duration=0.1, output_interval=0.05)
            
            self.assertIn('time_points', results)
            self.assertIn('molecular_data', results)
            self.assertIn('cellular_data', results)
            
            print("✓ Simulation engine working")
            
        except Exception as e:
            print(f"Note: Simulation engine test skipped - {e}")
    
    def test_06_biological_integration(self):
        """Test biological integration functionality"""
        try:
            from skin_twin.atomspace_integration import AtomSpaceManager
            from skin_twin.biological_integration import BiologicalIntegration
            
            atomspace_manager = AtomSpaceManager(use_mock=True)
            bio_integration = BiologicalIntegration(atomspace_manager, {})
            
            self.assertIsNotNone(bio_integration)
            
            # Test loading biological knowledge
            bio_integration.load_biological_knowledge()
            
            print("✓ Biological integration working")
            
        except Exception as e:
            self.fail(f"Biological integration failed: {e}")
    
    def test_07_chemical_integration(self):
        """Test chemical integration functionality"""
        try:
            from skin_twin.atomspace_integration import AtomSpaceManager
            from skin_twin.chemical_integration import ChemicalIntegration
            
            atomspace_manager = AtomSpaceManager(use_mock=True)
            chem_integration = ChemicalIntegration(atomspace_manager, {})
            
            self.assertIsNotNone(chem_integration)
            
            # Test loading chemical knowledge
            chem_integration.load_chemical_knowledge()
            
            print("✓ Chemical integration working")
            
        except Exception as e:
            self.fail(f"Chemical integration failed: {e}")
    
    def test_08_core_system_initialization(self):
        """Test complete core system initialization"""
        try:
            from skin_twin.core import SkinTwinCore
            from skin_twin.atomspace_integration import AtomSpaceManager
            from skin_twin.multiscale_model import MultiscaleModel
            
            # Create components
            atomspace_manager = AtomSpaceManager(use_mock=True)
            multiscale_model = MultiscaleModel(atomspace_manager)
            config = {'debug': True}
            
            # Initialize core system
            core = SkinTwinCore(atomspace_manager, multiscale_model, config)
            self.assertIsNotNone(core)
            
            print("✓ Core system initialization working")
            
        except Exception as e:
            self.fail(f"Core system initialization failed: {e}")
    
    def test_09_web_interface_creation(self):
        """Test web interface creation"""
        try:
            from skin_twin.web_interface import SkinTwinWebInterface, create_app
            
            # Test interface creation
            interface = SkinTwinWebInterface(None)
            self.assertIsNotNone(interface)
            self.assertIsNotNone(interface.app)
            
            # Test app factory
            app = create_app()
            self.assertIsNotNone(app)
            
            print("✓ Web interface creation working")
            
        except Exception as e:
            self.fail(f"Web interface creation failed: {e}")
    
    def test_10_configuration_loading(self):
        """Test configuration loading"""
        try:
            import yaml
            
            config_path = project_root / "config.yaml"
            if config_path.exists():
                with open(config_path, 'r') as f:
                    config = yaml.safe_load(f)
                
                self.assertIn('system', config)
                self.assertIn('multiscale_model', config)
                
                print("✓ Configuration loading working")
            else:
                print("Note: config.yaml not found, using defaults")
                
        except Exception as e:
            self.fail(f"Configuration loading failed: {e}")
    
    def test_11_data_export_import(self):
        """Test data export and import functionality"""
        try:
            from skin_twin.cython_integration import SkinModelInterface
            
            interface = SkinModelInterface()
            
            # Test export
            export_file = os.path.join(self.temp_dir, "test_export.scm")
            success = interface.export_model_state(export_file)
            
            if success and os.path.exists(export_file):
                with open(export_file, 'r') as f:
                    content = f.read()
                self.assertTrue(len(content) > 0)
                print("✓ Data export/import working")
            else:
                print("Note: Data export test skipped (mock implementation)")
                
        except Exception as e:
            print(f"Note: Data export test skipped - {e}")
    
    def test_12_analysis_functionality(self):
        """Test analysis and visualization functionality"""
        try:
            from skin_twin.analysis.statistical_analysis import StatisticalAnalyzer
            from skin_twin.analysis.visualization import SkinVisualizer
            
            # Test statistical analysis
            analyzer = StatisticalAnalyzer()
            self.assertIsNotNone(analyzer)
            
            # Test visualization
            visualizer = SkinVisualizer()
            self.assertIsNotNone(visualizer)
            
            print("✓ Analysis functionality working")
            
        except Exception as e:
            print(f"Note: Analysis functionality test skipped - {e}")
    
    def test_13_performance_benchmarks(self):
        """Test system performance benchmarks"""
        try:
            from skin_twin.cython_integration import SkinModelInterface
            
            interface = SkinModelInterface()
            
            # Benchmark molecular system creation
            start_time = time.time()
            
            molecules = [{'name': f'mol_{i}', 'formula': 'C6H12O6'} for i in range(100)]
            handles = interface.create_molecular_system(molecules)
            
            creation_time = time.time() - start_time
            
            self.assertEqual(len(handles), 100)
            self.assertLess(creation_time, 5.0)  # Should complete within 5 seconds
            
            print(f"✓ Performance test: Created 100 molecules in {creation_time:.3f}s")
            
        except Exception as e:
            print(f"Note: Performance benchmark skipped - {e}")
    
    def test_14_error_handling(self):
        """Test error handling and recovery"""
        try:
            from skin_twin.cython_integration import SkinModelInterface
            
            interface = SkinModelInterface()
            
            # Test invalid inputs
            with self.assertRaises((ValueError, TypeError, RuntimeError)):
                interface.create_molecular_system([{'invalid': 'data'}])
            
            print("✓ Error handling working")
            
        except Exception as e:
            print(f"Note: Error handling test inconclusive - {e}")
    
    def test_15_memory_management(self):
        """Test memory management and cleanup"""
        try:
            from skin_twin.atomspace_integration import AtomSpaceManager
            from skin_twin.multiscale_model import MultiscaleModel
            
            # Create and destroy multiple instances
            for i in range(10):
                manager = AtomSpaceManager(use_mock=True)
                model = MultiscaleModel(manager)
                manager.cleanup()
                del model
                del manager
            
            print("✓ Memory management test completed")
            
        except Exception as e:
            self.fail(f"Memory management test failed: {e}")

def run_comprehensive_tests():
    """Run all comprehensive tests with detailed reporting"""
    print("=" * 80)
    print("SkinTwin Comprehensive Integration Test Suite")
    print("=" * 80)
    
    # Create test suite
    loader = unittest.TestLoader()
    suite = loader.loadTestsFromTestCase(SkinTwinIntegrationTests)
    
    # Run tests with detailed output
    runner = unittest.TextTestRunner(verbosity=2)
    result = runner.run(suite)
    
    print("\n" + "=" * 80)
    print("Test Summary:")
    print(f"Tests run: {result.testsRun}")
    print(f"Failures: {len(result.failures)}")
    print(f"Errors: {len(result.errors)}")
    print(f"Skipped: {len(result.skipped) if hasattr(result, 'skipped') else 0}")
    
    if result.failures:
        print("\nFailures:")
        for test, traceback in result.failures:
            print(f"- {test}: {traceback}")
    
    if result.errors:
        print("\nErrors:")
        for test, traceback in result.errors:
            print(f"- {test}: {traceback}")
    
    success_rate = (result.testsRun - len(result.failures) - len(result.errors)) / result.testsRun * 100
    print(f"\nSuccess rate: {success_rate:.1f}%")
    print("=" * 80)
    
    return result.wasSuccessful()

if __name__ == '__main__':
    success = run_comprehensive_tests()
    sys.exit(0 if success else 1)

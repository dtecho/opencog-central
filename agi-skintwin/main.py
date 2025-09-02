
#!/usr/bin/env python3
"""
SkinTwin-ASI: Comprehensive Skin Modeling System
Main entry point for the multiscale computational skin model
"""

import sys
import os
import logging
from pathlib import Path

# Add project paths
project_root = Path(__file__).parent
sys.path.insert(0, str(project_root / "agi-bio"))
sys.path.insert(0, str(project_root / "cheminformatics"))

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)

def main():
    """Main entry point for SkinTwin-ASI system"""
    logger = logging.getLogger(__name__)
    logger.info("Initializing SkinTwin-ASI Comprehensive Skin Modeling System")
    
    try:
        # Load configuration
        import yaml
        config_path = project_root / "config.yaml"
        
        if config_path.exists():
            with open(config_path, 'r') as f:
                config = yaml.safe_load(f)
            logger.info("Configuration loaded from config.yaml")
        else:
            config = {}
            logger.warning("config.yaml not found, using default configuration")
        
        # Import core modules
        from skin_twin.core import SkinTwinCore
        from skin_twin.atomspace_integration import AtomSpaceManager
        from skin_twin.multiscale_model import MultiscaleModel
        
        # Initialize core system
        logger.info("Starting AtomSpace integration...")
        atomspace_manager = AtomSpaceManager()
        
        logger.info("Initializing multiscale skin model...")
        multiscale_model = MultiscaleModel(atomspace_manager)
        
        logger.info("Starting SkinTwin core system...")
        skin_twin = SkinTwinCore(atomspace_manager, multiscale_model, config)
        
        # Start the system
        skin_twin.start()
        
        # Keep the system running
        logger.info("SkinTwin-ASI system is running. Access web interface at http://localhost:5000")
        
        try:
            # Keep main thread alive
            while skin_twin.is_running:
                import time
                time.sleep(1)
        except KeyboardInterrupt:
            logger.info("Shutdown requested by user")
            skin_twin.stop()
        
    except ImportError as e:
        logger.error(f"Missing dependencies: {e}")
        logger.info("Please ensure OpenCog AtomSpace and related components are installed")
        sys.exit(1)
    except Exception as e:
        logger.error(f"System initialization failed: {e}")
        sys.exit(1)

if __name__ == "__main__":
    main()
#!/usr/bin/env python3
"""
SkinTwin: Multiscale Computational Skin Model

This is the main entry point for the SkinTwin system, providing a comprehensive
multiscale computational model of human skin that integrates biological and
chemical data within the OpenCog AtomSpace framework.
"""

import sys
import os
import logging
import argparse
from pathlib import Path

# Add the skin_twin module to path
sys.path.insert(0, str(Path(__file__).parent / "skin_twin"))

from skin_twin.cython_integration import SkinModelInterface, SkinSimulationEngine
from skin_twin.web_interface import create_app

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)

def create_example_skin_model():
    """Create an example skin model for demonstration."""
    logger.info("Creating example skin model...")
    
    # Initialize skin modeling interface
    skin_interface = SkinModelInterface()
    
    # Create molecular system
    logger.info("Creating molecular system...")
    molecules = [
        {'name': 'water', 'formula': 'H2O'},
        {'name': 'ceramide_ns', 'formula': 'C18H35NO3'},
        {'name': 'cholesterol', 'formula': 'C27H46O'},
        {'name': 'palmitic_acid', 'formula': 'C16H32O2'},
        {'name': 'collagen_1', 'sequence': 'GLYPROALAHYPPROARGGLUPRO', 'type': 'protein'},
        {'name': 'elastin', 'sequence': 'VPGVGVPGVGVPGFGVGAG', 'type': 'protein'},
        {'name': 'keratin_14', 'sequence': 'SCCPRRGGSRGGGY', 'type': 'protein'}
    ]
    
    molecule_handles = skin_interface.create_molecular_system(molecules)
    logger.info(f"Created {len(molecule_handles)} molecules")
    
    # Create cellular populations
    logger.info("Creating cellular populations...")
    cell_specs = [
        {
            'type': 'keratinocyte',
            'count': 100,
            'components': ['nucleus', 'mitochondria', 'keratin_filaments']
        },
        {
            'type': 'fibroblast',
            'count': 50,
            'components': ['nucleus', 'endoplasmic_reticulum', 'golgi_apparatus']
        },
        {
            'type': 'melanocyte',
            'count': 15,
            'components': ['nucleus', 'melanosomes']
        }
    ]
    
    cell_handles = skin_interface.create_cellular_population(cell_specs)
    logger.info(f"Created {len(cell_handles)} cells")
    
    # Create tissue architecture
    logger.info("Creating tissue architecture...")
    tissue_specs = [
        {'name': 'stratum_corneum', 'cells': cell_handles[:20]},
        {'name': 'stratum_granulosum', 'cells': cell_handles[20:40]},
        {'name': 'stratum_spinosum', 'cells': cell_handles[40:80]},
        {'name': 'stratum_basale', 'cells': cell_handles[80:100]},
        {'name': 'papillary_dermis', 'cells': cell_handles[100:125]},
        {'name': 'reticular_dermis', 'cells': cell_handles[125:]}
    ]
    
    tissue_handles = skin_interface.create_tissue_architecture(tissue_specs)
    logger.info(f"Created {len(tissue_handles)} tissue layers")
    
    # Model molecular interactions
    logger.info("Modeling molecular interactions...")
    if len(molecule_handles) >= 2:
        interactions = [
            {
                'molecule1': molecule_handles[0],  # water
                'molecule2': molecule_handles[1],  # ceramide
                'type': 'hydrogen_bonding'
            },
            {
                'molecule1': molecule_handles[2],  # cholesterol
                'molecule2': molecule_handles[3],  # palmitic_acid
                'type': 'hydrophobic_interaction'
            }
        ]
        
        interaction_handles = skin_interface.model_molecular_interactions(interactions)
        logger.info(f"Created {len(interaction_handles)} molecular interactions")
    
    return skin_interface

def run_simulation_demo(skin_interface):
    """Run a demonstration simulation."""
    logger.info("Running simulation demo...")
    
    # Initialize simulation engine
    sim_engine = SkinSimulationEngine(skin_interface)
    
    # Run short simulation
    logger.info("Starting multiscale simulation...")
    results = sim_engine.run_simulation(duration=0.1, output_interval=0.02)
    
    # Display results
    logger.info("Simulation completed!")
    logger.info(f"Time points simulated: {len(results['time_points'])}")
    logger.info(f"Final time: {results['time_points'][-1]:.4f} seconds")
    
    # Show molecular data summary
    if results['molecular_data']:
        final_mol_data = results['molecular_data'][-1]
        logger.info(f"Final molecular components: {final_mol_data['component_count']}")
    
    # Show cellular data summary
    if results['cellular_data']:
        final_cell_data = results['cellular_data'][-1]
        logger.info(f"Final cellular components: {final_cell_data['component_count']}")
    
    return results

def run_permeation_analysis(skin_interface):
    """Run permeation analysis demonstration."""
    logger.info("Running permeation analysis...")
    
    # Create test molecule (caffeine as example)
    test_molecule = skin_interface.skin_atomspace.create_molecule("caffeine", "CN1C=NC2=C1C(=O)N(C(=O)N2C)C")
    barrier = skin_interface.atomspace.add_node(ConceptNode, "stratum_corneum_barrier")
    
    # Simulate permeation
    concentrations = skin_interface.simulate_permeation(test_molecule, barrier, 100)
    
    logger.info(f"Permeation simulation completed")
    logger.info(f"Initial concentration: {concentrations[0]:.6f}")
    logger.info(f"Final concentration: {concentrations[-1]:.6f}")
    logger.info(f"Peak concentration: {np.max(concentrations):.6f}")
    
    return concentrations

def export_model_data(skin_interface, output_dir="output"):
    """Export model data for analysis."""
    logger.info("Exporting model data...")
    
    # Create output directory
    Path(output_dir).mkdir(exist_ok=True)
    
    # Export model state
    model_file = Path(output_dir) / "skin_model_state.scm"
    success = skin_interface.export_model_state(str(model_file))
    
    if success:
        logger.info(f"Model state exported to {model_file}")
    else:
        logger.error("Failed to export model state")
    
    # Export scale summaries
    for scale in ['molecular', 'cellular', 'tissue', 'organ']:
        summary = skin_interface.get_scale_summary(scale)
        summary_file = Path(output_dir) / f"{scale}_summary.txt"
        
        with open(summary_file, 'w') as f:
            for key, value in summary.items():
                f.write(f"{key}: {value}\n")
        
        logger.info(f"Scale summary exported to {summary_file}")

def main():
    """Main application entry point."""
    parser = argparse.ArgumentParser(description="SkinTwin: Multiscale Skin Modeling System")
    parser.add_argument("--demo", action="store_true", help="Run demonstration")
    parser.add_argument("--simulation", action="store_true", help="Run simulation demo")
    parser.add_argument("--permeation", action="store_true", help="Run permeation analysis")
    parser.add_argument("--web", action="store_true", help="Start web interface")
    parser.add_argument("--export", action="store_true", help="Export model data")
    parser.add_argument("--output-dir", default="output", help="Output directory for exports")
    
    args = parser.parse_args()
    
    logger.info("SkinTwin: Multiscale Computational Skin Model")
    logger.info("=" * 50)
    
    try:
        # Create example skin model
        skin_interface = create_example_skin_model()
        
        if args.demo or not any(vars(args).values()):
            logger.info("Running full demonstration...")
            results = run_simulation_demo(skin_interface)
            concentrations = run_permeation_analysis(skin_interface)
            export_model_data(skin_interface, args.output_dir)
        
        if args.simulation:
            run_simulation_demo(skin_interface)
        
        if args.permeation:
            run_permeation_analysis(skin_interface)
        
        if args.export:
            export_model_data(skin_interface, args.output_dir)
        
        if args.web:
            logger.info("Starting web interface...")
            app = create_app(skin_interface)
            app.run(host='0.0.0.0', port=5000, debug=True)
        
        logger.info("SkinTwin execution completed successfully!")
        
    except Exception as e:
        logger.error(f"Error during execution: {e}")
        sys.exit(1)

if __name__ == "__main__":
    main()

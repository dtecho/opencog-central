
#!/usr/bin/env python3
"""
SkinTwin Basic Modeling Example

Demonstrates basic usage of the SkinTwin multiscale skin modeling system.
"""

import sys
import logging
from pathlib import Path

# Add project path
project_root = Path(__file__).parent.parent
sys.path.insert(0, str(project_root))

from skin_twin.cython_integration import SkinModelInterface, SkinSimulationEngine
from skin_twin.analysis.statistical_analysis import StatisticalAnalyzer
from skin_twin.analysis.visualization import SkinVisualizer

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

def create_basic_skin_model():
    """Create a basic skin model with molecular and cellular components"""
    logger.info("Creating basic skin model...")
    
    # Initialize the skin modeling interface
    skin_interface = SkinModelInterface()
    
    # Create molecular system with key skin components
    molecules = [
        {'name': 'water', 'formula': 'H2O'},
        {'name': 'ceramide_ns', 'formula': 'C18H35NO3'},
        {'name': 'cholesterol', 'formula': 'C27H46O'},
        {'name': 'palmitic_acid', 'formula': 'C16H32O2'},
        {'name': 'collagen_1', 'sequence': 'GLYPROALAHYPPROARGGLUPRO', 'type': 'protein'},
        {'name': 'keratin_14', 'sequence': 'SCCPRRGGSRGGGY', 'type': 'protein'}
    ]
    
    logger.info(f"Creating {len(molecules)} molecular components...")
    molecule_handles = skin_interface.create_molecular_system(molecules)
    logger.info(f"Created {len(molecule_handles)} molecular components")
    
    # Create cellular populations
    cell_specs = [
        {
            'type': 'keratinocyte',
            'count': 50,
            'components': ['nucleus', 'mitochondria', 'keratin_filaments']
        },
        {
            'type': 'fibroblast',
            'count': 25,
            'components': ['nucleus', 'endoplasmic_reticulum', 'golgi_apparatus']
        },
        {
            'type': 'melanocyte',
            'count': 10,
            'components': ['nucleus', 'melanosomes']
        }
    ]
    
    logger.info(f"Creating cellular populations...")
    cell_handles = skin_interface.create_cellular_population(cell_specs)
    logger.info(f"Created {len(cell_handles)} cells")
    
    # Create tissue architecture
    tissue_specs = [
        {'name': 'stratum_corneum', 'cells': cell_handles[:15]},
        {'name': 'stratum_granulosum', 'cells': cell_handles[15:30]},
        {'name': 'stratum_spinosum', 'cells': cell_handles[30:60]},
        {'name': 'stratum_basale', 'cells': cell_handles[60:75]},
        {'name': 'papillary_dermis', 'cells': cell_handles[75:]}
    ]
    
    logger.info("Creating tissue architecture...")
    tissue_handles = skin_interface.create_tissue_architecture(tissue_specs)
    logger.info(f"Created {len(tissue_handles)} tissue layers")
    
    # Model molecular interactions
    if len(molecule_handles) >= 4:
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
        
        logger.info("Modeling molecular interactions...")
        interaction_handles = skin_interface.model_molecular_interactions(interactions)
        logger.info(f"Created {len(interaction_handles)} molecular interactions")
    
    return skin_interface

def run_basic_simulation(skin_interface):
    """Run a basic simulation demonstration"""
    logger.info("Running basic simulation...")
    
    # Initialize simulation engine
    sim_engine = SkinSimulationEngine(skin_interface)
    
    # Run simulation
    logger.info("Starting multiscale simulation...")
    results = sim_engine.run_simulation(duration=0.05, output_interval=0.01)
    
    logger.info("Simulation completed!")
    logger.info(f"Time points simulated: {len(results['time_points'])}")
    logger.info(f"Final time: {results['time_points'][-1]:.4f} seconds")
    
    return results

def analyze_results(results):
    """Analyze simulation results"""
    logger.info("Analyzing simulation results...")
    
    # Initialize analyzer
    analyzer = StatisticalAnalyzer()
    
    # Analyze molecular dynamics
    if results.get('molecular_data'):
        mol_analysis = analyzer.analyze_molecular_dynamics(results['molecular_data'])
        logger.info("Molecular dynamics analysis completed")
    
    # Analyze cellular behavior
    if results.get('cellular_data'):
        cell_analysis = analyzer.analyze_cellular_behavior(results['cellular_data'])
        logger.info("Cellular behavior analysis completed")
    
    # Generate summary report
    all_data = {
        'molecular': results.get('molecular_data', {}),
        'cellular': results.get('cellular_data', {}),
        'simulation_params': results.get('simulation_params', {})
    }
    
    summary_report = analyzer.generate_summary_report(all_data)
    logger.info("Summary report generated")
    
    return summary_report

def visualize_results(results, analysis):
    """Create visualizations of results"""
    logger.info("Creating visualizations...")
    
    # Initialize visualizer
    visualizer = SkinVisualizer()
    
    # Create molecular concentration plots
    if results.get('molecular_data'):
        mol_plot = visualizer.plot_molecular_concentrations(
            results['molecular_data'], 
            results.get('time_points')
        )
    
    # Create cellular population plots
    if results.get('cellular_data'):
        cell_plot = visualizer.plot_cellular_populations(results['cellular_data'])
    
    # Create multiscale overview
    overview_plot = visualizer.plot_multiscale_overview({
        'molecular': results.get('molecular_data', {}),
        'cellular': results.get('cellular_data', {})
    })
    
    logger.info("Visualizations created and saved to output/plots/")

def main():
    """Main execution function"""
    logger.info("Starting SkinTwin basic modeling example")
    
    try:
        # Create basic skin model
        skin_interface = create_basic_skin_model()
        
        # Run simulation
        results = run_basic_simulation(skin_interface)
        
        # Analyze results
        analysis = analyze_results(results)
        
        # Create visualizations
        visualize_results(results, analysis)
        
        logger.info("Basic modeling example completed successfully!")
        logger.info("Check the 'output/' directory for results and visualizations")
        
    except Exception as e:
        logger.error(f"Example failed: {e}")
        sys.exit(1)

if __name__ == "__main__":
    main()

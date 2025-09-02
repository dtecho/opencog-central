
"""
Visualization Tools for SkinTwin

Provides comprehensive visualization capabilities for multiscale skin modeling data.
"""

import matplotlib.pyplot as plt
import plotly.graph_objects as go
import plotly.express as px
from plotly.subplots import make_subplots
import numpy as np
import pandas as pd
import logging

logger = logging.getLogger(__name__)

class SkinVisualizer:
    """Visualization tools for skin model data"""
    
    def __init__(self, output_dir="output/plots"):
        self.output_dir = output_dir
        self._ensure_output_dir()
    
    def _ensure_output_dir(self):
        """Ensure output directory exists"""
        from pathlib import Path
        Path(self.output_dir).mkdir(parents=True, exist_ok=True)
    
    def plot_molecular_concentrations(self, molecular_data, time_points=None, save=True):
        """Plot molecular concentration profiles"""
        if not molecular_data:
            return None
        
        fig = go.Figure()
        
        if isinstance(molecular_data, dict):
            # Single time point
            molecules = list(molecular_data.keys())
            concentrations = list(molecular_data.values())
            
            fig.add_trace(go.Bar(
                x=molecules,
                y=concentrations,
                name='Concentrations'
            ))
            
            fig.update_layout(
                title='Molecular Concentrations',
                xaxis_title='Molecule',
                yaxis_title='Concentration'
            )
        
        elif isinstance(molecular_data, list) and time_points is not None:
            # Time series data
            for i, molecule_name in enumerate(molecular_data[0].keys() if molecular_data else []):
                concentrations = [data.get(molecule_name, 0) for data in molecular_data]
                
                fig.add_trace(go.Scatter(
                    x=time_points,
                    y=concentrations,
                    mode='lines+markers',
                    name=molecule_name
                ))
            
            fig.update_layout(
                title='Molecular Concentration Dynamics',
                xaxis_title='Time (s)',
                yaxis_title='Concentration'
            )
        
        if save:
            output_path = f"{self.output_dir}/molecular_concentrations.html"
            fig.write_html(output_path)
            logger.info(f"Molecular concentration plot saved to {output_path}")
        
        return fig
    
    def plot_cellular_populations(self, cellular_data, save=True):
        """Plot cellular population dynamics"""
        if not cellular_data:
            return None
        
        fig = make_subplots(
            rows=2, cols=2,
            subplot_titles=('Cell Counts', 'Viability', 'Growth Rate', 'Distribution'),
            specs=[[{"secondary_y": True}, {"secondary_y": False}],
                   [{"secondary_y": False}, {"type": "pie"}]]
        )
        
        # Extract data
        if isinstance(cellular_data, list):
            time_points = list(range(len(cellular_data)))
            cell_counts = [data.get('component_count', 0) for data in cellular_data]
            
            # Cell counts over time
            fig.add_trace(
                go.Scatter(x=time_points, y=cell_counts, name='Cell Count'),
                row=1, col=1
            )
        
        if save:
            output_path = f"{self.output_dir}/cellular_populations.html"
            fig.write_html(output_path)
            logger.info(f"Cellular population plot saved to {output_path}")
        
        return fig
    
    def plot_tissue_architecture(self, tissue_data, save=True):
        """Plot tissue architecture and properties"""
        if not tissue_data:
            return None
        
        fig = make_subplots(
            rows=2, cols=2,
            subplot_titles=('Layer Thickness', 'Cell Density', 'Mechanical Properties', 'Barrier Function')
        )
        
        # Sample tissue layer data
        layers = ['Stratum Corneum', 'Stratum Granulosum', 'Stratum Spinosum', 'Stratum Basale']
        thickness = [0.02, 0.05, 0.08, 0.03]  # mm
        density = [1000, 800, 1200, 1500]     # cells/mm³
        
        # Layer thickness
        fig.add_trace(
            go.Bar(x=layers, y=thickness, name='Thickness (mm)'),
            row=1, col=1
        )
        
        # Cell density
        fig.add_trace(
            go.Bar(x=layers, y=density, name='Density (cells/mm³)'),
            row=1, col=2
        )
        
        # Mechanical properties (sample data)
        elastic_modulus = [1e6, 0.8e6, 0.6e6, 0.4e6]  # Pa
        fig.add_trace(
            go.Scatter(x=layers, y=elastic_modulus, mode='lines+markers', 
                      name='Elastic Modulus (Pa)'),
            row=2, col=1
        )
        
        # Barrier function (sample data)
        permeability = [1e-8, 5e-7, 1e-6, 2e-6]  # cm/s
        fig.add_trace(
            go.Scatter(x=layers, y=permeability, mode='lines+markers',
                      name='Permeability (cm/s)'),
            row=2, col=2
        )
        
        fig.update_layout(height=800, title_text="Tissue Architecture Analysis")
        
        if save:
            output_path = f"{self.output_dir}/tissue_architecture.html"
            fig.write_html(output_path)
            logger.info(f"Tissue architecture plot saved to {output_path}")
        
        return fig
    
    def plot_permeation_profile(self, concentrations, time_points=None, depths=None, save=True):
        """Plot molecular permeation profiles"""
        if not concentrations:
            return None
        
        fig = go.Figure()
        
        conc_array = np.array(concentrations)
        
        if time_points is not None:
            # Time-dependent permeation
            fig.add_trace(go.Scatter(
                x=time_points,
                y=conc_array,
                mode='lines+markers',
                name='Concentration'
            ))
            
            fig.update_layout(
                title='Permeation Profile Over Time',
                xaxis_title='Time (s)',
                yaxis_title='Concentration'
            )
        
        elif depths is not None:
            # Depth-dependent concentration
            fig.add_trace(go.Scatter(
                x=depths,
                y=conc_array,
                mode='lines+markers',
                name='Concentration'
            ))
            
            fig.update_layout(
                title='Concentration Profile vs Depth',
                xaxis_title='Depth (μm)',
                yaxis_title='Concentration'
            )
        
        if save:
            output_path = f"{self.output_dir}/permeation_profile.html"
            fig.write_html(output_path)
            logger.info(f"Permeation profile plot saved to {output_path}")
        
        return fig
    
    def plot_multiscale_overview(self, all_data, save=True):
        """Create comprehensive multiscale overview plot"""
        fig = make_subplots(
            rows=3, cols=2,
            subplot_titles=('Molecular Scale', 'Cellular Scale', 'Tissue Scale',
                          'Interactions', 'Dynamics', 'Summary'),
            vertical_spacing=0.08
        )
        
        # Molecular scale visualization
        if 'molecular' in all_data:
            mol_data = all_data['molecular']
            if isinstance(mol_data, dict):
                molecules = list(mol_data.keys())[:5]  # Top 5
                values = list(mol_data.values())[:5]
                
                fig.add_trace(
                    go.Bar(x=molecules, y=values, name='Molecular'),
                    row=1, col=1
                )
        
        # Cellular scale visualization
        if 'cellular' in all_data:
            cell_data = all_data['cellular']
            if isinstance(cell_data, list) and cell_data:
                counts = [data.get('component_count', 0) for data in cell_data]
                time_points = list(range(len(counts)))
                
                fig.add_trace(
                    go.Scatter(x=time_points, y=counts, mode='lines', name='Cell Count'),
                    row=1, col=2
                )
        
        # Tissue scale visualization
        layers = ['SC', 'SG', 'SS', 'SB']  # Abbreviated layer names
        thickness = [0.02, 0.05, 0.08, 0.03]
        
        fig.add_trace(
            go.Bar(x=layers, y=thickness, name='Layer Thickness'),
            row=2, col=1
        )
        
        fig.update_layout(height=1000, title_text="Multiscale Skin Model Overview")
        
        if save:
            output_path = f"{self.output_dir}/multiscale_overview.html"
            fig.write_html(output_path)
            logger.info(f"Multiscale overview plot saved to {output_path}")
        
        return fig
    
    def create_interactive_dashboard(self, all_data, save=True):
        """Create interactive dashboard for real-time monitoring"""
        # This would integrate with Dash for a full interactive dashboard
        logger.info("Interactive dashboard creation would require Dash integration")
        
        # For now, create a comprehensive static visualization
        return self.plot_multiscale_overview(all_data, save)
    
    def export_plots_as_images(self, plots, format='png'):
        """Export plots as static images"""
        for plot_name, fig in plots.items():
            if fig is not None:
                output_path = f"{self.output_dir}/{plot_name}.{format}"
                if hasattr(fig, 'write_image'):
                    fig.write_image(output_path)
                elif hasattr(fig, 'savefig'):
                    fig.savefig(output_path, format=format, dpi=300, bbox_inches='tight')
                
                logger.info(f"Plot {plot_name} exported to {output_path}")

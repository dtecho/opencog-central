
"""
SkinTwin Web Interface

Provides a comprehensive web-based interface for interacting with the
SkinTwin multiscale skin modeling system.
"""

import os
import json
import logging
from flask import Flask, render_template, request, jsonify, send_from_directory
from flask_cors import CORS
import numpy as np
import matplotlib.pyplot as plt
import io
import base64
from datetime import datetime

logger = logging.getLogger(__name__)

class SkinTwinWebInterface:
    """Web interface for SkinTwin system"""
    
    def __init__(self, skin_twin_core, config=None):
        self.skin_twin = skin_twin_core
        self.config = config or {}
        self.app = Flask(__name__, 
                         template_folder='templates',
                         static_folder='static')
        CORS(self.app)
        
        # Configure Flask
        self.app.config['SECRET_KEY'] = 'skintwin-secret-key'
        self.app.config['DEBUG'] = self.config.get('debug', False)
        
        self._setup_routes()
        self._server = None
        
    def _setup_routes(self):
        """Setup Flask routes"""
        
        @self.app.route('/')
        def index():
            """Main dashboard"""
            return render_template('dashboard.html')
            
        @self.app.route('/api/status')
        def api_status():
            """System status endpoint"""
            try:
                status = {
                    'system_running': self.skin_twin.is_running if hasattr(self.skin_twin, 'is_running') else True,
                    'atomspace_size': self._get_atomspace_size(),
                    'molecular_components': self._get_component_count('molecular'),
                    'cellular_components': self._get_component_count('cellular'),
                    'tissue_components': self._get_component_count('tissue'),
                    'timestamp': datetime.now().isoformat()
                }
                return jsonify(status)
            except Exception as e:
                logger.error(f"Error getting system status: {e}")
                return jsonify({'error': str(e)}), 500
                
        @self.app.route('/api/simulation/start', methods=['POST'])
        def api_start_simulation():
            """Start simulation endpoint"""
            try:
                params = request.get_json() or {}
                duration = params.get('duration', 1.0)
                time_step = params.get('time_step', 0.1)
                
                # Start simulation using cython interface
                from .cython_integration import SkinSimulationEngine
                
                if hasattr(self.skin_twin, 'skin_interface'):
                    sim_engine = SkinSimulationEngine(self.skin_twin.skin_interface)
                    results = sim_engine.run_simulation(duration=duration, output_interval=time_step)
                    
                    return jsonify({
                        'success': True,
                        'simulation_id': 'sim_' + str(int(datetime.now().timestamp())),
                        'time_points': len(results.get('time_points', [])),
                        'final_time': results.get('time_points', [0])[-1] if results.get('time_points') else 0
                    })
                else:
                    return jsonify({'error': 'Skin interface not available'}), 500
                    
            except Exception as e:
                logger.error(f"Error starting simulation: {e}")
                return jsonify({'error': str(e)}), 500
                
        @self.app.route('/api/visualization/molecular')
        def api_molecular_visualization():
            """Generate molecular visualization"""
            try:
                # Create sample molecular network visualization
                fig, ax = plt.subplots(figsize=(10, 8))
                
                # Generate sample data for molecular interactions
                molecules = ['Water', 'Ceramide', 'Cholesterol', 'Collagen', 'Elastin']
                interactions = np.random.rand(len(molecules), len(molecules))
                
                im = ax.imshow(interactions, cmap='viridis', aspect='auto')
                ax.set_xticks(range(len(molecules)))
                ax.set_yticks(range(len(molecules)))
                ax.set_xticklabels(molecules, rotation=45)
                ax.set_yticklabels(molecules)
                ax.set_title('Molecular Interaction Network')
                
                plt.colorbar(im, ax=ax, label='Interaction Strength')
                plt.tight_layout()
                
                # Convert to base64
                img_buffer = io.BytesIO()
                plt.savefig(img_buffer, format='png', dpi=150, bbox_inches='tight')
                img_buffer.seek(0)
                img_str = base64.b64encode(img_buffer.getvalue()).decode()
                plt.close()
                
                return jsonify({
                    'image': f'data:image/png;base64,{img_str}',
                    'molecules': molecules,
                    'interactions': interactions.tolist()
                })
                
            except Exception as e:
                logger.error(f"Error generating molecular visualization: {e}")
                return jsonify({'error': str(e)}), 500
                
        @self.app.route('/api/model/export', methods=['POST'])
        def api_export_model():
            """Export model data"""
            try:
                export_format = request.json.get('format', 'json')
                
                if hasattr(self.skin_twin, 'skin_interface'):
                    if export_format == 'atomese':
                        # Export to Atomese format
                        success = self.skin_twin.skin_interface.export_model_state('exported_model.scm')
                        if success:
                            with open('exported_model.scm', 'r') as f:
                                content = f.read()
                            return jsonify({'success': True, 'content': content, 'format': 'atomese'})
                    else:
                        # Export summary data
                        summary = {
                            'molecular_summary': self.skin_twin.skin_interface.get_scale_summary('molecular'),
                            'cellular_summary': self.skin_twin.skin_interface.get_scale_summary('cellular'),
                            'tissue_summary': self.skin_twin.skin_interface.get_scale_summary('tissue'),
                            'export_timestamp': datetime.now().isoformat()
                        }
                        return jsonify({'success': True, 'data': summary, 'format': 'json'})
                
                return jsonify({'error': 'Skin interface not available'}), 500
                
            except Exception as e:
                logger.error(f"Error exporting model: {e}")
                return jsonify({'error': str(e)}), 500
                
        @self.app.route('/api/analysis/statistics')
        def api_analysis_statistics():
            """Get analysis statistics"""
            try:
                stats = {
                    'molecular_stats': self._get_molecular_statistics(),
                    'cellular_stats': self._get_cellular_statistics(),
                    'tissue_stats': self._get_tissue_statistics(),
                    'system_metrics': self._get_system_metrics()
                }
                return jsonify(stats)
                
            except Exception as e:
                logger.error(f"Error getting analysis statistics: {e}")
                return jsonify({'error': str(e)}), 500
    
    def _get_atomspace_size(self):
        """Get current AtomSpace size"""
        try:
            if hasattr(self.skin_twin, 'atomspace_manager'):
                return len(self.skin_twin.atomspace_manager.atomspace)
            return 0
        except:
            return 0
            
    def _get_component_count(self, scale):
        """Get component count for a specific scale"""
        try:
            if hasattr(self.skin_twin, 'skin_interface'):
                summary = self.skin_twin.skin_interface.get_scale_summary(scale)
                return summary.get('component_count', 0)
            return 0
        except:
            return 0
            
    def _get_molecular_statistics(self):
        """Get molecular-level statistics"""
        return {
            'total_molecules': np.random.randint(100, 1000),
            'unique_types': np.random.randint(10, 50),
            'interaction_count': np.random.randint(500, 5000),
            'avg_interaction_strength': np.random.uniform(0.1, 0.9)
        }
        
    def _get_cellular_statistics(self):
        """Get cellular-level statistics"""
        return {
            'total_cells': np.random.randint(50, 500),
            'cell_types': ['keratinocyte', 'fibroblast', 'melanocyte'],
            'avg_cell_density': np.random.uniform(100, 1000),
            'proliferation_rate': np.random.uniform(0.01, 0.1)
        }
        
    def _get_tissue_statistics(self):
        """Get tissue-level statistics"""
        return {
            'tissue_layers': ['stratum_corneum', 'epidermis', 'dermis'],
            'total_thickness': np.random.uniform(1.0, 3.0),
            'permeability': np.random.uniform(0.1, 0.8),
            'mechanical_properties': {
                'elasticity': np.random.uniform(100, 1000),
                'viscosity': np.random.uniform(10, 100)
            }
        }
        
    def _get_system_metrics(self):
        """Get system performance metrics"""
        return {
            'memory_usage': np.random.uniform(100, 500),  # MB
            'cpu_usage': np.random.uniform(10, 80),  # %
            'simulation_speed': np.random.uniform(1.0, 10.0),  # timesteps/second
            'last_update': datetime.now().isoformat()
        }
    
    def start(self, host='0.0.0.0', port=5000):
        """Start the web server"""
        logger.info(f"Starting SkinTwin web interface on {host}:{port}")
        try:
            self.app.run(host=host, port=port, debug=self.config.get('debug', False))
        except Exception as e:
            logger.error(f"Failed to start web interface: {e}")
            
    def stop(self):
        """Stop the web server"""
        logger.info("Stopping SkinTwin web interface")
        # Flask development server doesn't have a clean stop method
        # In production, this would be handled by the WSGI server

def create_app(skin_twin_core=None, config=None):
    """Factory function to create Flask app"""
    interface = SkinTwinWebInterface(skin_twin_core, config)
    return interface.app

if __name__ == '__main__':
    # For testing purposes
    app = create_app()
    app.run(host='0.0.0.0', port=5000, debug=True)

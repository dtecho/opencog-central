
"""
SkinTwin Web Interface

Web-based analysis workbench for the SkinTwin-ASI system
providing interactive tools for skin modeling and analysis.
"""

import logging
from flask import Flask, render_template, request, jsonify
from flask_cors import CORS
from typing import Dict, Any, Optional
import json

class SkinTwinWebInterface:
    """
    Web-based analysis workbench for SkinTwin-ASI
    
    Provides:
    - Interactive skin model visualization
    - Chemical analysis tools
    - Biological pathway exploration
    - Formulation design interface
    - AI agent interaction
    """
    
    def __init__(self, skin_twin_core, config: Dict[str, Any]):
        self.logger = logging.getLogger(__name__)
        self.skin_twin_core = skin_twin_core
        self.config = config
        
        # Initialize Flask app
        self.app = Flask(__name__, 
                        template_folder='templates',
                        static_folder='static')
        CORS(self.app)
        
        # Setup routes
        self._setup_routes()
        
        self.logger.info("SkinTwin web interface initialized")
    
    def _setup_routes(self):
        """Setup Flask routes for the web interface"""
        
        @self.app.route('/')
        def index():
            """Main dashboard"""
            return render_template('dashboard.html', 
                                 system_status=self.skin_twin_core.get_status())
        
        @self.app.route('/api/status')
        def api_status():
            """API endpoint for system status"""
            return jsonify(self.skin_twin_core.get_status())
        
        @self.app.route('/api/multiscale-model')
        def api_multiscale_model():
            """API endpoint for multiscale model data"""
            return jsonify({
                "molecular": list(self.skin_twin_core.multiscale_model.molecular_components.keys()),
                "cellular": list(self.skin_twin_core.multiscale_model.cellular_components.keys()),
                "tissue": list(self.skin_twin_core.multiscale_model.tissue_components.keys())
            })
        
        @self.app.route('/api/analyze-compound', methods=['POST'])
        def api_analyze_compound():
            """Analyze chemical compound for skin compatibility"""
            data = request.get_json()
            compound_smiles = data.get('smiles', '')
            
            if not compound_smiles:
                return jsonify({"error": "SMILES string required"}), 400
            
            # Use chemical integration for analysis
            if hasattr(self.skin_twin_core, 'chemical_integration'):
                result = self.skin_twin_core.chemical_integration.predict_skin_penetration(compound_smiles)
                return jsonify(result)
            else:
                return jsonify({"error": "Chemical integration not available"}), 503
        
        @self.app.route('/api/formulation-design', methods=['POST'])
        def api_formulation_design():
            """Design skincare formulation"""
            data = request.get_json()
            ingredients = data.get('ingredients', [])
            target_properties = data.get('target_properties', {})
            
            # Mock formulation design
            recommendation = {
                "formulation_type": "serum",
                "base_ingredients": ["water", "glycerin", "niacinamide"],
                "active_ingredients": ingredients,
                "predicted_properties": {
                    "viscosity": "low",
                    "penetration": "high",
                    "stability": "good"
                },
                "manufacturing_notes": [
                    "Heat aqueous phase to 70°C",
                    "Add actives below 40°C",
                    "Adjust pH to 5.5-6.5"
                ]
            }
            
            return jsonify(recommendation)
        
        @self.app.route('/api/biological-pathways')
        def api_biological_pathways():
            """Get biological pathway information"""
            pathways = {
                "collagen_synthesis": {
                    "genes": ["COL1A1", "COL1A2", "COL3A1"],
                    "proteins": ["Collagen_I", "Collagen_III"],
                    "regulation": ["TGF_beta", "Vitamin_C"],
                    "location": "dermis"
                },
                "barrier_function": {
                    "genes": ["KRT1", "KRT10", "FLG"],
                    "proteins": ["Keratin", "Filaggrin"],
                    "lipids": ["Ceramides", "Cholesterol"],
                    "location": "epidermis"
                }
            }
            
            return jsonify(pathways)
        
        @self.app.route('/visualization')
        def visualization():
            """3D skin model visualization page"""
            return render_template('visualization.html')
        
        @self.app.route('/analysis')
        def analysis():
            """Chemical analysis tools page"""
            return render_template('analysis.html')
        
        @self.app.route('/formulation')
        def formulation():
            """Formulation design interface"""
            return render_template('formulation.html')
        
        @self.app.route('/ai-chat')
        def ai_chat():
            """AI agent chat interface"""
            return render_template('ai_chat.html')
    
    def start(self):
        """Start the web interface server"""
        host = self.config.get('host', '0.0.0.0')
        port = self.config.get('port', 5000)
        debug = self.config.get('debug', True)
        
        self.logger.info(f"Starting web interface on {host}:{port}")
        
        try:
            self.app.run(host=host, port=port, debug=debug, threaded=True)
        except Exception as e:
            self.logger.error(f"Failed to start web interface: {e}")
            raise
    
    def stop(self):
        """Stop the web interface server"""
        self.logger.info("Stopping web interface...")
        # Flask doesn't have a direct stop method, would need to implement shutdown
        pass

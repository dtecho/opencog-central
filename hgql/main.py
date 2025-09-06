
"""
HGQL Main Application
Entry point for the HyperGraph Query Language interface system
"""

import asyncio
import logging
from flask import Flask
from hgql.core.query_engine import HypergraphQueryEngine
from hgql.interface.query_builder import HGQLQueryBuilder
from hgql.integration.hub import IntegrationHub, ConnectorFactory, ConnectionConfig, ConnectorType

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)

class HGQLApplication:
    def __init__(self):
        self.query_engine = HypergraphQueryEngine()
        self.integration_hub = IntegrationHub()
        self.query_builder = HGQLQueryBuilder(self.query_engine)
        self.logger = logging.getLogger(__name__)
        
    async def initialize(self):
        """Initialize the HGQL application"""
        self.logger.info("Initializing HGQL Application...")
        
        # Setup default integrations
        await self._setup_default_integrations()
        
        # Connect to data sources
        await self.integration_hub.connect_all()
        
        self.logger.info("HGQL Application initialized successfully")
        
    async def _setup_default_integrations(self):
        """Setup default integration connectors"""
        
        # Example OpenCog AtomSpace connector
        atomspace_config = ConnectionConfig(
            name="atomspace",
            connector_type=ConnectorType.REST_API,
            endpoint="http://localhost:17001",
            authentication={"type": "none"},
            rate_limit=100,
            timeout=30,
            retry_policy={
                "max_retries": 3,
                "backoff_factor": 1.5
            },
            transformation_rules=[
                {
                    "type": "field_mapping",
                    "mapping": {
                        "atom_type": "type",
                        "atom_name": "name"
                    }
                }
            ]
        )
        
        atomspace_connector = ConnectorFactory.create_connector(atomspace_config)
        self.integration_hub.register_connector("atomspace", atomspace_connector)
        
        # Example external knowledge base connector
        kb_config = ConnectionConfig(
            name="knowledge_base",
            connector_type=ConnectorType.REST_API,
            endpoint="https://api.conceptnet.io",
            authentication={"type": "none"},
            rate_limit=50,
            timeout=30,
            retry_policy={
                "max_retries": 2,
                "backoff_factor": 2.0
            },
            transformation_rules=[
                {
                    "type": "data_filtering",
                    "filters": ["english_only", "high_confidence"]
                }
            ]
        )
        
        kb_connector = ConnectorFactory.create_connector(kb_config)
        self.integration_hub.register_connector("knowledge_base", kb_connector)
        
    def run(self, host='0.0.0.0', port=5000, debug=True):
        """Run the HGQL application"""
        self.logger.info(f"Starting HGQL server on {host}:{port}")
        
        # Setup additional Flask routes for integration hub
        self._setup_integration_routes()
        
        # Initialize in background
        asyncio.create_task(self.initialize())
        
        # Run Flask application
        self.query_builder.run(host=host, port=port)
        
    def _setup_integration_routes(self):
        """Setup additional Flask routes for integration management"""
        app = self.query_builder.app
        
        @app.route('/api/integrations')
        def get_integrations():
            from flask import jsonify
            return jsonify(self.integration_hub.get_connection_status())
            
        @app.route('/api/integrations/health')
        async def health_check():
            from flask import jsonify
            health = await self.integration_hub.health_check()
            return jsonify(health)
            
        @app.route('/api/integrations/<source>/query', methods=['POST'])
        async def query_integration(source):
            from flask import request, jsonify
            query_data = request.json
            
            try:
                result = await self.integration_hub.fetch_from_source(source, query_data)
                return jsonify({'success': True, 'data': result})
            except Exception as e:
                return jsonify({'success': False, 'error': str(e)}), 400

def main():
    """Main entry point"""
    app = HGQLApplication()
    app.run(host='0.0.0.0', port=5000, debug=True)

if __name__ == "__main__":
    main()

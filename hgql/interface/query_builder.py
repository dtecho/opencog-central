
"""
HGQL Visual Query Builder
Provides GUI components for constructing hypergraph queries
"""

from flask import Flask, render_template, request, jsonify
import json
from typing import Dict, List, Any
from dataclasses import asdict

class HGQLQueryBuilder:
    def __init__(self, query_engine):
        self.query_engine = query_engine
        self.app = Flask(__name__)
        self.setup_routes()
        
    def setup_routes(self):
        @self.app.route('/')
        def index():
            return render_template('query_builder.html')
            
        @self.app.route('/api/build_query', methods=['POST'])
        def build_query():
            query_data = request.json
            query = self._construct_query(query_data)
            return jsonify({'query': asdict(query)})
            
        @self.app.route('/api/execute_query', methods=['POST'])
        async def execute_query():
            query_data = request.json
            query = self._construct_query(query_data)
            result = await self.query_engine.execute_query(query)
            return jsonify(result)
            
        @self.app.route('/api/schema')
        def get_schema():
            return jsonify(self._get_hypergraph_schema())
            
    def _construct_query(self, data: Dict) -> 'HGQLQuery':
        """Construct HGQLQuery from builder data"""
        from .query_engine import HGQLQuery, QueryType
        
        return HGQLQuery(
            query_type=QueryType(data.get('type', 'MATCH')),
            pattern=data.get('pattern', ''),
            conditions=data.get('conditions', []),
            bindings=data.get('bindings', {}),
            inference_rules=data.get('rules', []),
            confidence_threshold=data.get('confidence', 0.0)
        )
        
    def _get_hypergraph_schema(self) -> Dict:
        """Return hypergraph schema for UI"""
        return {
            'node_types': ['Concept', 'Predicate', 'Schema', 'Variable'],
            'edge_types': ['Inheritance', 'Similarity', 'Evaluation', 'Implication'],
            'inference_rules': ['Deduction', 'Induction', 'Abduction', 'Modus Ponens']
        }
        
    def run(self, host='0.0.0.0', port=5000):
        self.app.run(host=host, port=port, debug=True)

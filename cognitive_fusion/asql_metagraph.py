#!/usr/bin/env python3
"""
ASQL: AtomSpace Query Language with MetaGraph Support
A typed hypergraph query system with full introspection capabilities
Enables the cognitive architecture to query its own query patterns
"""

from typing import Any, Dict, List, Set, Tuple, Optional, Union
from enum import Enum
from dataclasses import dataclass
import json
import time

class AtomType(Enum):
    """Typed atom categories for the MetaGraph"""
    # Knowledge atoms
    CONCEPT = "ConceptNode"
    PREDICATE = "PredicateNode"
    VARIABLE = "VariableNode"
    
    # Link types
    INHERITANCE = "InheritanceLink"
    EVALUATION = "EvaluationLink"
    IMPLICATION = "ImplicationLink"
    SIMILARITY = "SimilarityLink"
    
    # Meta types (for introspection)
    QUERY = "QueryNode"
    PATTERN = "PatternNode"
    INTROSPECTION = "IntrospectionLink"
    SELF_REFERENCE = "SelfReferenceLink"
    
    # Cognitive types
    ATTENTION = "AttentionValue"
    TRUTH_VALUE = "TruthValue"
    EMERGENCE = "EmergencePattern"

@dataclass
class TypedAtom:
    """A typed atom in the MetaGraph"""
    id: str
    atom_type: AtomType
    name: str
    truth_value: Optional[Tuple[float, float]] = None  # (strength, confidence)
    attention_value: Optional[float] = None
    metadata: Dict[str, Any] = None
    
    def __post_init__(self):
        if self.metadata is None:
            self.metadata = {}

@dataclass
class TypedLink:
    """A typed hyperedge in the MetaGraph"""
    id: str
    link_type: AtomType
    targets: List[Union['TypedAtom', 'TypedLink']]
    truth_value: Optional[Tuple[float, float]] = None
    metadata: Dict[str, Any] = None
    
    def __post_init__(self):
        if self.metadata is None:
            self.metadata = {}

class MetaGraph:
    """
    A typed hypergraph that can represent both knowledge and meta-knowledge
    Supports introspection by allowing queries about queries
    """
    
    def __init__(self):
        self.atoms: Dict[str, TypedAtom] = {}
        self.links: Dict[str, TypedLink] = {}
        self.type_index: Dict[AtomType, Set[str]] = {}
        self.query_history: List[Dict] = []
        self.introspection_enabled = True
        
    def add_atom(self, atom: TypedAtom) -> str:
        """Add a typed atom to the MetaGraph"""
        self.atoms[atom.id] = atom
        
        # Index by type for efficient querying
        if atom.atom_type not in self.type_index:
            self.type_index[atom.atom_type] = set()
        self.type_index[atom.atom_type].add(atom.id)
        
        return atom.id
        
    def add_link(self, link: TypedLink) -> str:
        """Add a typed link to the MetaGraph"""
        self.links[link.id] = link
        
        if link.link_type not in self.type_index:
            self.type_index[link.link_type] = set()
        self.type_index[link.link_type].add(link.id)
        
        return link.id
        
    def introspect(self, query_id: str) -> Dict:
        """
        Introspect on a previous query
        This allows the system to understand its own query patterns
        """
        if not self.introspection_enabled:
            return {}
            
        # Find the query in history
        query_data = None
        for q in self.query_history:
            if q['id'] == query_id:
                query_data = q
                break
                
        if not query_data:
            return {}
            
        # Analyze the query pattern
        introspection = {
            'query_id': query_id,
            'pattern_type': self._classify_query_pattern(query_data),
            'cognitive_cost': self._estimate_cognitive_cost(query_data),
            'related_queries': self._find_similar_queries(query_data),
            'optimization_suggestions': self._suggest_optimizations(query_data),
            'emergent_patterns': self._detect_emergent_patterns(query_data)
        }
        
        # Store introspection as a meta-atom
        intro_atom = TypedAtom(
            id=f"introspection_{query_id}",
            atom_type=AtomType.INTROSPECTION,
            name=f"Introspection of {query_id}",
            metadata={'introspection_data': introspection}
        )
        self.add_atom(intro_atom)
        
        # Create self-reference link
        if query_id in self.atoms:
            self_ref = TypedLink(
                id=f"self_ref_{query_id}",
                link_type=AtomType.SELF_REFERENCE,
                targets=[self.atoms[query_id], intro_atom]
            )
            self.add_link(self_ref)
        
        return introspection
        
    def _classify_query_pattern(self, query_data: Dict) -> str:
        """Classify the type of query pattern"""
        query_text = query_data.get('query', '').lower()
        
        if 'match' in query_text and 'where' in query_text:
            return 'pattern_matching'
        elif 'infer' in query_text:
            return 'inference_chain'
        elif 'bind' in query_text:
            return 'variable_binding'
        elif 'introspect' in query_text:
            return 'meta_query'
        else:
            return 'simple_lookup'
            
    def _estimate_cognitive_cost(self, query_data: Dict) -> float:
        """Estimate the cognitive cost of a query"""
        # Simple heuristic based on query complexity
        complexity = len(query_data.get('query', ''))
        result_size = len(query_data.get('results', []))
        execution_time = query_data.get('execution_time', 0)
        
        cost = (complexity * 0.01 + result_size * 0.1 + execution_time * 10)
        return min(1.0, cost)  # Normalize to 0-1
        
    def _find_similar_queries(self, query_data: Dict) -> List[str]:
        """Find queries with similar patterns"""
        similar = []
        pattern = self._classify_query_pattern(query_data)
        
        for q in self.query_history:
            if q['id'] != query_data['id']:
                if self._classify_query_pattern(q) == pattern:
                    similar.append(q['id'])
                    
        return similar[:5]  # Return top 5 similar
        
    def _suggest_optimizations(self, query_data: Dict) -> List[str]:
        """Suggest query optimizations"""
        suggestions = []
        
        if query_data.get('execution_time', 0) > 0.1:
            suggestions.append("Consider adding type constraints to reduce search space")
            
        if len(query_data.get('results', [])) > 100:
            suggestions.append("Add LIMIT clause to prevent memory overflow")
            
        if 'join' in query_data.get('query', '').lower():
            suggestions.append("Consider caching join results for repeated queries")
            
        return suggestions
        
    def _detect_emergent_patterns(self, query_data: Dict) -> List[Dict]:
        """Detect emergent patterns from query execution"""
        patterns = []
        
        # Check if query revealed unexpected connections
        results = query_data.get('results', [])
        if len(results) > 10:
            patterns.append({
                'type': 'high_connectivity',
                'description': 'Query revealed highly connected knowledge region'
            })
            
        # Check for recursive patterns
        if 'recursive' in query_data.get('query', '').lower():
            patterns.append({
                'type': 'recursive_structure',
                'description': 'Query operates on self-similar structures'
            })
            
        return patterns

class ASQLEngine:
    """
    AtomSpace Query Language Engine with introspection
    Executes typed queries on the MetaGraph with self-awareness
    """
    
    def __init__(self, metagraph: MetaGraph):
        self.metagraph = metagraph
        self.query_cache = {}
        self.introspection_depth = 0
        
    def execute(self, query: str, introspect: bool = False) -> Dict:
        """
        Execute an ASQL query with optional introspection
        """
        query_id = f"query_{int(time.time() * 1000)}"
        start_time = time.time()
        
        # Parse and execute query
        parsed = self._parse_asql(query)
        results = self._execute_parsed(parsed)
        
        execution_time = time.time() - start_time
        
        # Store query in history
        query_record = {
            'id': query_id,
            'query': query,
            'parsed': parsed,
            'results': results,
            'execution_time': execution_time,
            'timestamp': time.time()
        }
        self.metagraph.query_history.append(query_record)
        
        # Create query atom for meta-reasoning
        query_atom = TypedAtom(
            id=query_id,
            atom_type=AtomType.QUERY,
            name=query[:50],  # First 50 chars as name
            metadata={'full_query': query, 'execution_time': execution_time}
        )
        self.metagraph.add_atom(query_atom)
        
        response = {
            'query_id': query_id,
            'results': results,
            'execution_time': execution_time
        }
        
        # Perform introspection if requested
        if introspect:
            self.introspection_depth += 1
            
            # Prevent infinite introspection
            if self.introspection_depth < 3:
                introspection = self.metagraph.introspect(query_id)
                response['introspection'] = introspection
                
                # Meta-meta query: introspect on the introspection
                if self.introspection_depth == 1:
                    meta_query = f"INTROSPECT ON INTROSPECTION {query_id}"
                    meta_result = self.execute(meta_query, introspect=False)
                    response['meta_introspection'] = meta_result
                    
            self.introspection_depth = max(0, self.introspection_depth - 1)
            
        return response
        
    def _parse_asql(self, query: str) -> Dict:
        """Parse ASQL query into structured format"""
        # Simplified parser - real implementation would use proper grammar
        parsed = {
            'operation': None,
            'targets': [],
            'conditions': [],
            'introspection': False
        }
        
        query_upper = query.upper()
        
        if 'MATCH' in query_upper:
            parsed['operation'] = 'match'
        elif 'INTROSPECT' in query_upper:
            parsed['operation'] = 'introspect'
            parsed['introspection'] = True
        elif 'INFER' in query_upper:
            parsed['operation'] = 'infer'
        elif 'BIND' in query_upper:
            parsed['operation'] = 'bind'
        else:
            parsed['operation'] = 'select'
            
        return parsed
        
    def _execute_parsed(self, parsed: Dict) -> List[Any]:
        """Execute parsed query on MetaGraph"""
        operation = parsed['operation']
        
        if operation == 'match':
            return self._execute_match(parsed)
        elif operation == 'introspect':
            return self._execute_introspection(parsed)
        elif operation == 'infer':
            return self._execute_inference(parsed)
        else:
            return []
            
    def _execute_match(self, parsed: Dict) -> List[Any]:
        """Execute pattern matching query"""
        # Simplified - would do actual pattern matching
        results = []
        for atom_id, atom in self.metagraph.atoms.items():
            if atom.atom_type in [AtomType.CONCEPT, AtomType.PREDICATE]:
                results.append({
                    'id': atom_id,
                    'type': atom.atom_type.value,
                    'name': atom.name
                })
        return results[:10]  # Limit for demo
        
    def _execute_introspection(self, parsed: Dict) -> List[Any]:
        """Execute introspection query"""
        # Return information about recent queries
        recent_queries = self.metagraph.query_history[-5:]
        return [
            {
                'query_id': q['id'],
                'pattern': self.metagraph._classify_query_pattern(q),
                'cost': self.metagraph._estimate_cognitive_cost(q)
            }
            for q in recent_queries
        ]
        
    def _execute_inference(self, parsed: Dict) -> List[Any]:
        """Execute inference query"""
        # Simplified inference - would use PLN in production
        inferences = []
        
        # Find implication links
        if AtomType.IMPLICATION in self.metagraph.type_index:
            for link_id in self.metagraph.type_index[AtomType.IMPLICATION]:
                link = self.metagraph.links[link_id]
                inferences.append({
                    'inference': link_id,
                    'confidence': link.truth_value[1] if link.truth_value else 0.5
                })
                
        return inferences

# Example usage demonstrating introspection
if __name__ == '__main__':
    # Create MetaGraph
    mg = MetaGraph()
    
    # Add some knowledge
    human = TypedAtom('human', AtomType.CONCEPT, 'Human', truth_value=(1.0, 0.9))
    mortal = TypedAtom('mortal', AtomType.CONCEPT, 'Mortal', truth_value=(1.0, 0.9))
    mg.add_atom(human)
    mg.add_atom(mortal)
    
    # Add relationship
    inheritance = TypedLink(
        'human_mortal',
        AtomType.INHERITANCE,
        [human, mortal],
        truth_value=(0.99, 0.95)
    )
    mg.add_link(inheritance)
    
    # Create ASQL engine
    engine = ASQLEngine(mg)
    
    # Execute query with introspection
    result = engine.execute(
        "MATCH (x:Concept) WHERE x.truth > 0.8 RETURN x",
        introspect=True
    )
    
    print("🧠 ASQL with MetaGraph Introspection")
    print("=" * 50)
    print(f"Query Results: {result['results']}")
    print(f"Execution Time: {result['execution_time']:.4f}s")
    
    if 'introspection' in result:
        print(f"\n🔍 Introspection:")
        print(f"  Pattern Type: {result['introspection']['pattern_type']}")
        print(f"  Cognitive Cost: {result['introspection']['cognitive_cost']:.2f}")
        print(f"  Suggestions: {result['introspection']['optimization_suggestions']}")
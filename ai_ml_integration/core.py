
"""
OpenCog AI/ML Integration Framework
Connects neural networks, cognitive architectures, and ML systems
"""

import torch
import numpy as np
from typing import Dict, List, Any, Optional, Union
import logging
from pathlib import Path

# Import OpenCog components
try:
    from opencog.atomspace import AtomSpace, TruthValue
    from opencog.type_constructors import *
    from opencog.utilities import initialize_opencog
    OPENCOG_AVAILABLE = True
except ImportError:
    OPENCOG_AVAILABLE = False
    logging.warning("OpenCog not available, using mock implementations")

# Import neural network components
from nn.models.cognitive_net import CognitiveNetwork
from nn.cognitive.attention import AttentionMechanism
from nn.cognitive.memory import WorkingMemory, EpisodicMemory
from nn.atomspace_integration.bridge import AtomSpaceBridge

logger = logging.getLogger(__name__)

class OpenCogAIMLIntegration:
    """
    Core integration framework connecting OpenCog with AI/ML systems
    """
    
    def __init__(self, config: Dict[str, Any] = None):
        self.config = config or self._default_config()
        
        # Initialize components
        self.atomspace = self._init_atomspace()
        self.neural_bridge = self._init_neural_bridge()
        self.cognitive_net = self._init_cognitive_network()
        self.memory_systems = self._init_memory_systems()
        self.attention_system = self._init_attention_system()
        
        # Integration state
        self.integration_metrics = {}
        self.learning_history = []
        
        logger.info("OpenCog AI/ML Integration initialized")
    
    def _default_config(self) -> Dict[str, Any]:
        """Default configuration for the integration system"""
        return {
            'atomspace': {
                'enable_persistence': True,
                'persistence_type': 'rocks',
                'database_path': './atomspace_db'
            },
            'neural': {
                'feature_dim': 512,
                'hidden_dim': 1024,
                'num_layers': 3,
                'attention_heads': 8
            },
            'memory': {
                'working_capacity': 1000,
                'episodic_capacity': 10000,
                'decay_rate': 0.95
            },
            'learning': {
                'learning_rate': 0.001,
                'batch_size': 32,
                'adaptation_rate': 0.1
            }
        }
    
    def _init_atomspace(self) -> Any:
        """Initialize AtomSpace with persistence if available"""
        if OPENCOG_AVAILABLE:
            initialize_opencog()
            atomspace = AtomSpace()
            
            # Set up persistence if configured
            if self.config['atomspace']['enable_persistence']:
                try:
                    # Configure persistence (placeholder for actual implementation)
                    logger.info("AtomSpace persistence configured")
                except Exception as e:
                    logger.warning(f"Persistence setup failed: {e}")
            
            return atomspace
        else:
            return MockAtomSpace()
    
    def _init_neural_bridge(self) -> AtomSpaceBridge:
        """Initialize neural-symbolic bridge"""
        return AtomSpaceBridge(
            feature_dim=self.config['neural']['feature_dim'],
            atomspace=self.atomspace if OPENCOG_AVAILABLE else None
        )
    
    def _init_cognitive_network(self) -> CognitiveNetwork:
        """Initialize cognitive neural network"""
        return CognitiveNetwork(self.config['neural'])
    
    def _init_memory_systems(self) -> Dict[str, Any]:
        """Initialize memory systems"""
        return {
            'working': WorkingMemory(
                capacity=self.config['memory']['working_capacity'],
                feature_dim=self.config['neural']['feature_dim']
            ),
            'episodic': EpisodicMemory(
                capacity=self.config['memory']['episodic_capacity'],
                feature_dim=self.config['neural']['feature_dim']
            )
        }
    
    def _init_attention_system(self) -> AttentionMechanism:
        """Initialize attention mechanism"""
        return AttentionMechanism(
            feature_dim=self.config['neural']['feature_dim'],
            num_heads=self.config['neural']['attention_heads']
        )
    
    def process_input(self, input_data: Union[str, torch.Tensor, Dict[str, Any]]) -> Dict[str, Any]:
        """
        Process input through the integrated AI/ML pipeline
        
        Args:
            input_data: Input can be text, tensor, or structured data
            
        Returns:
            Processing results with neural and symbolic outputs
        """
        results = {
            'input_type': type(input_data).__name__,
            'neural_output': None,
            'symbolic_output': None,
            'attention_weights': None,
            'memory_updates': None
        }
        
        try:
            # Convert input to neural representation
            if isinstance(input_data, str):
                # Text processing
                neural_input = self._text_to_neural(input_data)
                results['symbolic_output'] = self._text_to_symbolic(input_data)
            elif isinstance(input_data, torch.Tensor):
                # Direct neural input
                neural_input = input_data
            else:
                # Structured data
                neural_input = self._structured_to_neural(input_data)
            
            # Process through cognitive network
            cognitive_output = self.cognitive_net(neural_input)
            results['neural_output'] = cognitive_output
            
            # Apply attention
            attended_output, attention_weights = self.attention_system(cognitive_output)
            results['attention_weights'] = attention_weights
            
            # Update memory systems
            memory_updates = self._update_memories(attended_output)
            results['memory_updates'] = memory_updates
            
            # Convert neural output to symbolic if needed
            if results['symbolic_output'] is None:
                results['symbolic_output'] = self.neural_bridge.tensor_to_atoms(
                    attended_output.unsqueeze(0)
                )
            
            # Update integration metrics
            self._update_metrics(results)
            
        except Exception as e:
            logger.error(f"Error processing input: {e}")
            results['error'] = str(e)
        
        return results
    
    def _text_to_neural(self, text: str) -> torch.Tensor:
        """Convert text to neural representation"""
        # Simple embedding (in practice, use proper tokenizer/embedder)
        words = text.lower().split()
        # Create fixed-size representation
        embedding = torch.zeros(self.config['neural']['feature_dim'])
        
        # Basic word hashing (replace with proper embeddings)
        for i, word in enumerate(words[:10]):  # Limit to 10 words
            word_hash = hash(word) % self.config['neural']['feature_dim']
            embedding[word_hash] += 1.0
        
        return embedding.unsqueeze(0).unsqueeze(0)  # Add batch and sequence dims
    
    def _text_to_symbolic(self, text: str) -> Dict[str, Any]:
        """Convert text to symbolic AtomSpace representation"""
        if not OPENCOG_AVAILABLE:
            return {'mock_concepts': text.split()}
        
        atoms_created = []
        words = text.lower().split()
        
        for word in words:
            # Create concept nodes
            concept = ConceptNode(word)
            atoms_created.append(concept)
            
            # Add to atomspace
            self.atomspace.add_atom(concept)
        
        return {
            'atoms_created': len(atoms_created),
            'concepts': [str(atom) for atom in atoms_created]
        }
    
    def _structured_to_neural(self, data: Dict[str, Any]) -> torch.Tensor:
        """Convert structured data to neural representation"""
        # Convert dict to tensor (simplified)
        values = []
        for key, value in data.items():
            if isinstance(value, (int, float)):
                values.append(float(value))
            elif isinstance(value, str):
                values.append(float(hash(value) % 1000) / 1000.0)
        
        # Pad or truncate to feature_dim
        feature_dim = self.config['neural']['feature_dim']
        if len(values) > feature_dim:
            values = values[:feature_dim]
        else:
            values.extend([0.0] * (feature_dim - len(values)))
        
        return torch.tensor(values, dtype=torch.float32).unsqueeze(0).unsqueeze(0)
    
    def _update_memories(self, neural_output: torch.Tensor) -> Dict[str, Any]:
        """Update memory systems with new information"""
        updates = {}
        
        # Update working memory
        working_update = self.memory_systems['working'].store(
            neural_output.squeeze(), 
            importance=0.8
        )
        updates['working_memory'] = working_update
        
        # Update episodic memory
        episodic_update = self.memory_systems['episodic'].store_episode(
            neural_output.squeeze(),
            context={'timestamp': torch.tensor([0.0])}  # Add proper timestamp
        )
        updates['episodic_memory'] = episodic_update
        
        return updates
    
    def _update_metrics(self, results: Dict[str, Any]):
        """Update integration performance metrics"""
        if 'error' not in results:
            self.integration_metrics['successful_processes'] = \
                self.integration_metrics.get('successful_processes', 0) + 1
        else:
            self.integration_metrics['failed_processes'] = \
                self.integration_metrics.get('failed_processes', 0) + 1
        
        self.integration_metrics['total_processes'] = \
            self.integration_metrics.get('total_processes', 0) + 1
    
    def reason_with_pln(self, query: str) -> Dict[str, Any]:
        """
        Perform reasoning using PLN (Probabilistic Logic Networks)
        """
        if not OPENCOG_AVAILABLE:
            return {'mock_reasoning': f"Reasoning about: {query}"}
        
        try:
            # Create query atoms
            query_atoms = self._text_to_symbolic(query)
            
            # Placeholder for PLN reasoning
            # In practice, this would use the PLN reasoning engine
            reasoning_result = {
                'query': query,
                'confidence': 0.8,
                'reasoning_steps': ['premise1', 'inference', 'conclusion'],
                'atoms_involved': query_atoms['concepts']
            }
            
            return reasoning_result
            
        except Exception as e:
            logger.error(f"PLN reasoning failed: {e}")
            return {'error': str(e)}
    
    def learn_from_interaction(self, input_data: Any, feedback: float = 1.0):
        """
        Learn from interaction using both neural and symbolic approaches
        
        Args:
            input_data: Input to learn from
            feedback: Feedback signal (-1.0 to 1.0)
        """
        # Process input through pipeline
        results = self.process_input(input_data)
        
        # Update neural networks based on feedback
        if results['neural_output'] is not None:
            self._update_neural_weights(results['neural_output'], feedback)
        
        # Update symbolic knowledge
        if results['symbolic_output'] is not None:
            self._update_symbolic_knowledge(results['symbolic_output'], feedback)
        
        # Store learning episode
        learning_episode = {
            'input': str(input_data),
            'feedback': feedback,
            'neural_state': results.get('neural_output'),
            'symbolic_state': results.get('symbolic_output')
        }
        self.learning_history.append(learning_episode)
        
        logger.info(f"Learning episode recorded with feedback: {feedback}")
    
    def _update_neural_weights(self, neural_output: torch.Tensor, feedback: float):
        """Update neural network weights based on feedback"""
        # Simplified learning update
        learning_rate = self.config['learning']['learning_rate']
        adaptation_rate = self.config['learning']['adaptation_rate']
        
        # Update cognitive network (placeholder)
        # In practice, this would involve proper backpropagation
        pass
    
    def _update_symbolic_knowledge(self, symbolic_output: Dict[str, Any], feedback: float):
        """Update symbolic knowledge based on feedback"""
        if not OPENCOG_AVAILABLE:
            return
        
        # Update truth values based on feedback
        for concept_str in symbolic_output.get('concepts', []):
            try:
                # Find or create concept
                concept = ConceptNode(concept_str.split('"')[1])  # Extract name
                
                # Update truth value based on feedback
                current_tv = concept.tv if hasattr(concept, 'tv') else TruthValue(0.5, 0.1)
                new_strength = min(1.0, max(0.0, current_tv.mean + feedback * 0.1))
                new_confidence = min(1.0, current_tv.confidence + 0.01)
                
                concept.tv = TruthValue(new_strength, new_confidence)
                
            except Exception as e:
                logger.warning(f"Failed to update concept {concept_str}: {e}")
    
    def get_cognitive_state(self) -> Dict[str, Any]:
        """Get current cognitive state across all systems"""
        state = {
            'neural_state': self.cognitive_net.get_cognitive_state(),
            'memory_state': {
                'working_memory_size': len(self.memory_systems['working'].memories),
                'episodic_memory_size': len(self.memory_systems['episodic'].episodes)
            },
            'attention_state': self.attention_system.get_attention_state(),
            'integration_metrics': self.integration_metrics,
            'atomspace_size': self.atomspace.size() if OPENCOG_AVAILABLE else 0
        }
        
        return state
    
    def save_state(self, filepath: str):
        """Save current integration state"""
        state = {
            'config': self.config,
            'cognitive_state': self.get_cognitive_state(),
            'learning_history': self.learning_history[-100:]  # Last 100 episodes
        }
        
        # Save neural network state
        if hasattr(self.cognitive_net, 'state_dict'):
            state['neural_weights'] = self.cognitive_net.state_dict()
        
        torch.save(state, filepath)
        logger.info(f"State saved to {filepath}")
    
    def load_state(self, filepath: str):
        """Load integration state"""
        try:
            state = torch.load(filepath)
            
            # Restore configuration
            self.config.update(state.get('config', {}))
            
            # Restore learning history
            self.learning_history = state.get('learning_history', [])
            
            # Restore neural weights
            if 'neural_weights' in state and hasattr(self.cognitive_net, 'load_state_dict'):
                self.cognitive_net.load_state_dict(state['neural_weights'])
            
            logger.info(f"State loaded from {filepath}")
            
        except Exception as e:
            logger.error(f"Failed to load state: {e}")

class MockAtomSpace:
    """Mock AtomSpace for when OpenCog is not available"""
    
    def __init__(self):
        self.atoms = {}
        self.atom_count = 0
    
    def add_atom(self, atom):
        self.atom_count += 1
        self.atoms[self.atom_count] = atom
        return atom
    
    def size(self):
        return self.atom_count

class AIMLIntegrationManager:
    """
    High-level manager for AI/ML integration across OpenCog ecosystem
    """
    
    def __init__(self):
        self.integrations = {}
        self.active_sessions = {}
    
    def create_integration(self, name: str, config: Dict[str, Any] = None) -> OpenCogAIMLIntegration:
        """Create a new AI/ML integration instance"""
        integration = OpenCogAIMLIntegration(config)
        self.integrations[name] = integration
        logger.info(f"Created integration: {name}")
        return integration
    
    def get_integration(self, name: str) -> Optional[OpenCogAIMLIntegration]:
        """Get existing integration by name"""
        return self.integrations.get(name)
    
    def list_integrations(self) -> List[str]:
        """List all available integrations"""
        return list(self.integrations.keys())
    
    def start_learning_session(self, integration_name: str, session_name: str):
        """Start a learning session for continuous learning"""
        integration = self.get_integration(integration_name)
        if integration:
            self.active_sessions[session_name] = {
                'integration': integration,
                'start_time': torch.tensor([0.0]),  # Add proper timestamp
                'interactions': 0
            }
            logger.info(f"Started learning session: {session_name}")
    
    def end_learning_session(self, session_name: str) -> Dict[str, Any]:
        """End learning session and return summary"""
        if session_name in self.active_sessions:
            session = self.active_sessions.pop(session_name)
            
            summary = {
                'session_name': session_name,
                'interactions': session['interactions'],
                'final_state': session['integration'].get_cognitive_state()
            }
            
            logger.info(f"Ended learning session: {session_name}")
            return summary
        
        return {'error': f"Session {session_name} not found"}

# Global integration manager
integration_manager = AIMLIntegrationManager()

def get_integration_manager() -> AIMLIntegrationManager:
    """Get the global integration manager"""
    return integration_manager


"""
Cognitive Network Architecture
=============================

Main neural network architecture that integrates multiple cognitive components.
"""

import torch
import torch.nn as nn
from typing import Dict, List, Optional, Any, Tuple
from ..core.module import NeuralModule, Sequential
from ..layers.linear import CognitiveLinear
from ..layers.attention import MultiHeadAttention, CognitiveAttention
from ..cognitive.memory import WorkingMemory, EpisodicMemory
from ..cognitive.attention import AttentionMechanism


class CognitiveNetwork(NeuralModule):
    """
    Comprehensive cognitive neural network architecture.
    
    Integrates multiple cognitive subsystems:
    - Attention mechanisms
    - Working and episodic memory
    - Reasoning capabilities
    - Learning and adaptation
    """
    
    def __init__(self, config: Dict[str, Any], name: str = "CognitiveNetwork"):
        super().__init__(name=name)
        
        self.config = config
        self.input_dim = config['input_dim']
        self.hidden_dim = config['hidden_dim']
        self.output_dim = config['output_dim']
        self.num_layers = config.get('num_layers', 3)
        self.attention_heads = config.get('attention_heads', 8)
        
        # Input processing
        self.input_processor = CognitiveLinear(
            self.input_dim, self.hidden_dim, name="InputProcessor"
        )
        
        # Attention mechanism
        self.attention = MultiHeadAttention(
            self.hidden_dim, self.attention_heads, name="CoreAttention"
        )
        
        # Working memory system
        self.working_memory = WorkingMemory(
            capacity=config.get('working_memory_capacity', 64),
            feature_dim=self.hidden_dim
        )
        
        # Episodic memory system
        self.episodic_memory = EpisodicMemory(
            capacity=config.get('episodic_memory_capacity', 1000),
            feature_dim=self.hidden_dim
        )
        
        # Attention management
        self.attention_manager = AttentionMechanism(
            feature_dim=self.hidden_dim,
            focus_size=config.get('attention_focus_size', 16)
        )
        
        # Processing layers
        self.hidden_layers = nn.ModuleList([
            CognitiveLinear(self.hidden_dim, self.hidden_dim, 
                          name=f"HiddenLayer_{i}")
            for i in range(self.num_layers)
        ])
        
        # Output processing
        self.output_processor = CognitiveLinear(
            self.hidden_dim, self.output_dim, name="OutputProcessor"
        )
        
        # Cognitive state tracking
        self.cognitive_state = {
            'arousal': 0.5,
            'valence': 0.0,
            'attention_focus': torch.zeros(self.hidden_dim),
            'memory_consolidation': 0.0
        }
        
        self.reset_parameters()
    
    def _forward_impl(self, x: torch.Tensor, 
                     context: Optional[torch.Tensor] = None,
                     return_attention: bool = False,
                     return_memory_state: bool = False) -> torch.Tensor:
        
        batch_size, seq_len, _ = x.size()
        
        # Input processing
        hidden = self.input_processor(x)
        
        # Apply attention mechanism
        attended_hidden, attention_weights = self.attention(
            hidden, return_attention=True
        )
        
        # Update attention manager
        self.attention_manager.update_focus(attended_hidden.mean(dim=1))
        
        # Working memory integration
        memory_enhanced = self.working_memory.integrate(attended_hidden)
        
        # Process through hidden layers
        for layer in self.hidden_layers:
            residual = memory_enhanced
            memory_enhanced = F.relu(layer(memory_enhanced))
            
            # Residual connection with attention weighting
            if memory_enhanced.size() == residual.size():
                memory_enhanced = memory_enhanced + 0.1 * residual
        
        # Update episodic memory
        if self.training:
            self.episodic_memory.store_episode(memory_enhanced.detach())
        
        # Output processing
        output = self.output_processor(memory_enhanced)
        
        # Update cognitive state
        self._update_cognitive_state(attention_weights, memory_enhanced)
        
        # Prepare return values
        result = output
        
        if return_attention:
            result = (result, attention_weights)
        
        if return_memory_state:
            memory_state = {
                'working_memory': self.working_memory.get_state(),
                'episodic_memory': self.episodic_memory.get_recent_episodes(5),
                'attention_focus': self.attention_manager.get_focus_state()
            }
            
            if return_attention:
                result = (*result, memory_state)
            else:
                result = (result, memory_state)
        
        return result
    
    def _update_cognitive_state(self, attention_weights: torch.Tensor, 
                               hidden_state: torch.Tensor):
        """Update cognitive state based on current processing."""
        with torch.no_grad():
            # Update arousal based on attention distribution
            attention_entropy = self._compute_entropy(attention_weights)
            self.cognitive_state['arousal'] = 0.9 * self.cognitive_state['arousal'] + \
                                            0.1 * attention_entropy
            
            # Update attention focus
            current_focus = hidden_state.mean(dim=(0, 1))
            self.cognitive_state['attention_focus'] = \
                0.8 * self.cognitive_state['attention_focus'] + 0.2 * current_focus
    
    def _compute_entropy(self, attention_weights: torch.Tensor) -> float:
        """Compute entropy of attention distribution."""
        # Average over batch and heads
        avg_attention = attention_weights.mean(dim=(0, 1))
        entropy = -torch.sum(avg_attention * torch.log(avg_attention + 1e-8))
        return torch.sigmoid(entropy / 10.0).item()  # Normalize to [0,1]
    
    def get_cognitive_state(self) -> Dict[str, Any]:
        """Get current cognitive state."""
        return {
            'arousal': self.cognitive_state['arousal'],
            'valence': self.cognitive_state['valence'],
            'attention_focus_norm': torch.norm(self.cognitive_state['attention_focus']).item(),
            'working_memory_usage': self.working_memory.get_usage_ratio(),
            'episodic_memory_size': len(self.episodic_memory.episodes)
        }
    
    def consolidate_memory(self):
        """Trigger memory consolidation process."""
        # Move important items from working to episodic memory
        important_items = self.working_memory.get_high_importance_items()
        for item in important_items:
            self.episodic_memory.store_episode(item)
        
        # Clear working memory of consolidated items
        self.working_memory.consolidate()
        
        self.cognitive_state['memory_consolidation'] += 0.1
    
    def adapt_learning_rate(self, current_lr: float) -> float:
        """Adapt learning rate based on cognitive state."""
        arousal = self.cognitive_state['arousal']
        
        # Higher arousal -> higher learning rate (within bounds)
        adaptation_factor = 0.5 + arousal
        adapted_lr = current_lr * adaptation_factor
        
        return max(1e-6, min(adapted_lr, 1e-2))
    
    def get_network_summary(self) -> str:
        """Generate comprehensive network summary."""
        total_params = sum(p.numel() for p in self.parameters())
        trainable_params = sum(p.numel() for p in self.parameters() if p.requires_grad)
        
        summary = [
            f"Cognitive Network: {self.name}",
            f"Total Parameters: {total_params:,}",
            f"Trainable Parameters: {trainable_params:,}",
            f"Input Dimension: {self.input_dim}",
            f"Hidden Dimension: {self.hidden_dim}",
            f"Output Dimension: {self.output_dim}",
            f"Attention Heads: {self.attention_heads}",
            f"Hidden Layers: {self.num_layers}",
            "",
            "Cognitive State:",
            f"  Arousal: {self.cognitive_state['arousal']:.3f}",
            f"  Valence: {self.cognitive_state['valence']:.3f}",
            f"  Working Memory Usage: {self.working_memory.get_usage_ratio():.3f}",
            f"  Episodic Episodes: {len(self.episodic_memory.episodes)}"
        ]
        
        return "\n".join(summary)


class CognitiveEnsemble(NeuralModule):
    """
    Ensemble of cognitive networks with voting mechanisms.
    """
    
    def __init__(self, networks: List[CognitiveNetwork], 
                 voting_method: str = "attention_weighted",
                 name: str = "CognitiveEnsemble"):
        super().__init__(name=name)
        
        self.networks = nn.ModuleList(networks)
        self.voting_method = voting_method
        
        # Meta-attention for ensemble weighting
        if networks:
            feature_dim = networks[0].hidden_dim
            self.meta_attention = CognitiveAttention(
                feature_dim, name="MetaAttention"
            )
    
    def _forward_impl(self, x: torch.Tensor, **kwargs) -> torch.Tensor:
        # Get outputs from all networks
        outputs = []
        attention_states = []
        
        for network in self.networks:
            output = network(x, **kwargs)
            if isinstance(output, tuple):
                outputs.append(output[0])
                attention_states.append(output[1])
            else:
                outputs.append(output)
                attention_states.append(None)
        
        # Stack outputs
        stacked_outputs = torch.stack(outputs, dim=0)  # [num_networks, batch, ...]
        
        # Apply voting mechanism
        if self.voting_method == "simple_average":
            final_output = stacked_outputs.mean(dim=0)
        elif self.voting_method == "attention_weighted":
            final_output = self._attention_weighted_vote(stacked_outputs, x)
        else:
            final_output = stacked_outputs[0]  # Fallback to first network
        
        return final_output
    
    def _attention_weighted_vote(self, outputs: torch.Tensor, x: torch.Tensor) -> torch.Tensor:
        """Compute attention-weighted ensemble output."""
        num_networks, batch_size, seq_len, feature_dim = outputs.size()
        
        # Compute meta-attention over networks
        network_features = outputs.mean(dim=2)  # Average over sequence
        
        network_weights = []
        for i in range(num_networks):
            weight, _ = self.meta_attention(network_features[i].unsqueeze(1))
            network_weights.append(weight.squeeze(1))
        
        # Stack and normalize weights
        network_weights = torch.stack(network_weights, dim=0)
        network_weights = F.softmax(network_weights, dim=0)
        
        # Apply weights
        weighted_output = torch.sum(
            outputs * network_weights.unsqueeze(-1).unsqueeze(-1), dim=0
        )
        
        return weighted_output

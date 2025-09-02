
"""
Cognitive Linear Layers
=======================

Linear transformation layers enhanced with cognitive features.
"""

import torch
import torch.nn as nn
import torch.nn.functional as F
from typing import Optional, Dict, Any
from ..core.module import NeuralModule


class CognitiveLinear(NeuralModule):
    """
    Linear layer with cognitive attention mechanisms.
    
    Features:
    - Attention-weighted connections
    - Adaptive weight updates based on importance
    - Integration with AtomSpace concepts
    """
    
    def __init__(self, in_features: int, out_features: int, 
                 bias: bool = True, attention_dim: int = None,
                 name: str = "CognitiveLinear"):
        super().__init__(name=name)
        
        self.in_features = in_features
        self.out_features = out_features
        self.attention_dim = attention_dim or min(in_features, out_features) // 4
        
        # Core linear transformation
        self.linear = nn.Linear(in_features, out_features, bias=bias)
        
        # Attention mechanism for adaptive weights
        self.attention_net = nn.Sequential(
            nn.Linear(in_features, self.attention_dim),
            nn.Tanh(),
            nn.Linear(self.attention_dim, out_features),
            nn.Sigmoid()
        )
        
        # Cognitive importance tracking
        self.importance_weights = nn.Parameter(torch.ones(out_features))
        self.usage_counter = nn.Parameter(torch.zeros(out_features), requires_grad=False)
        
        self.reset_parameters()
    
    def _forward_impl(self, x: torch.Tensor, use_attention: bool = True) -> torch.Tensor:
        # Standard linear transformation
        output = self.linear(x)
        
        if use_attention and self.training:
            # Compute attention weights
            attention_weights = self.attention_net(x)
            
            # Apply attention to output
            output = output * attention_weights
            
            # Update usage statistics
            with torch.no_grad():
                self.usage_counter += output.abs().mean(dim=0)
        
        # Apply importance weighting
        output = output * self.importance_weights
        
        return output
    
    def update_importance(self, feedback: torch.Tensor):
        """Update importance weights based on feedback."""
        with torch.no_grad():
            self.importance_weights += 0.01 * feedback.mean(dim=0)
            self.importance_weights.clamp_(0.1, 2.0)
    
    def get_usage_stats(self) -> Dict[str, torch.Tensor]:
        """Get usage statistics for analysis."""
        return {
            'usage_counter': self.usage_counter.clone(),
            'importance_weights': self.importance_weights.clone(),
            'total_usage': self.usage_counter.sum(),
            'mean_importance': self.importance_weights.mean()
        }
    
    def reset_usage_stats(self):
        """Reset usage statistics."""
        with torch.no_grad():
            self.usage_counter.zero_()


class AdaptiveLinear(NeuralModule):
    """
    Linear layer that adapts its structure based on cognitive feedback.
    
    Can grow or shrink the number of connections based on usage patterns.
    """
    
    def __init__(self, in_features: int, out_features: int,
                 bias: bool = True, adaptation_rate: float = 0.01,
                 name: str = "AdaptiveLinear"):
        super().__init__(name=name)
        
        self.in_features = in_features
        self.out_features = out_features
        self.adaptation_rate = adaptation_rate
        
        self.weight = nn.Parameter(torch.empty(out_features, in_features))
        self.bias = nn.Parameter(torch.empty(out_features)) if bias else None
        
        # Adaptive connection masks
        self.connection_strength = nn.Parameter(torch.ones_like(self.weight))
        self.connection_threshold = 0.1
        
        # Plasticity mechanisms
        self.hebbian_trace = nn.Parameter(torch.zeros_like(self.weight), requires_grad=False)
        
        self.reset_parameters()
    
    def _forward_impl(self, x: torch.Tensor) -> torch.Tensor:
        # Apply connection masking
        effective_weight = self.weight * (self.connection_strength > self.connection_threshold).float()
        
        # Standard linear operation
        output = F.linear(x, effective_weight, self.bias)
        
        # Update Hebbian traces during training
        if self.training:
            self._update_hebbian_traces(x, output)
        
        return output
    
    def _update_hebbian_traces(self, x: torch.Tensor, output: torch.Tensor):
        """Update Hebbian learning traces."""
        with torch.no_grad():
            # Compute correlation between input and output
            correlation = torch.outer(output.mean(dim=0), x.mean(dim=0))
            
            # Update traces with decay
            self.hebbian_trace = 0.99 * self.hebbian_trace + 0.01 * correlation
            
            # Update connection strengths based on correlation
            self.connection_strength += self.adaptation_rate * self.hebbian_trace.abs()
            self.connection_strength.clamp_(0.0, 2.0)
    
    def prune_connections(self, threshold: float = None):
        """Prune weak connections."""
        threshold = threshold or self.connection_threshold
        with torch.no_grad():
            mask = self.connection_strength > threshold
            self.weight *= mask.float()
            self.connection_strength *= mask.float()
    
    def get_connectivity_stats(self) -> Dict[str, float]:
        """Get statistics about connection patterns."""
        active_connections = (self.connection_strength > self.connection_threshold).sum().item()
        total_connections = self.connection_strength.numel()
        
        return {
            'active_connections': active_connections,
            'total_connections': total_connections,
            'connectivity_ratio': active_connections / total_connections,
            'mean_strength': self.connection_strength.mean().item(),
            'std_strength': self.connection_strength.std().item()
        }


class CognitiveLinearBlock(NeuralModule):
    """
    Block of multiple linear layers with cognitive routing.
    """
    
    def __init__(self, in_features: int, hidden_features: List[int], 
                 out_features: int, activation: str = 'relu',
                 name: str = "CognitiveLinearBlock"):
        super().__init__(name=name)
        
        self.layers = nn.ModuleList()
        
        # Build layer sequence
        prev_features = in_features
        for hidden_dim in hidden_features:
            self.layers.append(CognitiveLinear(prev_features, hidden_dim))
            prev_features = hidden_dim
        
        # Output layer
        self.layers.append(CognitiveLinear(prev_features, out_features))
        
        # Activation function
        self.activation = self._get_activation(activation)
        
        # Cognitive routing
        self.layer_selector = nn.Linear(in_features, len(self.layers))
    
    def _get_activation(self, activation: str) -> nn.Module:
        """Get activation function by name."""
        activations = {
            'relu': nn.ReLU(),
            'tanh': nn.Tanh(),
            'sigmoid': nn.Sigmoid(),
            'gelu': nn.GELU(),
            'swish': nn.SiLU()
        }
        return activations.get(activation, nn.ReLU())
    
    def _forward_impl(self, x: torch.Tensor, use_routing: bool = False) -> torch.Tensor:
        if use_routing and len(self.layers) > 1:
            return self._forward_with_routing(x)
        else:
            return self._forward_sequential(x)
    
    def _forward_sequential(self, x: torch.Tensor) -> torch.Tensor:
        """Standard sequential forward pass."""
        for i, layer in enumerate(self.layers[:-1]):
            x = self.activation(layer(x))
        
        # No activation on final layer
        x = self.layers[-1](x)
        return x
    
    def _forward_with_routing(self, x: torch.Tensor) -> torch.Tensor:
        """Forward pass with cognitive routing."""
        # Compute routing weights
        routing_logits = self.layer_selector(x)
        routing_weights = F.softmax(routing_logits, dim=-1)
        
        # Apply weighted combination of layer outputs
        outputs = []
        current_x = x
        
        for i, layer in enumerate(self.layers[:-1]):
            layer_output = self.activation(layer(current_x))
            outputs.append(layer_output)
            current_x = layer_output
        
        # Final layer
        final_output = self.layers[-1](current_x)
        
        return final_output

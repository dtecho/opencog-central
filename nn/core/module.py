
"""
Base Neural Module Implementation
=================================

Core module class that all neural network components inherit from.
Provides integration with AtomSpace and cognitive computing features.
"""

import torch
import torch.nn as nn
from typing import Dict, Any, Optional, List, Union, Callable
from abc import ABC, abstractmethod
import logging

logger = logging.getLogger(__name__)


class NeuralModule(nn.Module, ABC):
    """
    Base class for all neural network modules in the OpenCog framework.
    
    Extends PyTorch's nn.Module with AtomSpace integration and cognitive features.
    """
    
    def __init__(self, name: str = None, atomspace_node: Any = None):
        super().__init__()
        self.name = name or self.__class__.__name__
        self.atomspace_node = atomspace_node
        self._attention_values = {}
        self._cognitive_metadata = {}
        self._training_history = []
        
    def forward(self, x: torch.Tensor, *args, **kwargs) -> torch.Tensor:
        """Forward pass through the neural module."""
        return self._forward_impl(x, *args, **kwargs)
    
    @abstractmethod
    def _forward_impl(self, x: torch.Tensor, *args, **kwargs) -> torch.Tensor:
        """Implementation of the forward pass. Must be overridden by subclasses."""
        pass
    
    def set_attention_value(self, sti: float, lti: float = 0.0, vlti: float = 0.0):
        """Set cognitive attention values for this module."""
        self._attention_values = {
            'sti': sti,  # Short-term importance
            'lti': lti,  # Long-term importance
            'vlti': vlti  # Very long-term importance
        }
    
    def get_attention_value(self) -> Dict[str, float]:
        """Get current attention values."""
        return self._attention_values.copy()
    
    def add_cognitive_metadata(self, key: str, value: Any):
        """Add cognitive metadata to this module."""
        self._cognitive_metadata[key] = value
    
    def get_cognitive_metadata(self, key: str = None) -> Any:
        """Get cognitive metadata."""
        if key is None:
            return self._cognitive_metadata.copy()
        return self._cognitive_metadata.get(key)
    
    def log_training_step(self, step: int, loss: float, metrics: Dict[str, float] = None):
        """Log training step information."""
        entry = {
            'step': step,
            'loss': loss,
            'metrics': metrics or {},
            'timestamp': torch.tensor(0.0)  # Placeholder for actual timestamp
        }
        self._training_history.append(entry)
    
    def get_training_history(self) -> List[Dict]:
        """Get training history."""
        return self._training_history.copy()
    
    def reset_parameters(self):
        """Reset module parameters using cognitive-inspired initialization."""
        for module in self.modules():
            if hasattr(module, 'weight') and module.weight is not None:
                # Use Xavier initialization as default
                torch.nn.init.xavier_uniform_(module.weight)
            if hasattr(module, 'bias') and module.bias is not None:
                torch.nn.init.zeros_(module.bias)
    
    def get_parameter_stats(self) -> Dict[str, torch.Tensor]:
        """Get statistics about module parameters."""
        stats = {}
        for name, param in self.named_parameters():
            if param.requires_grad:
                stats[f"{name}_mean"] = param.data.mean()
                stats[f"{name}_std"] = param.data.std()
                stats[f"{name}_min"] = param.data.min()
                stats[f"{name}_max"] = param.data.max()
        return stats
    
    def cognitive_summary(self) -> str:
        """Generate a cognitive summary of this module."""
        summary = [
            f"Neural Module: {self.name}",
            f"Parameters: {sum(p.numel() for p in self.parameters())}",
            f"Trainable: {sum(p.numel() for p in self.parameters() if p.requires_grad)}",
            f"Attention Values: {self._attention_values}",
            f"Metadata Keys: {list(self._cognitive_metadata.keys())}"
        ]
        return "\n".join(summary)


class Sequential(NeuralModule):
    """Sequential container for neural modules."""
    
    def __init__(self, *modules, name: str = "Sequential"):
        super().__init__(name=name)
        self.layers = nn.ModuleList(modules)
    
    def _forward_impl(self, x: torch.Tensor, *args, **kwargs) -> torch.Tensor:
        for layer in self.layers:
            if isinstance(layer, NeuralModule):
                x = layer(x, *args, **kwargs)
            else:
                x = layer(x)
        return x
    
    def add_module_with_attention(self, module: NeuralModule, sti: float):
        """Add a module with specific attention values."""
        module.set_attention_value(sti)
        self.layers.append(module)
    
    def get_layer_attention_summary(self) -> Dict[int, Dict[str, float]]:
        """Get attention values for all layers."""
        summary = {}
        for i, layer in enumerate(self.layers):
            if isinstance(layer, NeuralModule):
                summary[i] = layer.get_attention_value()
        return summary


class ModuleList(NeuralModule):
    """List container for neural modules with cognitive features."""
    
    def __init__(self, modules: List[nn.Module] = None, name: str = "ModuleList"):
        super().__init__(name=name)
        self.modules_list = nn.ModuleList(modules or [])
        self._module_routing = {}
    
    def _forward_impl(self, x: torch.Tensor, routing_key: str = None, *args, **kwargs) -> torch.Tensor:
        """Forward with optional routing based on cognitive attention."""
        if routing_key and routing_key in self._module_routing:
            module_idx = self._module_routing[routing_key]
            return self.modules_list[module_idx](x, *args, **kwargs)
        
        # Default: use module with highest attention
        best_module = self._select_best_module()
        return best_module(x, *args, **kwargs)
    
    def _select_best_module(self) -> nn.Module:
        """Select module based on attention values."""
        best_sti = -float('inf')
        best_module = self.modules_list[0] if self.modules_list else None
        
        for module in self.modules_list:
            if isinstance(module, NeuralModule):
                attention = module.get_attention_value()
                if attention.get('sti', 0) > best_sti:
                    best_sti = attention.get('sti', 0)
                    best_module = module
        
        return best_module or self.modules_list[0]
    
    def set_routing(self, key: str, module_idx: int):
        """Set routing key to specific module index."""
        self._module_routing[key] = module_idx
    
    def append(self, module: nn.Module):
        """Append a module to the list."""
        self.modules_list.append(module)

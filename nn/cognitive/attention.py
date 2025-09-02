
"""
Cognitive Attention Mechanisms
=============================

Attention systems inspired by cognitive science and neuroscience.
"""

import torch
import torch.nn as nn
import torch.nn.functional as F
from typing import Dict, List, Optional, Tuple, Any
from ..core.module import NeuralModule


class AttentionMechanism(NeuralModule):
    """
    Cognitive attention mechanism with focus management.
    """
    
    def __init__(self, feature_dim: int, focus_size: int = 16,
                 saliency_threshold: float = 0.5,
                 name: str = "AttentionMechanism"):
        super().__init__(name=name)
        
        self.feature_dim = feature_dim
        self.focus_size = focus_size
        self.saliency_threshold = saliency_threshold
        
        # Attention focus state
        self.attention_focus = nn.Parameter(
            torch.zeros(focus_size, feature_dim), requires_grad=False
        )
        self.focus_importance = nn.Parameter(
            torch.zeros(focus_size), requires_grad=False
        )
        
        # Saliency computation
        self.saliency_net = nn.Sequential(
            nn.Linear(feature_dim, feature_dim // 2),
            nn.ReLU(),
            nn.Linear(feature_dim // 2, 1),
            nn.Sigmoid()
        )
        
        # Focus update mechanism
        self.focus_updater = nn.GRU(feature_dim, feature_dim, batch_first=True)
        
        # Competition and cooperation
        self.competition_net = nn.Linear(focus_size, focus_size)
        
    def _forward_impl(self, x: torch.Tensor, 
                     update_focus: bool = True) -> Tuple[torch.Tensor, torch.Tensor]:
        """Process input through attention mechanism."""
        batch_size, seq_len, feature_dim = x.size()
        
        # Compute saliency for each element
        saliency_scores = self.saliency_net(x).squeeze(-1)  # [batch, seq_len]
        
        # Update attention focus if requested
        if update_focus:
            self.update_focus(x, saliency_scores)
        
        # Apply attentional weighting
        attention_weights = F.softmax(saliency_scores, dim=-1)
        attended_output = torch.sum(x * attention_weights.unsqueeze(-1), dim=1)
        
        return attended_output, attention_weights
    
    def update_focus(self, stimuli: torch.Tensor, saliency: torch.Tensor):
        """Update attention focus based on current stimuli."""
        with torch.no_grad():
            batch_size, seq_len, feature_dim = stimuli.size()
            
            # Find highly salient items
            high_saliency_mask = saliency > self.saliency_threshold
            
            for b in range(batch_size):
                salient_items = stimuli[b][high_saliency_mask[b]]
                salient_scores = saliency[b][high_saliency_mask[b]]
                
                if salient_items.size(0) > 0:
                    # Add to focus (replace least important if full)
                    for item, score in zip(salient_items, salient_scores):
                        self._add_to_focus(item, score.item())
            
            # Apply competition within focus
            self._apply_focus_competition()
    
    def _add_to_focus(self, item: torch.Tensor, importance: float):
        """Add item to attention focus."""
        # Find slot with lowest importance
        min_importance_idx = torch.argmin(self.focus_importance)
        
        if self.focus_importance[min_importance_idx] < importance:
            self.attention_focus[min_importance_idx] = item
            self.focus_importance[min_importance_idx] = importance
    
    def _apply_focus_competition(self):
        """Apply competitive dynamics within attention focus."""
        if self.focus_importance.sum() == 0:
            return
        
        # Compute competition weights
        competition_weights = F.softmax(self.competition_net(self.focus_importance), dim=0)
        
        # Update importance based on competition
        self.focus_importance *= competition_weights
        
        # Normalize to maintain total attention budget
        self.focus_importance /= (self.focus_importance.sum() + 1e-8)
    
    def get_focus_state(self) -> Dict[str, Any]:
        """Get current attention focus state."""
        return {
            'focus_items': self.attention_focus.clone(),
            'importance_scores': self.focus_importance.clone(),
            'total_importance': self.focus_importance.sum().item(),
            'focus_diversity': torch.std(self.attention_focus.view(-1)).item()
        }
    
    def reset_focus(self):
        """Reset attention focus."""
        with torch.no_grad():
            self.attention_focus.zero_()
            self.focus_importance.zero_()


class FocusManager(NeuralModule):
    """
    Manages multiple attention foci and their interactions.
    """
    
    def __init__(self, feature_dim: int, num_foci: int = 4,
                 focus_size: int = 16, name: str = "FocusManager"):
        super().__init__(name=name)
        
        self.feature_dim = feature_dim
        self.num_foci = num_foci
        self.focus_size = focus_size
        
        # Multiple attention mechanisms
        self.attention_foci = nn.ModuleList([
            AttentionMechanism(feature_dim, focus_size, name=f"Focus_{i}")
            for i in range(num_foci)
        ])
        
        # Focus coordination
        self.focus_coordinator = nn.Linear(feature_dim * num_foci, feature_dim)
        
        # Focus competition
        self.focus_competition = nn.Linear(num_foci, num_foci)
        
    def _forward_impl(self, x: torch.Tensor) -> Tuple[torch.Tensor, List[torch.Tensor]]:
        """Process input through multiple attention foci."""
        focus_outputs = []
        focus_weights = []
        
        # Process through each focus
        for focus in self.attention_foci:
            output, weights = focus(x)
            focus_outputs.append(output)
            focus_weights.append(weights)
        
        # Coordinate focus outputs
        combined_focus = torch.cat(focus_outputs, dim=-1)
        coordinated_output = self.focus_coordinator(combined_focus)
        
        return coordinated_output, focus_weights
    
    def shift_focus(self, focus_id: int, target_importance: float):
        """Shift attention to a specific focus."""
        with torch.no_grad():
            # Increase importance of target focus
            self.attention_foci[focus_id].focus_importance *= (1.0 + target_importance)
            
            # Decrease importance of other foci
            for i, focus in enumerate(self.attention_foci):
                if i != focus_id:
                    focus.focus_importance *= 0.9
    
    def get_global_attention_state(self) -> Dict[str, Any]:
        """Get state of all attention foci."""
        states = {}
        for i, focus in enumerate(self.attention_foci):
            states[f"focus_{i}"] = focus.get_focus_state()
        
        return states

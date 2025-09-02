
"""
Attention Mechanisms
===================

Various attention implementations for cognitive neural networks.
"""

import torch
import torch.nn as nn
import torch.nn.functional as F
import math
from typing import Optional, Tuple, Dict
from ..core.module import NeuralModule


class MultiHeadAttention(NeuralModule):
    """
    Multi-head attention mechanism with cognitive enhancements.
    """
    
    def __init__(self, embed_dim: int, num_heads: int = 8,
                 dropout: float = 0.1, bias: bool = True,
                 name: str = "MultiHeadAttention"):
        super().__init__(name=name)
        
        assert embed_dim % num_heads == 0, "embed_dim must be divisible by num_heads"
        
        self.embed_dim = embed_dim
        self.num_heads = num_heads
        self.head_dim = embed_dim // num_heads
        self.scale = 1.0 / math.sqrt(self.head_dim)
        
        # Linear projections
        self.q_proj = nn.Linear(embed_dim, embed_dim, bias=bias)
        self.k_proj = nn.Linear(embed_dim, embed_dim, bias=bias)
        self.v_proj = nn.Linear(embed_dim, embed_dim, bias=bias)
        self.out_proj = nn.Linear(embed_dim, embed_dim, bias=bias)
        
        # Dropout
        self.dropout = nn.Dropout(dropout)
        
        # Cognitive attention tracking
        self.attention_history = []
        self.max_history_length = 100
        
    def _forward_impl(self, query: torch.Tensor, key: torch.Tensor = None, 
                     value: torch.Tensor = None, attn_mask: Optional[torch.Tensor] = None,
                     return_attention: bool = False) -> torch.Tensor:
        
        if key is None:
            key = query
        if value is None:
            value = query
            
        batch_size, seq_len, embed_dim = query.size()
        
        # Linear projections
        q = self.q_proj(query).view(batch_size, seq_len, self.num_heads, self.head_dim).transpose(1, 2)
        k = self.k_proj(key).view(batch_size, -1, self.num_heads, self.head_dim).transpose(1, 2)
        v = self.v_proj(value).view(batch_size, -1, self.num_heads, self.head_dim).transpose(1, 2)
        
        # Scaled dot-product attention
        attn_weights = torch.matmul(q, k.transpose(-2, -1)) * self.scale
        
        if attn_mask is not None:
            attn_weights += attn_mask
        
        attn_weights = F.softmax(attn_weights, dim=-1)
        attn_weights = self.dropout(attn_weights)
        
        # Store attention patterns for cognitive analysis
        if self.training:
            self._store_attention_pattern(attn_weights.detach())
        
        # Apply attention
        attn_output = torch.matmul(attn_weights, v)
        attn_output = attn_output.transpose(1, 2).contiguous().view(
            batch_size, seq_len, embed_dim)
        
        output = self.out_proj(attn_output)
        
        if return_attention:
            return output, attn_weights
        return output
    
    def _store_attention_pattern(self, attn_weights: torch.Tensor):
        """Store attention patterns for cognitive analysis."""
        pattern_stats = {
            'mean_attention': attn_weights.mean().item(),
            'max_attention': attn_weights.max().item(),
            'entropy': self._compute_attention_entropy(attn_weights),
            'sparsity': (attn_weights < 0.01).float().mean().item()
        }
        
        self.attention_history.append(pattern_stats)
        
        # Keep history bounded
        if len(self.attention_history) > self.max_history_length:
            self.attention_history.pop(0)
    
    def _compute_attention_entropy(self, attn_weights: torch.Tensor) -> float:
        """Compute entropy of attention distribution."""
        # Average over batch and heads
        avg_attention = attn_weights.mean(dim=(0, 1))
        
        # Compute entropy
        entropy = -torch.sum(avg_attention * torch.log(avg_attention + 1e-8))
        return entropy.item()
    
    def get_attention_stats(self) -> Dict[str, float]:
        """Get aggregated attention statistics."""
        if not self.attention_history:
            return {}
        
        stats = {}
        for key in self.attention_history[0].keys():
            values = [h[key] for h in self.attention_history]
            stats[f"mean_{key}"] = sum(values) / len(values)
            stats[f"std_{key}"] = torch.tensor(values).std().item()
        
        return stats


class CognitiveAttention(NeuralModule):
    """
    Simplified attention mechanism inspired by cognitive processes.
    """
    
    def __init__(self, feature_dim: int, attention_dim: int = None,
                 temperature: float = 1.0, name: str = "CognitiveAttention"):
        super().__init__(name=name)
        
        self.feature_dim = feature_dim
        self.attention_dim = attention_dim or feature_dim // 2
        self.temperature = temperature
        
        # Attention computation network
        self.attention_net = nn.Sequential(
            nn.Linear(feature_dim, self.attention_dim),
            nn.ReLU(),
            nn.Linear(self.attention_dim, 1)
        )
        
        # Context integration
        self.context_gate = nn.Linear(feature_dim, feature_dim)
        
    def _forward_impl(self, x: torch.Tensor, context: Optional[torch.Tensor] = None) -> torch.Tensor:
        batch_size, seq_len, feature_dim = x.size()
        
        # Compute attention scores
        attention_scores = self.attention_net(x).squeeze(-1)  # [batch, seq_len]
        attention_weights = F.softmax(attention_scores / self.temperature, dim=-1)
        
        # Apply attention
        attended_features = torch.sum(x * attention_weights.unsqueeze(-1), dim=1)  # [batch, feature_dim]
        
        # Context integration if provided
        if context is not None:
            gate_values = torch.sigmoid(self.context_gate(context))
            attended_features = attended_features * gate_values
        
        return attended_features, attention_weights


class SelfAttention(NeuralModule):
    """
    Self-attention mechanism for sequence modeling.
    """
    
    def __init__(self, embed_dim: int, num_heads: int = 1,
                 name: str = "SelfAttention"):
        super().__init__(name=name)
        
        self.embed_dim = embed_dim
        self.num_heads = num_heads
        self.head_dim = embed_dim // num_heads
        
        assert embed_dim % num_heads == 0
        
        self.qkv_proj = nn.Linear(embed_dim, 3 * embed_dim)
        self.out_proj = nn.Linear(embed_dim, embed_dim)
        
    def _forward_impl(self, x: torch.Tensor, mask: Optional[torch.Tensor] = None) -> torch.Tensor:
        batch_size, seq_len, embed_dim = x.size()
        
        # Compute Q, K, V
        qkv = self.qkv_proj(x)
        qkv = qkv.view(batch_size, seq_len, 3, self.num_heads, self.head_dim)
        qkv = qkv.permute(2, 0, 3, 1, 4)  # [3, batch, heads, seq_len, head_dim]
        
        q, k, v = qkv[0], qkv[1], qkv[2]
        
        # Scaled dot-product attention
        attn_scores = torch.matmul(q, k.transpose(-2, -1)) / math.sqrt(self.head_dim)
        
        if mask is not None:
            attn_scores.masked_fill_(mask == 0, float('-inf'))
        
        attn_weights = F.softmax(attn_scores, dim=-1)
        attn_output = torch.matmul(attn_weights, v)
        
        # Reshape and project
        attn_output = attn_output.transpose(1, 2).contiguous().view(
            batch_size, seq_len, embed_dim)
        
        output = self.out_proj(attn_output)
        return output


"""
Cognitive Memory Systems
=======================

Implementation of various memory systems for cognitive neural networks.
"""

import torch
import torch.nn as nn
import torch.nn.functional as F
from typing import List, Dict, Optional, Tuple, Any
from collections import deque
import numpy as np
from ..core.module import NeuralModule


class WorkingMemory(NeuralModule):
    """
    Working memory system with limited capacity and decay.
    """
    
    def __init__(self, capacity: int, feature_dim: int, 
                 decay_rate: float = 0.95, name: str = "WorkingMemory"):
        super().__init__(name=name)
        
        self.capacity = capacity
        self.feature_dim = feature_dim
        self.decay_rate = decay_rate
        
        # Memory storage
        self.memory_buffer = nn.Parameter(
            torch.zeros(capacity, feature_dim), requires_grad=False
        )
        self.importance_scores = nn.Parameter(
            torch.zeros(capacity), requires_grad=False
        )
        self.age_scores = nn.Parameter(
            torch.zeros(capacity), requires_grad=False
        )
        
        # Memory management
        self.current_size = 0
        self.write_pointer = 0
        
        # Integration networks
        self.memory_gate = nn.Linear(feature_dim, feature_dim)
        self.retrieval_net = nn.Linear(feature_dim * 2, feature_dim)
        
    def _forward_impl(self, x: torch.Tensor) -> torch.Tensor:
        """Process input through working memory."""
        return self.integrate(x)
    
    def store(self, item: torch.Tensor, importance: float = 1.0):
        """Store an item in working memory."""
        with torch.no_grad():
            if self.current_size < self.capacity:
                # Add to empty slot
                self.memory_buffer[self.current_size] = item
                self.importance_scores[self.current_size] = importance
                self.age_scores[self.current_size] = 0.0
                self.current_size += 1
            else:
                # Replace least important item
                least_important_idx = torch.argmin(
                    self.importance_scores * torch.exp(-0.1 * self.age_scores)
                )
                self.memory_buffer[least_important_idx] = item
                self.importance_scores[least_important_idx] = importance
                self.age_scores[least_important_idx] = 0.0
            
            # Age all items
            self.age_scores += 1.0
            
            # Decay importance
            self.importance_scores *= self.decay_rate
    
    def retrieve(self, query: torch.Tensor, k: int = 5) -> Tuple[torch.Tensor, torch.Tensor]:
        """Retrieve k most relevant items from memory."""
        if self.current_size == 0:
            return torch.zeros(k, self.feature_dim), torch.zeros(k)
        
        # Compute similarities
        memory_items = self.memory_buffer[:self.current_size]
        similarities = F.cosine_similarity(
            query.unsqueeze(0), memory_items, dim=-1
        )
        
        # Weight by importance
        retrieval_scores = similarities * self.importance_scores[:self.current_size]
        
        # Get top-k
        k = min(k, self.current_size)
        top_k_scores, top_k_indices = torch.topk(retrieval_scores, k)
        
        retrieved_items = memory_items[top_k_indices]
        
        return retrieved_items, top_k_scores
    
    def integrate(self, x: torch.Tensor) -> torch.Tensor:
        """Integrate current input with working memory."""
        batch_size, seq_len, feature_dim = x.size()
        
        # Store current input in memory
        current_item = x.mean(dim=1).mean(dim=0)  # Average over batch and sequence
        self.store(current_item)
        
        # Retrieve relevant memories
        query = x.view(-1, feature_dim).mean(dim=0)
        retrieved_memories, scores = self.retrieve(query)
        
        if retrieved_memories.size(0) > 0:
            # Compute memory context
            memory_context = torch.sum(
                retrieved_memories * scores.unsqueeze(-1), dim=0
            ) / (scores.sum() + 1e-8)
            
            # Integrate with current input
            gate_values = torch.sigmoid(self.memory_gate(memory_context))
            
            # Apply memory integration
            integrated = x + gate_values.unsqueeze(0).unsqueeze(0) * memory_context.unsqueeze(0).unsqueeze(0)
        else:
            integrated = x
        
        return integrated
    
    def get_usage_ratio(self) -> float:
        """Get current memory usage ratio."""
        return self.current_size / self.capacity
    
    def get_state(self) -> Dict[str, Any]:
        """Get current memory state."""
        return {
            'size': self.current_size,
            'capacity': self.capacity,
            'usage_ratio': self.get_usage_ratio(),
            'mean_importance': self.importance_scores[:self.current_size].mean().item() if self.current_size > 0 else 0.0,
            'mean_age': self.age_scores[:self.current_size].mean().item() if self.current_size > 0 else 0.0
        }
    
    def get_high_importance_items(self, threshold: float = 0.7) -> List[torch.Tensor]:
        """Get items with importance above threshold."""
        if self.current_size == 0:
            return []
        
        high_importance_mask = self.importance_scores[:self.current_size] > threshold
        return [self.memory_buffer[i] for i in range(self.current_size) 
                if high_importance_mask[i]]
    
    def consolidate(self):
        """Consolidate memory by removing low-importance items."""
        if self.current_size == 0:
            return
        
        with torch.no_grad():
            # Keep only top 50% most important items
            keep_ratio = 0.5
            keep_count = max(1, int(self.current_size * keep_ratio))
            
            # Sort by importance
            importance_order = torch.argsort(
                self.importance_scores[:self.current_size], descending=True
            )
            
            # Reorganize memory
            new_buffer = torch.zeros_like(self.memory_buffer)
            new_importance = torch.zeros_like(self.importance_scores)
            new_age = torch.zeros_like(self.age_scores)
            
            for i, old_idx in enumerate(importance_order[:keep_count]):
                new_buffer[i] = self.memory_buffer[old_idx]
                new_importance[i] = self.importance_scores[old_idx]
                new_age[i] = self.age_scores[old_idx]
            
            self.memory_buffer.copy_(new_buffer)
            self.importance_scores.copy_(new_importance)
            self.age_scores.copy_(new_age)
            self.current_size = keep_count


class EpisodicMemory(NeuralModule):
    """
    Episodic memory system for storing temporal sequences.
    """
    
    def __init__(self, capacity: int, feature_dim: int,
                 sequence_length: int = 10, name: str = "EpisodicMemory"):
        super().__init__(name=name)
        
        self.capacity = capacity
        self.feature_dim = feature_dim
        self.sequence_length = sequence_length
        
        # Episode storage
        self.episodes = deque(maxlen=capacity)
        self.episode_importance = deque(maxlen=capacity)
        
        # Retrieval mechanism
        self.episode_encoder = nn.LSTM(
            feature_dim, feature_dim // 2, batch_first=True
        )
        self.similarity_net = nn.Linear(feature_dim, feature_dim // 2)
        
    def _forward_impl(self, x: torch.Tensor) -> torch.Tensor:
        """Process input and optionally retrieve relevant episodes."""
        # This is mainly a storage/retrieval system
        return x
    
    def store_episode(self, sequence: torch.Tensor, importance: float = 1.0):
        """Store an episodic sequence."""
        if sequence.dim() == 2:
            sequence = sequence.unsqueeze(0)  # Add batch dimension if needed
        
        # Truncate or pad sequence to fixed length
        if sequence.size(1) > self.sequence_length:
            sequence = sequence[:, -self.sequence_length:]
        elif sequence.size(1) < self.sequence_length:
            padding = torch.zeros(
                sequence.size(0), 
                self.sequence_length - sequence.size(1),
                sequence.size(2)
            )
            sequence = torch.cat([sequence, padding], dim=1)
        
        self.episodes.append(sequence.detach().cpu())
        self.episode_importance.append(importance)
    
    def retrieve_similar_episodes(self, query: torch.Tensor, k: int = 5) -> List[torch.Tensor]:
        """Retrieve episodes similar to the query."""
        if not self.episodes:
            return []
        
        # Encode query
        query_encoded, _ = self.episode_encoder(query.unsqueeze(0))
        query_embedding = query_encoded.mean(dim=1)
        
        # Compute similarities with all episodes
        similarities = []
        for episode in self.episodes:
            episode_encoded, _ = self.episode_encoder(episode)
            episode_embedding = episode_encoded.mean(dim=1)
            
            similarity = F.cosine_similarity(
                query_embedding, episode_embedding, dim=-1
            ).mean().item()
            similarities.append(similarity)
        
        # Get top-k most similar
        top_k_indices = np.argsort(similarities)[-k:][::-1]
        
        return [self.episodes[i] for i in top_k_indices]
    
    def get_recent_episodes(self, k: int = 10) -> List[torch.Tensor]:
        """Get k most recent episodes."""
        return list(self.episodes)[-k:]
    
    def consolidate_episodes(self):
        """Consolidate episodes by importance."""
        if len(self.episodes) < self.capacity:
            return
        
        # Keep episodes with highest importance
        importance_array = np.array(list(self.episode_importance))
        keep_indices = np.argsort(importance_array)[-self.capacity//2:]
        
        new_episodes = deque(maxlen=self.capacity)
        new_importance = deque(maxlen=self.capacity)
        
        for idx in keep_indices:
            new_episodes.append(self.episodes[idx])
            new_importance.append(self.episode_importance[idx])
        
        self.episodes = new_episodes
        self.episode_importance = new_importance


class LongTermMemory(NeuralModule):
    """
    Long-term memory system with semantic organization.
    """
    
    def __init__(self, feature_dim: int, num_concepts: int = 1000,
                 name: str = "LongTermMemory"):
        super().__init__(name=name)
        
        self.feature_dim = feature_dim
        self.num_concepts = num_concepts
        
        # Concept embeddings
        self.concept_embeddings = nn.Embedding(num_concepts, feature_dim)
        
        # Semantic organization
        self.concept_relations = nn.Parameter(
            torch.zeros(num_concepts, num_concepts)
        )
        
        # Access and update mechanisms
        self.access_net = nn.Linear(feature_dim, num_concepts)
        self.update_net = nn.Linear(feature_dim * 2, feature_dim)
        
        self.reset_parameters()
    
    def _forward_impl(self, x: torch.Tensor, concept_ids: Optional[torch.Tensor] = None) -> torch.Tensor:
        """Access long-term memory concepts."""
        if concept_ids is not None:
            # Direct concept access
            concepts = self.concept_embeddings(concept_ids)
            return concepts
        else:
            # Content-based retrieval
            return self.retrieve_by_content(x)
    
    def retrieve_by_content(self, query: torch.Tensor, k: int = 5) -> torch.Tensor:
        """Retrieve concepts based on content similarity."""
        # Compute access weights
        access_weights = F.softmax(self.access_net(query), dim=-1)
        
        # Get top-k concepts
        top_k_weights, top_k_indices = torch.topk(access_weights, k, dim=-1)
        
        # Retrieve concept embeddings
        retrieved_concepts = self.concept_embeddings(top_k_indices)
        
        # Weight by access scores
        weighted_concepts = retrieved_concepts * top_k_weights.unsqueeze(-1)
        
        return weighted_concepts.sum(dim=-2)  # Sum over k concepts
    
    def update_concept(self, concept_id: int, new_info: torch.Tensor):
        """Update a specific concept with new information."""
        with torch.no_grad():
            current_concept = self.concept_embeddings.weight[concept_id]
            
            # Compute update
            combined = torch.cat([current_concept, new_info], dim=-1)
            updated_concept = self.update_net(combined)
            
            # Apply update with momentum
            self.concept_embeddings.weight[concept_id] = \
                0.9 * current_concept + 0.1 * updated_concept
    
    def strengthen_relation(self, concept1_id: int, concept2_id: int, strength: float = 0.1):
        """Strengthen relationship between two concepts."""
        with torch.no_grad():
            self.concept_relations[concept1_id, concept2_id] += strength
            self.concept_relations[concept2_id, concept1_id] += strength
            
            # Keep relations normalized
            self.concept_relations.clamp_(0.0, 1.0)
    
    def get_related_concepts(self, concept_id: int, k: int = 5) -> Tuple[torch.Tensor, torch.Tensor]:
        """Get k most related concepts."""
        relations = self.concept_relations[concept_id]
        top_k_scores, top_k_indices = torch.topk(relations, k)
        
        related_concepts = self.concept_embeddings(top_k_indices)
        
        return related_concepts, top_k_scores
    
    def semantic_clustering(self) -> Dict[int, List[int]]:
        """Perform semantic clustering of concepts."""
        # Compute concept similarities
        embeddings = self.concept_embeddings.weight
        similarities = F.cosine_similarity(
            embeddings.unsqueeze(1), embeddings.unsqueeze(0), dim=-1
        )
        
        # Simple clustering based on similarity threshold
        clusters = {}
        visited = set()
        cluster_id = 0
        
        for i in range(self.num_concepts):
            if i in visited:
                continue
            
            # Find similar concepts
            similar_concepts = torch.where(similarities[i] > 0.7)[0].tolist()
            
            if similar_concepts:
                clusters[cluster_id] = similar_concepts
                visited.update(similar_concepts)
                cluster_id += 1
        
        return clusters

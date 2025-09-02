
"""
Cognitive Neural Network Trainer
===============================

Training framework with cognitive-inspired features.
"""

import torch
import torch.nn as nn
from typing import Dict, List, Optional, Any, Callable
import logging
from ..core.module import NeuralModule
from .loss import CognitiveLoss
from .optimizer import CognitiveOptimizer

logger = logging.getLogger(__name__)


class CognitiveTrainer:
    """
    Trainer for cognitive neural networks with adaptive learning.
    """
    
    def __init__(self, model: NeuralModule, 
                 optimizer: torch.optim.Optimizer = None,
                 loss_fn: nn.Module = None,
                 device: str = 'cpu'):
        
        self.model = model
        self.device = device
        self.model.to(device)
        
        # Default optimizer and loss
        self.optimizer = optimizer or CognitiveOptimizer(model.parameters())
        self.loss_fn = loss_fn or CognitiveLoss()
        
        # Training state
        self.epoch = 0
        self.global_step = 0
        self.training_history = []
        
        # Cognitive training parameters
        self.attention_regularization = True
        self.memory_consolidation_interval = 100
        self.adaptation_rate = 0.01
        
        # Performance tracking
        self.best_loss = float('inf')
        self.patience_counter = 0
        self.early_stopping_patience = 50
        
    def train_epoch(self, dataloader, validation_loader=None) -> Dict[str, float]:
        """Train for one epoch."""
        self.model.train()
        
        epoch_losses = []
        epoch_metrics = {}
        
        for batch_idx, batch in enumerate(dataloader):
            # Move batch to device
            if isinstance(batch, (list, tuple)):
                batch = [b.to(self.device) if torch.is_tensor(b) else b for b in batch]
            else:
                batch = batch.to(self.device)
            
            # Training step
            loss, metrics = self.train_step(batch)
            
            epoch_losses.append(loss)
            
            # Accumulate metrics
            for key, value in metrics.items():
                if key not in epoch_metrics:
                    epoch_metrics[key] = []
                epoch_metrics[key].append(value)
            
            # Log progress
            if batch_idx % 100 == 0:
                logger.info(f"Epoch {self.epoch}, Batch {batch_idx}, Loss: {loss:.6f}")
            
            # Memory consolidation
            if self.global_step % self.memory_consolidation_interval == 0:
                self._consolidate_memory()
        
        # Compute epoch averages
        avg_loss = sum(epoch_losses) / len(epoch_losses)
        avg_metrics = {key: sum(values) / len(values) 
                      for key, values in epoch_metrics.items()}
        
        # Validation
        val_metrics = {}
        if validation_loader is not None:
            val_metrics = self.validate(validation_loader)
        
        # Update training history
        epoch_record = {
            'epoch': self.epoch,
            'train_loss': avg_loss,
            'train_metrics': avg_metrics,
            'val_metrics': val_metrics,
            'cognitive_state': self.model.get_cognitive_state() if hasattr(self.model, 'get_cognitive_state') else {}
        }
        self.training_history.append(epoch_record)
        
        # Adaptive learning rate
        if hasattr(self.model, 'adapt_learning_rate'):
            current_lr = self.optimizer.param_groups[0]['lr']
            new_lr = self.model.adapt_learning_rate(current_lr)
            for param_group in self.optimizer.param_groups:
                param_group['lr'] = new_lr
        
        self.epoch += 1
        
        return {**avg_metrics, 'loss': avg_loss, **val_metrics}
    
    def train_step(self, batch) -> Tuple[float, Dict[str, float]]:
        """Single training step."""
        self.optimizer.zero_grad()
        
        # Extract inputs and targets
        if isinstance(batch, (list, tuple)) and len(batch) >= 2:
            inputs, targets = batch[0], batch[1]
        else:
            inputs = batch
            targets = None
        
        # Forward pass
        outputs = self.model(inputs)
        
        # Compute loss
        if targets is not None:
            loss = self.loss_fn(outputs, targets)
        else:
            # Self-supervised or unsupervised loss
            loss = self.loss_fn(outputs, inputs)
        
        # Add cognitive regularization
        if self.attention_regularization:
            loss += self._compute_attention_regularization()
        
        # Backward pass
        loss.backward()
        
        # Gradient clipping
        torch.nn.utils.clip_grad_norm_(self.model.parameters(), max_norm=1.0)
        
        # Optimizer step
        self.optimizer.step()
        
        # Update cognitive components
        self._update_cognitive_components(loss.item())
        
        # Compute metrics
        metrics = self._compute_metrics(outputs, targets if targets is not None else inputs)
        
        # Log training step in model
        if hasattr(self.model, 'log_training_step'):
            self.model.log_training_step(self.global_step, loss.item(), metrics)
        
        self.global_step += 1
        
        return loss.item(), metrics
    
    def validate(self, validation_loader) -> Dict[str, float]:
        """Validate model on validation set."""
        self.model.eval()
        
        val_losses = []
        val_metrics = {}
        
        with torch.no_grad():
            for batch in validation_loader:
                # Move batch to device
                if isinstance(batch, (list, tuple)):
                    batch = [b.to(self.device) if torch.is_tensor(b) else b for b in batch]
                else:
                    batch = batch.to(self.device)
                
                # Extract inputs and targets
                if isinstance(batch, (list, tuple)) and len(batch) >= 2:
                    inputs, targets = batch[0], batch[1]
                else:
                    inputs = batch
                    targets = None
                
                # Forward pass
                outputs = self.model(inputs)
                
                # Compute loss
                if targets is not None:
                    loss = self.loss_fn(outputs, targets)
                else:
                    loss = self.loss_fn(outputs, inputs)
                
                val_losses.append(loss.item())
                
                # Compute metrics
                metrics = self._compute_metrics(outputs, targets if targets is not None else inputs)
                
                # Accumulate metrics
                for key, value in metrics.items():
                    if key not in val_metrics:
                        val_metrics[key] = []
                    val_metrics[key].append(value)
        
        # Average metrics
        avg_val_loss = sum(val_losses) / len(val_losses)
        avg_val_metrics = {f"val_{key}": sum(values) / len(values) 
                          for key, values in val_metrics.items()}
        
        avg_val_metrics['val_loss'] = avg_val_loss
        
        # Early stopping check
        if avg_val_loss < self.best_loss:
            self.best_loss = avg_val_loss
            self.patience_counter = 0
        else:
            self.patience_counter += 1
        
        return avg_val_metrics
    
    def _compute_attention_regularization(self) -> torch.Tensor:
        """Compute regularization based on attention patterns."""
        reg_loss = torch.tensor(0.0, device=self.device)
        
        # Regularize attention weights to prevent over-concentration
        for module in self.model.modules():
            if hasattr(module, 'get_attention_stats'):
                stats = module.get_attention_stats()
                if 'mean_entropy' in stats:
                    # Encourage diverse attention
                    target_entropy = 2.0  # Desired entropy level
                    entropy_diff = abs(stats['mean_entropy'] - target_entropy)
                    reg_loss += 0.01 * entropy_diff
        
        return reg_loss
    
    def _compute_metrics(self, outputs: torch.Tensor, targets: torch.Tensor) -> Dict[str, float]:
        """Compute training metrics."""
        metrics = {}
        
        with torch.no_grad():
            # Basic metrics
            if outputs.dim() == targets.dim():
                mse = F.mse_loss(outputs, targets)
                metrics['mse'] = mse.item()
                
                # Cosine similarity
                cos_sim = F.cosine_similarity(
                    outputs.view(-1), targets.view(-1), dim=0
                )
                metrics['cosine_similarity'] = cos_sim.item()
            
            # Output statistics
            metrics['output_mean'] = outputs.mean().item()
            metrics['output_std'] = outputs.std().item()
            metrics['output_max'] = outputs.max().item()
            metrics['output_min'] = outputs.min().item()
        
        return metrics
    
    def _update_cognitive_components(self, loss: float):
        """Update cognitive components based on training feedback."""
        # Update attention values based on performance
        attention_update = 1.0 / (1.0 + loss)  # Better performance -> higher attention
        
        if hasattr(self.model, 'set_attention_value'):
            current_attention = self.model.get_attention_value()
            new_sti = current_attention.get('sti', 0.5) * 0.9 + attention_update * 0.1
            self.model.set_attention_value(new_sti)
    
    def _consolidate_memory(self):
        """Trigger memory consolidation in cognitive components."""
        if hasattr(self.model, 'consolidate_memory'):
            self.model.consolidate_memory()
        
        # Consolidate individual memory systems
        for module in self.model.modules():
            if hasattr(module, 'consolidate'):
                module.consolidate()
    
    def should_stop_early(self) -> bool:
        """Check if training should stop early."""
        return self.patience_counter >= self.early_stopping_patience
    
    def save_checkpoint(self, filepath: str, include_optimizer: bool = True):
        """Save training checkpoint."""
        checkpoint = {
            'model_state_dict': self.model.state_dict(),
            'epoch': self.epoch,
            'global_step': self.global_step,
            'best_loss': self.best_loss,
            'training_history': self.training_history,
            'cognitive_state': self.model.get_cognitive_state() if hasattr(self.model, 'get_cognitive_state') else {}
        }
        
        if include_optimizer:
            checkpoint['optimizer_state_dict'] = self.optimizer.state_dict()
        
        torch.save(checkpoint, filepath)
        logger.info(f"Checkpoint saved to {filepath}")
    
    def load_checkpoint(self, filepath: str, load_optimizer: bool = True):
        """Load training checkpoint."""
        checkpoint = torch.load(filepath, map_location=self.device)
        
        self.model.load_state_dict(checkpoint['model_state_dict'])
        self.epoch = checkpoint.get('epoch', 0)
        self.global_step = checkpoint.get('global_step', 0)
        self.best_loss = checkpoint.get('best_loss', float('inf'))
        self.training_history = checkpoint.get('training_history', [])
        
        if load_optimizer and 'optimizer_state_dict' in checkpoint:
            self.optimizer.load_state_dict(checkpoint['optimizer_state_dict'])
        
        logger.info(f"Checkpoint loaded from {filepath}")
    
    def get_training_summary(self) -> str:
        """Generate training summary."""
        if not self.training_history:
            return "No training history available"
        
        latest = self.training_history[-1]
        
        summary = [
            f"Training Summary for {self.model.name}",
            f"Epoch: {self.epoch}",
            f"Global Step: {self.global_step}",
            f"Best Loss: {self.best_loss:.6f}",
            f"Current Loss: {latest.get('train_loss', 'N/A')}",
            f"Patience Counter: {self.patience_counter}/{self.early_stopping_patience}",
            "",
            "Latest Metrics:",
        ]
        
        for key, value in latest.get('train_metrics', {}).items():
            summary.append(f"  {key}: {value:.6f}")
        
        return "\n".join(summary)

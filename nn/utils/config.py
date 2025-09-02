
"""
Configuration Management
========================

Configuration utilities for cognitive neural networks.
"""

import torch
import yaml
import json
from typing import Dict, Any, Optional, List
from pathlib import Path
import logging

logger = logging.getLogger(__name__)


class ConfigManager:
    """
    Manages configuration for cognitive neural networks.
    """
    
    def __init__(self, config_path: Optional[str] = None):
        self.config_path = config_path
        self.config = {}
        
        if config_path:
            self.load_config(config_path)
        else:
            self.config = self.get_default_config()
    
    def get_default_config(self) -> Dict[str, Any]:
        """Get default configuration for cognitive networks."""
        return {
            'model': {
                'input_dim': 512,
                'hidden_dim': 1024,
                'output_dim': 256,
                'num_layers': 3,
                'attention_heads': 8,
                'dropout': 0.1
            },
            'cognitive': {
                'working_memory_capacity': 64,
                'episodic_memory_capacity': 1000,
                'attention_focus_size': 16,
                'memory_decay_rate': 0.95,
                'attention_temperature': 1.0
            },
            'training': {
                'learning_rate': 1e-3,
                'batch_size': 32,
                'max_epochs': 100,
                'early_stopping_patience': 10,
                'gradient_clip_norm': 1.0,
                'weight_decay': 1e-4
            },
            'atomspace': {
                'enable_integration': True,
                'sync_interval': 100,
                'concept_threshold': 0.5,
                'max_concepts': 10000
            },
            'logging': {
                'level': 'INFO',
                'log_interval': 10,
                'save_checkpoints': True,
                'checkpoint_interval': 1000
            }
        }
    
    def load_config(self, config_path: str):
        """Load configuration from file."""
        path = Path(config_path)
        
        if not path.exists():
            logger.warning(f"Config file {config_path} not found, using defaults")
            self.config = self.get_default_config()
            return
        
        try:
            with open(path, 'r') as f:
                if path.suffix.lower() in ['.yaml', '.yml']:
                    self.config = yaml.safe_load(f)
                elif path.suffix.lower() == '.json':
                    self.config = json.load(f)
                else:
                    raise ValueError(f"Unsupported config format: {path.suffix}")
            
            # Merge with defaults
            self.config = self._merge_configs(self.get_default_config(), self.config)
            
            logger.info(f"Configuration loaded from {config_path}")
            
        except Exception as e:
            logger.error(f"Failed to load config from {config_path}: {e}")
            self.config = self.get_default_config()
    
    def save_config(self, config_path: str):
        """Save current configuration to file."""
        path = Path(config_path)
        path.parent.mkdir(parents=True, exist_ok=True)
        
        try:
            with open(path, 'w') as f:
                if path.suffix.lower() in ['.yaml', '.yml']:
                    yaml.dump(self.config, f, default_flow_style=False)
                elif path.suffix.lower() == '.json':
                    json.dump(self.config, f, indent=2)
                else:
                    raise ValueError(f"Unsupported config format: {path.suffix}")
            
            logger.info(f"Configuration saved to {config_path}")
            
        except Exception as e:
            logger.error(f"Failed to save config to {config_path}: {e}")
    
    def get(self, key: str, default: Any = None) -> Any:
        """Get configuration value using dot notation."""
        keys = key.split('.')
        value = self.config
        
        for k in keys:
            if isinstance(value, dict) and k in value:
                value = value[k]
            else:
                return default
        
        return value
    
    def set(self, key: str, value: Any):
        """Set configuration value using dot notation."""
        keys = key.split('.')
        config = self.config
        
        for k in keys[:-1]:
            if k not in config:
                config[k] = {}
            config = config[k]
        
        config[keys[-1]] = value
    
    def _merge_configs(self, default: Dict, custom: Dict) -> Dict:
        """Recursively merge custom config with default."""
        merged = default.copy()
        
        for key, value in custom.items():
            if key in merged and isinstance(merged[key], dict) and isinstance(value, dict):
                merged[key] = self._merge_configs(merged[key], value)
            else:
                merged[key] = value
        
        return merged
    
    def validate_config(self) -> List[str]:
        """Validate configuration and return list of issues."""
        issues = []
        
        # Check required fields
        required_fields = [
            'model.input_dim',
            'model.hidden_dim', 
            'model.output_dim',
            'training.learning_rate',
            'training.batch_size'
        ]
        
        for field in required_fields:
            if self.get(field) is None:
                issues.append(f"Missing required field: {field}")
        
        # Check value ranges
        if self.get('training.learning_rate', 0) <= 0:
            issues.append("Learning rate must be positive")
        
        if self.get('training.batch_size', 0) <= 0:
            issues.append("Batch size must be positive")
        
        if self.get('model.num_layers', 0) <= 0:
            issues.append("Number of layers must be positive")
        
        return issues
    
    def get_model_config(self) -> Dict[str, Any]:
        """Get model-specific configuration."""
        return self.config.get('model', {})
    
    def get_training_config(self) -> Dict[str, Any]:
        """Get training-specific configuration."""
        return self.config.get('training', {})
    
    def get_cognitive_config(self) -> Dict[str, Any]:
        """Get cognitive-specific configuration."""
        return self.config.get('cognitive', {})


class HyperparameterTuner:
    """
    Automated hyperparameter tuning for cognitive networks.
    """
    
    def __init__(self, config_manager: ConfigManager):
        self.config_manager = config_manager
        self.search_space = {}
        self.best_config = None
        self.best_score = float('-inf')
        self.trial_history = []
    
    def define_search_space(self, search_space: Dict[str, Dict[str, Any]]):
        """
        Define hyperparameter search space.
        
        Example:
        {
            'model.hidden_dim': {'type': 'choice', 'values': [512, 1024, 2048]},
            'training.learning_rate': {'type': 'uniform', 'low': 1e-5, 'high': 1e-2},
            'cognitive.attention_focus_size': {'type': 'int', 'low': 8, 'high': 32}
        }
        """
        self.search_space = search_space
    
    def sample_config(self) -> Dict[str, Any]:
        """Sample a configuration from the search space."""
        import random
        
        sampled_config = self.config_manager.config.copy()
        
        for param_path, param_spec in self.search_space.items():
            if param_spec['type'] == 'choice':
                value = random.choice(param_spec['values'])
            elif param_spec['type'] == 'uniform':
                value = random.uniform(param_spec['low'], param_spec['high'])
            elif param_spec['type'] == 'int':
                value = random.randint(param_spec['low'], param_spec['high'])
            elif param_spec['type'] == 'log_uniform':
                log_low = torch.log10(torch.tensor(param_spec['low']))
                log_high = torch.log10(torch.tensor(param_spec['high']))
                log_value = random.uniform(log_low, log_high)
                value = 10 ** log_value
            else:
                continue
            
            # Set the sampled value
            self.config_manager.set(param_path, value)
        
        return self.config_manager.config.copy()
    
    def update_best(self, config: Dict[str, Any], score: float):
        """Update best configuration if score improves."""
        if score > self.best_score:
            self.best_score = score
            self.best_config = config.copy()
            logger.info(f"New best score: {score:.6f}")
        
        # Record trial
        self.trial_history.append({
            'config': config.copy(),
            'score': score
        })
    
    def get_optimization_summary(self) -> Dict[str, Any]:
        """Get summary of optimization process."""
        if not self.trial_history:
            return {'message': 'No trials completed'}
        
        scores = [trial['score'] for trial in self.trial_history]
        
        return {
            'num_trials': len(self.trial_history),
            'best_score': self.best_score,
            'mean_score': sum(scores) / len(scores),
            'std_score': torch.tensor(scores).std().item(),
            'improvement': scores[-1] - scores[0] if len(scores) > 1 else 0.0,
            'best_config': self.best_config
        }

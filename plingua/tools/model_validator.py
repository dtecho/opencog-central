
"""
P-Lingua Model Validator

Validates P-Lingua models for syntax and semantic correctness.
"""

import re
import sys
from typing import List, Dict, Set, Tuple
from pathlib import Path

class ModelValidator:
    def __init__(self):
        self.errors = []
        self.warnings = []
        
    def validate_file(self, file_path: str) -> bool:
        """Validate a P-Lingua model file."""
        try:
            with open(file_path, 'r') as f:
                content = f.read()
            
            return self.validate_model(content, file_path)
        except FileNotFoundError:
            self.errors.append(f"File not found: {file_path}")
            return False
        except Exception as e:
            self.errors.append(f"Error reading file {file_path}: {e}")
            return False
    
    def validate_model(self, content: str, filename: str = "") -> bool:
        """Validate P-Lingua model content."""
        lines = content.split('\n')
        
        # Check for required sections
        has_model = self._check_model_declaration(lines)
        has_mu = self._check_initial_configuration(lines)
        has_rules = self._check_rules(lines)
        
        if not has_model:
            self.errors.append(f"Missing @model declaration in {filename}")
        
        if not has_mu:
            self.errors.append(f"Missing @mu (initial configuration) in {filename}")
        
        if not has_rules:
            self.warnings.append(f"No rules found in {filename}")
        
        # Validate syntax
        self._validate_syntax(lines, filename)
        
        return len(self.errors) == 0
    
    def _check_model_declaration(self, lines: List[str]) -> bool:
        """Check for @model<name> declaration."""
        model_pattern = r'@model<\w+>'
        return any(re.search(model_pattern, line.strip()) for line in lines)
    
    def _check_initial_configuration(self, lines: List[str]) -> bool:
        """Check for @mu initial configuration."""
        return any(line.strip().startswith('@mu') for line in lines)
    
    def _check_rules(self, lines: List[str]) -> bool:
        """Check for evolution rules."""
        rule_pattern = r'r\d+:'
        return any(re.search(rule_pattern, line.strip()) for line in lines)
    
    def _validate_syntax(self, lines: List[str], filename: str):
        """Validate P-Lingua syntax."""
        for i, line in enumerate(lines, 1):
            line = line.strip()
            if not line or line.startswith('#'):
                continue
            
            # Check balanced brackets
            if '[' in line or ']' in line:
                if line.count('[') != line.count(']'):
                    self.errors.append(f"{filename}:{i}: Unbalanced brackets")
            
            # Check balanced parentheses
            if '(' in line or ')' in line:
                if line.count('(') != line.count(')'):
                    self.errors.append(f"{filename}:{i}: Unbalanced parentheses")
            
            # Check rule syntax
            if re.match(r'r\d+:', line):
                if '->' not in line:
                    self.errors.append(f"{filename}:{i}: Rule missing '->' operator")
    
    def print_results(self):
        """Print validation results."""
        if self.errors:
            print("ERRORS:")
            for error in self.errors:
                print(f"  {error}")
        
        if self.warnings:
            print("WARNINGS:")
            for warning in self.warnings:
                print(f"  {warning}")
        
        if not self.errors and not self.warnings:
            print("✓ Model validation passed")
        
        return len(self.errors) == 0

def main():
    if len(sys.argv) < 2:
        print("Usage: python model_validator.py <model_file.pli>")
        sys.exit(1)
    
    validator = ModelValidator()
    model_file = sys.argv[1]
    
    if validator.validate_file(model_file):
        print(f"✓ {model_file} is valid")
    else:
        print(f"✗ {model_file} has validation errors")
        validator.print_results()
        sys.exit(1)

if __name__ == "__main__":
    main()

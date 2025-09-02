
"""
P-Lingua Model Explorer

Explores and analyzes P-Lingua models, showing structure and statistics.
"""

import re
import sys
from typing import Dict, List, Set
from pathlib import Path

class ModelExplorer:
    def __init__(self):
        self.model_name = ""
        self.membranes = {}
        self.rules = {}
        self.objects = set()
        
    def explore_file(self, file_path: str):
        """Explore a P-Lingua model file."""
        try:
            with open(file_path, 'r') as f:
                content = f.read()
            
            self.parse_model(content)
            self.print_analysis()
            
        except FileNotFoundError:
            print(f"Error: File not found: {file_path}")
            sys.exit(1)
        except Exception as e:
            print(f"Error reading file: {e}")
            sys.exit(1)
    
    def parse_model(self, content: str):
        """Parse P-Lingua model content."""
        lines = content.split('\n')
        
        for line in lines:
            line = line.strip()
            if not line or line.startswith('#'):
                continue
                
            # Parse model name
            model_match = re.search(r'@model<(\w+)>', line)
            if model_match:
                self.model_name = model_match.group(1)
            
            # Parse rules
            rule_match = re.match(r'(r\d+):\s*(.+)', line)
            if rule_match:
                rule_id = rule_match.group(1)
                rule_def = rule_match.group(2)
                self.rules[rule_id] = rule_def
                
                # Extract objects from rules
                objects = re.findall(r'\b[a-z]\w*\b', rule_def)
                self.objects.update(objects)
            
            # Parse membrane structure (simplified)
            if '[' in line and ']' in line:
                membrane_objects = re.findall(r"'([^']+)", line)
                for obj_list in membrane_objects:
                    if ',' in obj_list:
                        self.objects.update(obj_list.split(','))
                    elif obj_list:
                        self.objects.add(obj_list)
    
    def print_analysis(self):
        """Print model analysis."""
        print(f"=== P-Lingua Model Analysis ===")
        print(f"Model Name: {self.model_name or 'Unnamed'}")
        print(f"Number of Rules: {len(self.rules)}")
        print(f"Number of Objects: {len(self.objects)}")
        
        print(f"\n--- Objects ---")
        for obj in sorted(self.objects):
            if obj and not obj.isdigit():
                print(f"  {obj}")
        
        print(f"\n--- Rules ---")
        for rule_id, rule_def in self.rules.items():
            print(f"  {rule_id}: {rule_def}")
        
        # Basic complexity analysis
        print(f"\n--- Complexity Analysis ---")
        print(f"  Rule complexity: {self._calculate_rule_complexity()}")
        print(f"  Object diversity: {len([o for o in self.objects if o and not o.isdigit()])}")
        print(f"  Communication patterns: {self._count_communication_patterns()}")
    
    def _calculate_rule_complexity(self) -> str:
        """Calculate rule complexity level."""
        total_rules = len(self.rules)
        if total_rules <= 3:
            return "Simple"
        elif total_rules <= 8:
            return "Moderate"
        else:
            return "Complex"
    
    def _count_communication_patterns(self) -> int:
        """Count communication patterns in rules."""
        comm_count = 0
        for rule_def in self.rules.values():
            if '[]' in rule_def and "'" in rule_def:
                comm_count += 1
        return comm_count

def main():
    if len(sys.argv) < 2:
        print("Usage: python model_explorer.py <model_file.pli>")
        print("\nAvailable models:")
        
        # List available models
        plingua_dir = Path(__file__).parent.parent
        examples_dir = plingua_dir / "examples"
        
        if examples_dir.exists():
            for pli_file in examples_dir.rglob("*.pli"):
                print(f"  {pli_file.relative_to(plingua_dir)}")
        
        sys.exit(1)
    
    explorer = ModelExplorer()
    explorer.explore_file(sys.argv[1])

if __name__ == "__main__":
    main()

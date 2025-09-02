
from typing import Dict, List, Optional, Set, Tuple
from .psystem import PSystem
from .atom_membrane import AtomMembrane, LinkAtomMembrane, NodeAtomMembrane
from .configuration import Configuration
from .rule import EvolutionRule, CommunicationRule
from .multiset import Multiset

class AtomSpacePSystem(PSystem):
    """
    A P-System where the AtomSpace is represented as a hierarchy of membranes.
    
    - Each Atom becomes an AtomMembrane
    - Truth values become objects in multisets
    - Attention values affect membrane charges
    - Inference becomes membrane communication and evolution
    """
    
    def __init__(self):
        super().__init__("atomspace_psystem")
        self.atom_membranes: Dict[int, AtomMembrane] = {}
        self.type_hierarchies: Dict[str, List[int]] = {}
        self.attention_focus: Set[int] = set()
        self.inference_trails: List[Tuple[int, int, str]] = []
        self.step_count = 0
        
    def create_node_atom(self, atom_type: str, atom_name: str, 
                        truth_strength: float = 1.0, truth_confidence: float = 1.0) -> int:
        """Create a new Node atom as a membrane."""
        atom_id = len(self.atom_membranes) + 1
        
        membrane = NodeAtomMembrane(atom_type, atom_name, atom_id)
        membrane.set_truth_value(truth_strength, truth_confidence)
        
        self.atom_membranes[atom_id] = membrane
        
        # Add to type hierarchy
        if atom_type not in self.type_hierarchies:
            self.type_hierarchies[atom_type] = []
        self.type_hierarchies[atom_type].append(atom_id)
        
        return atom_id
    
    def create_link_atom(self, atom_type: str, outgoing_atoms: List[int],
                        truth_strength: float = 1.0, truth_confidence: float = 1.0) -> int:
        """Create a new Link atom as a membrane containing other atoms."""
        atom_id = len(self.atom_membranes) + 1
        
        membrane = LinkAtomMembrane(atom_type, outgoing_atoms, atom_id)
        membrane.set_truth_value(truth_strength, truth_confidence)
        
        # Establish parent-child relationships
        for out_atom_id in outgoing_atoms:
            if out_atom_id in self.atom_membranes:
                child_membrane = self.atom_membranes[out_atom_id]
                membrane.add_child(child_membrane)
                child_membrane.add_incoming_atom(atom_id)
        
        self.atom_membranes[atom_id] = membrane
        
        # Add to type hierarchy
        if atom_type not in self.type_hierarchies:
            self.type_hierarchies[atom_type] = []
        self.type_hierarchies[atom_type].append(atom_id)
        
        return atom_id
    
    def set_attention_focus(self, atom_ids: List[int], focus_strength: int = 100):
        """Set attention focus on specific atoms."""
        self.attention_focus.clear()
        
        for atom_id in atom_ids:
            if atom_id in self.atom_membranes:
                membrane = self.atom_membranes[atom_id]
                membrane.set_attention_value(focus_strength, 
                                           membrane.attention_value["lti"],
                                           membrane.attention_value["vlti"])
                self.attention_focus.add(atom_id)
    
    def spread_activation(self, source_atom_id: int, activation_amount: int = 50, max_hops: int = 3):
        """Spread activation through the atom network."""
        visited = set()
        queue = [(source_atom_id, activation_amount, 0)]
        
        while queue:
            current_id, current_activation, hops = queue.pop(0)
            
            if current_id in visited or hops >= max_hops or current_activation <= 0:
                continue
                
            visited.add(current_id)
            
            if current_id in self.atom_membranes:
                membrane = self.atom_membranes[current_id]
                membrane.spread_activation(current_activation)
                
                # Spread to connected atoms with decay
                decay_factor = 0.7
                next_activation = int(current_activation * decay_factor)
                
                # Spread to outgoing atoms
                for out_id in membrane.outgoing_atoms:
                    if out_id not in visited:
                        queue.append((out_id, next_activation, hops + 1))
                
                # Spread to incoming atoms
                for in_id in membrane.incoming_atoms:
                    if in_id not in visited:
                        queue.append((in_id, next_activation, hops + 1))
    
    def create_inference_rules(self):
        """Generate inference rules based on atom relationships."""
        rules = []
        
        # Create deduction rules for ImplicationLinks
        implication_atoms = self.type_hierarchies.get("ImplicationLink", [])
        
        for impl_id in implication_atoms:
            impl_membrane = self.atom_membranes[impl_id]
            if len(impl_membrane.outgoing_atoms) >= 2:
                antecedent_id = impl_membrane.outgoing_atoms[0]
                consequent_id = impl_membrane.outgoing_atoms[1]
                
                # Deduction rule: P->Q, P ⊢ Q
                lhs = Multiset()
                lhs.add("implication_active", 1)
                lhs.add("antecedent_active", 1)
                lhs.add("truth_strength", 30)
                
                rhs = Multiset()
                rhs.add("consequent_derived", 1)
                rhs.add("truth_strength", 25)
                rhs.add("inference_trail", 1)
                
                rule = EvolutionRule(
                    rule_id=f"deduction_{impl_id}",
                    lhs=lhs,
                    rhs=rhs,
                    membrane_label=impl_id,
                    priority=impl_membrane.attention_value["sti"]
                )
                rules.append(rule)
        
        # Create similarity propagation rules
        similarity_atoms = self.type_hierarchies.get("SimilarityLink", [])
        
        for sim_id in similarity_atoms:
            sim_membrane = self.atom_membranes[sim_id]
            if len(sim_membrane.outgoing_atoms) >= 2:
                lhs = Multiset()
                lhs.add("similarity_active", 1)
                lhs.add("activation_spread", 10)
                
                rhs = Multiset()
                rhs.add("similarity_boost", 1)
                rhs.add("activation_spread", 15)
                
                rule = EvolutionRule(
                    rule_id=f"similarity_prop_{sim_id}",
                    lhs=lhs,
                    rhs=rhs,
                    membrane_label=sim_id,
                    priority=50
                )
                rules.append(rule)
        
        self.rules.extend(rules)
    
    def apply_forgetting(self, decay_rate: float = 0.05):
        """Apply forgetting to all atoms."""
        atoms_to_remove = []
        
        for atom_id, membrane in self.atom_membranes.items():
            membrane.apply_forgetting_rule(decay_rate)
            
            if membrane.dissolved:
                atoms_to_remove.append(atom_id)
        
        # Remove dissolved atoms
        for atom_id in atoms_to_remove:
            self.remove_atom(atom_id)
    
    def remove_atom(self, atom_id: int):
        """Remove an atom and update connections."""
        if atom_id not in self.atom_membranes:
            return
            
        membrane = self.atom_membranes[atom_id]
        
        # Update incoming atoms
        for in_id in membrane.incoming_atoms:
            if in_id in self.atom_membranes:
                in_membrane = self.atom_membranes[in_id]
                if atom_id in in_membrane.outgoing_atoms:
                    in_membrane.outgoing_atoms.remove(atom_id)
        
        # Update outgoing atoms
        for out_id in membrane.outgoing_atoms:
            if out_id in self.atom_membranes:
                out_membrane = self.atom_membranes[out_id]
                out_membrane.incoming_atoms.discard(atom_id)
        
        # Remove from type hierarchy
        atom_type = membrane.atom_type
        if atom_type in self.type_hierarchies:
            if atom_id in self.type_hierarchies[atom_type]:
                self.type_hierarchies[atom_type].remove(atom_id)
        
        # Remove from focus if present
        self.attention_focus.discard(atom_id)
        
        del self.atom_membranes[atom_id]
    
    def step(self) -> bool:
        """Execute one computation step of the P-System."""
        self.step_count += 1
        
        # Apply rules to focused atoms first
        rules_applied = 0
        
        for atom_id in list(self.attention_focus):
            if atom_id in self.atom_membranes:
                membrane = self.atom_membranes[atom_id]
                
                # Apply evolution rules
                for rule in self.rules:
                    if hasattr(rule, 'membrane_label') and rule.membrane_label == atom_id:
                        if rule.can_apply(membrane.multiset):
                            rule.apply(membrane.multiset)
                            rules_applied += 1
                            
                            # Record inference trail
                            self.inference_trails.append((atom_id, self.step_count, rule.rule_id))
        
        # Spread activation from highly active atoms
        high_sti_atoms = [
            atom_id for atom_id, membrane in self.atom_membranes.items()
            if membrane.attention_value["sti"] > 200
        ]
        
        for atom_id in high_sti_atoms[:5]:  # Limit to top 5
            self.spread_activation(atom_id, 30, 2)
        
        # Apply forgetting every 10 steps
        if self.step_count % 10 == 0:
            self.apply_forgetting()
        
        # Regenerate rules every 20 steps
        if self.step_count % 20 == 0:
            self.rules.clear()
            self.create_inference_rules()
        
        return rules_applied > 0 or len(self.attention_focus) > 0
    
    def is_halting(self) -> bool:
        """Check if the system has reached a halting configuration."""
        # Halt if no atoms have significant attention
        max_sti = max((m.attention_value["sti"] for m in self.atom_membranes.values()), default=0)
        return max_sti < 10
    
    def get_atomspace_state(self) -> Dict:
        """Get current state of the AtomSpace P-System."""
        return {
            "total_atoms": len(self.atom_membranes),
            "type_counts": {t: len(atoms) for t, atoms in self.type_hierarchies.items()},
            "attention_focus": list(self.attention_focus),
            "average_sti": sum(m.attention_value["sti"] for m in self.atom_membranes.values()) / max(len(self.atom_membranes), 1),
            "inference_trails": len(self.inference_trails),
            "step_count": self.step_count
        }
    
    def query_atoms_by_pattern(self, pattern_type: str, min_sti: int = 0) -> List[int]:
        """Query atoms matching a pattern."""
        results = []
        
        for atom_id, membrane in self.atom_membranes.items():
            if (membrane.atom_type == pattern_type and 
                membrane.attention_value["sti"] >= min_sti):
                results.append(atom_id)
        
        return sorted(results, key=lambda x: self.atom_membranes[x].attention_value["sti"], reverse=True)
    
    def to_atomese(self) -> str:
        """Convert the entire P-System back to Atomese format."""
        atomese_lines = []
        
        for atom_id in sorted(self.atom_membranes.keys()):
            membrane = self.atom_membranes[atom_id]
            atomese_str = membrane.to_atomese_string()
            tv_str = f" (stv {membrane.truth_value['strength']:.3f} {membrane.truth_value['confidence']:.3f})"
            atomese_lines.append(f"{atomese_str}{tv_str}")
        
        return "\n".join(atomese_lines)

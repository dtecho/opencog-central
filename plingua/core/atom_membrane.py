
from typing import Dict, List, Optional, Any, Set
from .membrane import Membrane
from .multiset import Multiset
from .rule import Rule

class AtomMembrane(Membrane):
    """
    A membrane that represents an OpenCog Atom as a P-System membrane.
    
    Each AtomMembrane encapsulates:
    - Atom type and name as membrane properties
    - Truth values as objects in the multiset
    - Incoming/outgoing connections as child/parent relationships
    - Attention values as membrane charge
    """
    
    def __init__(self, atom_type: str, atom_name: str = "", atom_id: Optional[int] = None):
        super().__init__(label=atom_id or hash(f"{atom_type}:{atom_name}"))
        self.atom_type = atom_type
        self.atom_name = atom_name
        self.atom_id = atom_id
        self.truth_value = {"strength": 1.0, "confidence": 1.0}
        self.attention_value = {"sti": 0, "lti": 0, "vlti": 0}
        self.incoming_atoms: Set[int] = set()
        self.outgoing_atoms: List[int] = []
        
        # Initialize multiset with truth value objects
        self.multiset.add("truth_strength", int(self.truth_value["strength"] * 100))
        self.multiset.add("truth_confidence", int(self.truth_value["confidence"] * 100))
        
        # Set charge based on STI (Short Term Importance)
        self.charge = 1 if self.attention_value["sti"] > 0 else 0
    
    def set_truth_value(self, strength: float, confidence: float):
        """Update truth value and corresponding multiset objects."""
        self.truth_value = {"strength": strength, "confidence": confidence}
        
        # Clear old truth values and add new ones
        self.multiset.objects.pop("truth_strength", None)
        self.multiset.objects.pop("truth_confidence", None)
        
        self.multiset.add("truth_strength", int(strength * 100))
        self.multiset.add("truth_confidence", int(confidence * 100))
    
    def set_attention_value(self, sti: int, lti: int, vlti: int = 0):
        """Update attention value and membrane charge."""
        self.attention_value = {"sti": sti, "lti": lti, "vlti": vlti}
        
        # Update charge based on STI
        if sti > 100:
            self.charge = 1  # Positive charge for high importance
        elif sti < -100:
            self.charge = -1  # Negative charge for low importance
        else:
            self.charge = 0  # Neutral charge
        
        # Add attention objects to multiset
        self.multiset.add("sti_units", max(0, sti))
        self.multiset.add("lti_units", max(0, lti))
    
    def add_incoming_atom(self, atom_id: int):
        """Add an incoming atom connection."""
        self.incoming_atoms.add(atom_id)
        self.multiset.add("incoming_connection", 1)
    
    def add_outgoing_atom(self, atom_id: int):
        """Add an outgoing atom connection."""
        self.outgoing_atoms.append(atom_id)
        self.multiset.add("outgoing_connection", 1)
    
    def get_connectivity_degree(self) -> int:
        """Calculate the connectivity degree of this atom."""
        return len(self.incoming_atoms) + len(self.outgoing_atoms)
    
    def create_inference_rule(self, other_membrane: 'AtomMembrane') -> Optional[Rule]:
        """Create a P-System rule for inference between two atoms."""
        from .rule import EvolutionRule
        
        # Example: Deduction rule between two atoms
        if (self.atom_type == "ImplicationLink" and 
            other_membrane.atom_type in ["ConceptNode", "PredicateNode"]):
            
            lhs = Multiset()
            lhs.add("implication_premise", 1)
            lhs.add("truth_strength", 50)
            
            rhs = Multiset()
            rhs.add("deduction_result", 1)
            rhs.add("truth_strength", 40)
            
            return EvolutionRule(
                rule_id=f"deduction_{self.label}_{other_membrane.label}",
                lhs=lhs,
                rhs=rhs,
                membrane_label=self.label,
                priority=self.attention_value["sti"]
            )
        
        return None
    
    def apply_forgetting_rule(self, decay_rate: float = 0.1):
        """Apply forgetting by reducing attention and truth values."""
        # Decay STI
        new_sti = int(self.attention_value["sti"] * (1 - decay_rate))
        
        # Decay truth confidence
        new_confidence = self.truth_value["confidence"] * (1 - decay_rate)
        
        self.set_attention_value(new_sti, self.attention_value["lti"], self.attention_value["vlti"])
        self.set_truth_value(self.truth_value["strength"], new_confidence)
        
        # If attention drops too low, mark for dissolution
        if new_sti < -1000:
            self.dissolved = True
    
    def spread_activation(self, activation_amount: int):
        """Spread activation to connected atoms via multiset objects."""
        if activation_amount <= 0:
            return
        
        # Add activation objects to spread
        self.multiset.add("activation_spread", activation_amount)
        
        # Increase STI based on received activation
        current_sti = self.attention_value["sti"]
        boost = min(activation_amount, 100)  # Cap the boost
        self.set_attention_value(
            current_sti + boost,
            self.attention_value["lti"],
            self.attention_value["vlti"]
        )
    
    def to_atomese_string(self) -> str:
        """Convert membrane back to Atomese representation."""
        if self.outgoing_atoms:
            outgoing_str = " ".join(f"(Atom {atom_id})" for atom_id in self.outgoing_atoms)
            return f"({self.atom_type} {outgoing_str})"
        else:
            return f"({self.atom_type} \"{self.atom_name}\")"
    
    def __str__(self) -> str:
        """Enhanced string representation showing atom properties."""
        base_str = super().__str__()
        return (f"AtomMembrane[{self.atom_type}:{self.atom_name}] "
                f"TV({self.truth_value['strength']:.2f},{self.truth_value['confidence']:.2f}) "
                f"AV({self.attention_value['sti']}) {base_str}")

class LinkAtomMembrane(AtomMembrane):
    """Specialized membrane for Link atoms that can contain other atoms."""
    
    def __init__(self, atom_type: str, outgoing_atoms: List[int], atom_id: Optional[int] = None):
        super().__init__(atom_type, "", atom_id)
        self.outgoing_atoms = outgoing_atoms
        
        # Add objects representing the link structure
        self.multiset.add("link_arity", len(outgoing_atoms))
        for i, out_atom in enumerate(outgoing_atoms):
            self.multiset.add(f"outgoing_{i}", 1)
    
    def add_outgoing_atom(self, atom_id: int):
        """Override to maintain link structure."""
        super().add_outgoing_atom(atom_id)
        self.multiset.add("link_arity", 1)

class NodeAtomMembrane(AtomMembrane):
    """Specialized membrane for Node atoms with names."""
    
    def __init__(self, atom_type: str, atom_name: str, atom_id: Optional[int] = None):
        super().__init__(atom_type, atom_name, atom_id)
        
        # Add objects representing node properties
        name_hash = hash(atom_name) % 1000
        self.multiset.add("name_hash", name_hash)
        self.multiset.add("node_type", 1)

import constants
from membrane import Membrane

class Rule:
    def __init__(self, ruletype, label, lhs, rhs):
        self.ident = next(constants.next_rule_ident)
        self.ruletype = ruletype
        self.label = label
        self.lhs = lhs
        self.rhs = rhs

    def is_applicable(self, membrane):
        pass

    def apply_lhs(self, membrane):
        pass

    def apply_rhs(self, membrane):
        pass

class SymportRule(Rule):
    def __init__(self, label, lhs, obj):
        Rule.__init__(self, constants.SYM, label, lhs, lhs)
        self.obj = obj

    def is_applicable(self, membrane):
        if (membrane.label == self.label) and (not (membrane.blocked == constants.CRE)):
            applicable = True
            if self.obj == constants.OUT:
                if not (self.lhs in membrane.objects):
                    applicable = False
            else:
                if not (self.lhs in membrane.parent_membrane.objects):
                    applicable = False
        else:
             applicable = False
        return applicable

    def apply_lhs(self, membrane):
        membrane.blocked = constants.SYM
        if self.obj == constants.OUT:
            if membrane.objects[self.lhs] == 1:
                membrane.objects.pop(self.lhs, None)
            else:
                membrane.objects[self.lhs] -= 1
        else:
            if membrane.parent_membrane.objects[self.lhs] == 1:
                membrane.parent_membrane.objects.pop(self.lhs, None)
            else:
                membrane.parent_membrane.objects[self.lhs] -= 1

    def apply_rhs(self, membrane):
        if self.obj == constants.IN:
            if self.rhs in membrane.objects:
                membrane.objects[self.rhs] += 1
            else:
                membrane.objects[self.rhs] = 1
        else:
            if self.rhs in membrane.parent_membrane.objects:
                membrane.parent_membrane.objects[self.rhs] += 1
            else:
                membrane.parent_membrane.objects[self.rhs] = 1

    def __str__(self):
        return '({}, {})'.format(self.lhs, 'out' if self.obj == constants.OUT else 'in')

class OutRule(SymportRule):
    def __init__(self, label, lhs):
        SymportRule.__init__(self, label, lhs, constants.OUT)

class InRule(SymportRule):
    def __init__(self, label, lhs):
        SymportRule.__init__(self, label, lhs, constants.IN)

class CreationRule(Rule):
    def __init__(self, label, lhs, rhs, newlabel):
        Rule.__init__(self, constants.CRE, label, lhs, rhs)
        self.newlabel = newlabel

    def is_applicable(self, membrane):
        if (membrane.label == self.label) and (not membrane.blocked) and (self.lhs in membrane.objects):
            applicable = True
        else:
            applicable = False       
        return applicable

    def apply_lhs(self, membrane):
        membrane.blocked = constants.CRE
        if membrane.objects[self.lhs] == 1:
            membrane.objects.pop(self.lhs, None)
        else:
            membrane.objects[self.lhs] -= 1

    def apply_rhs(self, membrane):
        new_membrane = Membrane(membrane, self.newlabel)
        for obj in self.rhs:
            if not (obj == '#'):
                new_membrane.objects[obj] = 1
        membrane.inner_membranes.add(new_membrane)

    def __str__(self):
        return '[{} --> [ {} ]_{}]_{}'.format(self.lhs, ', '.join(self.rhs), self.newlabel, self.label)

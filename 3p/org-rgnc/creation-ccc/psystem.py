import re
import constants
from membrane import Membrane
from rule import SymportRule, CreationRule

class Psystem:

    def __init__(self):
        self.environment = Membrane(None, 'env')
        self.config = 0
        self.rules = dict()

    def add_rule(self, rule):
        if not (rule.label in self.rules):
            self.rules[rule.label] = set()
        self.rules[rule.label].add(rule)

    def add_rules(self, rule_template, dict_variables):
        templates = set()
        templates.add(rule_template)
        rules = set()
        for key in dict_variables:
            for template in templates:
                for val in dict_variables[key]:
                    rules.add(map(lambda x : x.format(**{ key : val }), template))
                    # rules.add(template.format({ key : val }))
            templates = rules
            rules = set()
        for rule in templates:
            if len(rule_template) == 3:
                self.add_rule(SymportRule(rule[0], rule[1], rule[2]))
            elif len(rule_template) == 4:
                self.add_rule(CreationRule(rule[0], rule[1], rule[2], rule[3]))

    def step(self):
        selected_rules = self.select_rules()
        step_exec = False
        if selected_rules:
            self.config += 1
            step_exec = True
        self.apply_rules(selected_rules)
        self.clean_membranes()
        return step_exec

    def compute(self, verbose=0, steps=constants.MAX_INT):
        step_exec = True
        init_config = self.config
        if verbose:
            print(self)
        while step_exec and ((self.config - init_config) < steps):
            # if not (self.config % 100):
            #     print('Step', self.config)
            #     print(self.environment.__str__(0, 2))
            step_exec = self.step()
            if verbose > 1:
                print(self)
        if verbose:
            print("Computation finished")
            print(self)
        else:
            print(self.environment.__str__(0,0))

    def select_rules(self):
        return self.select_rules_aux(self.environment)

    def select_rules_aux(self, region):
        region.blocked = False
        selected_rules = dict()
        if region.label in self.rules:
            rules_for_region = self.rules[region.label]
            selected_rules_region = self.select_region_rules(region, rules_for_region)
            self.add_selected_rules(selected_rules, selected_rules_region)
        for i_membrane in region.inner_membranes:
            i_rules = self.select_rules_aux(i_membrane)
            selected_rules = self.add_selected_rules(selected_rules, i_rules)
        return selected_rules

    def select_region_rules(self, region, rules):
        region_rules = dict()
        for rule in rules:
            while rule.is_applicable(region):
                if (region, rule) in region_rules:
                    region_rules[(region, rule)] += 1
                else:
                    region_rules[(region, rule)] = 1
                rule.apply_lhs(region)
        return region_rules

    def add_selected_rules(self, selected_rules, rules_region):
        for key in rules_region:
            if key in selected_rules:
                selected_rules[key] += rules_region[key]
            else:
                selected_rules[key] = rules_region[key]
        return selected_rules
            
    def apply_rules(self, selected_rules):
        for key in selected_rules:
            for i in range(selected_rules[key]):
                key[1].apply_rhs(key[0])

    def clean_membranes(self):
        to_clean = self.clean_membranes_aux(self.environment)
        for membrane in to_clean:
            membrane.parent_membrane.inner_membranes.remove(membrane)

    def clean_membranes_aux(self, region):
        to_clean = set()
        if region.label == '#' and len(region.objects) == 0:
            to_clean.add(region)
        else:
            for i_membrane in region.inner_membranes:
                for membrane in self.clean_membranes_aux(i_membrane):
                    to_clean.add(membrane)
        return to_clean

    def __str__(self):
        return self.environment.__str__(0)

    def parse_rule(self, rule):
        crm = re.match("\[ *(.*?) *--> *\[ *(.*?) *\]'(.*?) *\]'(.*) *", rule)
        srm = re.match("\( *(.*?) *; *(.*?) *\)'(.*)", rule)
        # Creation rule
        if crm:
            label = crm[4]
            lhs = crm[1]
            rhs = crm[2].split(';')
            newlabel = crm[3]
            self.add_rule(CreationRule(label, lhs, rhs, newlabel))
        # Symport rule
        elif srm:
            label = srm[3]
            lhs = srm[1]
            obj = constants.objs[srm[2]]
            self.add_rule(SymportRule(label, lhs, obj))

    def print_rules(self, membrane='skin', membrane_type=CreationRule):
        for rule in self.rules[membrane]:
            if type(rule) == membrane_type:
                print(rule)

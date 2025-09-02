import math
from qsat import QSATPsystem
import examples
from rule import CreationRule, SymportRule, InRule, OutRule

n = 10
p = 5
formula = examples.generate_random_formula(n, p)
n, p, init_multiset = examples.get_init_multiset(formula)

# print(n, p, math.floor((((n**2)*p) + 12*n + 5*p + 2) / 2))
print(examples.formula_str(n, p, formula))

# n, p, init_multiset = examples.example4()

psystem = QSATPsystem(n, p, init_multiset)

# for key in p.rules:
#     print(key, ':')
#     for rule in p.rules[key]:
#         print(' ', rule)

psystem.compute()

# psystem.print_rules()


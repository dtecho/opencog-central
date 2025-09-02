import re, random

def formula_str(n, p, formula):
    output = ''
    for i in range(n):
        if i % 2:
            output += 'Ex{}'.format(i+1)
        else:
            output += 'Ax{}'.format(i+1)
    output += ' '
    formulas = []
    for j in range(p):
        formulas.append('(' + ' + '.join(formula[j]) + ')')
    output += ' · '.join(formulas)
    return output

def get_init_multiset(formula):
    multiset = set()
    n = 0
    p = len(formula)
    j = 1
    for clause in formula:
        for literal in clause:
            regex = re.match('(.*)\[(.*)\]', literal)
            lit = regex[1]
            var = int(regex[2])
            if var > n:
                n = var
            multiset.add('{}<{},{}>'.format(lit, str(var), str(j)))
        j += 1
    return [n, p, multiset]

def generate_random_formula():
    n = random.randint(1, 30)
    p = random.randint(1, 30)
    formula = generate_random_formula(n, p)
    return formula

def generate_random_formula(n, p):
    formula = []
    for j in range(p):
        clause = []
        for i in range(n):
            if random.random() < 0.5:
                if random.random() < 0.5:
                    clause.append('x[{}]'.format(i+1))
                else:
                    clause.append('xb[{}]'.format(i+1))
        clause = tuple(clause)
        formula.append(clause)
    formula = tuple(formula)
    return formula

# True
def example1():
    formula = (('x[1]', 'x[2]'), ('x[1]', 'x[2]'))
    return formula

# True
def example2():
    formula = (('x[1]', 'x[2]', 'x[3]'),)
    return formula

# False
def example3():
    formula = (('x[1]',), ('xb[1]', 'xb[2]'), ('x[2]',))
    return formula

# True
def example4():
    formula = (('x[1]', 'x[2]'), ('x[3]', 'x[4]'), ('x[5]', 'x[6]'), ('x[7]', 'x[8]'), ('x[9]', 'x[10]'))
    return formula


def random_formula():
    formula = generate_random_formula()
    return get_init_multiset(formula)

def random_formula(n, p):
    formula = generate_random_formula(n, p)
    return get_init_multiset(formula)

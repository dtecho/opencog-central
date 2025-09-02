import math
from psystem import Psystem
from membrane import Membrane
from rule import OutRule, InRule, CreationRule

class QSATPsystem(Psystem):
    def __init__(self, n, p, init_multiset):
        Psystem.__init__(self)
        self.init_multiset = init_multiset
        self.initialize_structure()
        self.initialize_initial_multisets()
        self.initialize_rules(n, p)
        self.insert_init_multiset(init_multiset)

    def initialize_structure(self):
        self.mskin = Membrane(self.environment, 'skin')
        self.malpha = Membrane(self.mskin, 'alpha')

    def initialize_initial_multisets(self):
        self.mskin.objects = { 'z<1,t>' : 1, 'z<1,f>' : 1 }
        self.malpha.objects = { 'alpha<0>' : 1, 'alphap' : 1 }

    def insert_init_multiset(self, init_multiset):
        for key in init_multiset:
            self.mskin.objects[key] = 1

    def initialize_rules(self, n, p):
        self.counter_rules(n, p)
        self.positive_rules(n, p)
        self.negative_rules(n, p)
        self.structure_rules(n)
        self.clauses_rules(n, p)
        self.all_rules(n, p)
        self.quantifiers_rules(n)

    def counter_rules(self, n, p):
        # k1 = n * (n * p)
        # k2 = 5 * p + 2
        # k3 = 10 * n
        k = (n**2)*p + 13*n + 5 * p + 2
        #
        for i in range(math.floor(k / 2)):
            self.parse_rule("[alpha<{}> --> [alpha<{}>]'#]'alpha".format(i, i+1))
        #
        for i in range(1, math.floor((k / 2) + 1)):
            self.parse_rule("(alpha<{}>; out)'#".format(i))
        #
        self.parse_rule("[alpha<{}> --> [alpha]'alphap]'alpha".format(math.floor(k / 2)))
        self.parse_rule("(alpha; out)'alphap")
        self.parse_rule("(alpha; out)'alpha")
        self.parse_rule("(alphap; in)'alphap")
        self.parse_rule("[ alphap --> [alphapp]'#]'alphap")
        self.parse_rule("(alphapp; out)'#")
        self.parse_rule("(alphapp; out)'alphap")
        self.parse_rule("(alphapp; out)'alpha")

    def positive_rules(self, n, p):
        #
        for r in ['t', 'f']:
            self.parse_rule("[ D<1,{}> --> [#]'yes]'skin".format(r))
        self.parse_rule("(alpha; in)'yes")
        self.parse_rule("[ alpha --> [yes]'#]'yes")
        self.parse_rule("(yes; out)'#")
        self.parse_rule("(yes; out)'yes")
        self.parse_rule("(yes; out)'skin")

    def negative_rules(self, n, p):
        #
        self.parse_rule("[ alphapp --> [#]'no]'skin")
        self.parse_rule("(alpha; in)'no")
        self.parse_rule("[ alpha --> [no]'#]'no")
        self.parse_rule("(no; out)'#")
        self.parse_rule("(no; out)'no")
        self.parse_rule("(no; out)'skin")

    def structure_rules(self, n):
        #
        for r in ['t', 'f']:
            self.parse_rule("[z<1,{}> --> [z<1>;dA]'<1,{}> ]'skin".format(r, r))
        #
        for i in range(2, n, 2):
            for r in ['t', 'f']:
                for rp in ['t', 'f']:
                    self.parse_rule("[ z<{},{}> --> [z<{}>;dE]'<{},{}>]'<{},{}>".format(i, r, i, i, r, i-1, rp))
        #
        for i in range(3, n, 2):
            for r in ['t', 'f']:
                for rp in ['t', 'f']:
                    self.parse_rule("[ z<{},{}> --> [z<{}>;dA]'<{},{}>]'<{},{}>".format(i, r, i, i, r, i-1, rp))
        #
        for r in ['t', 'f']:
            for rp in ['t', 'f']:
                self.parse_rule("[ z<{},{}> --> [z<{}>]'<{},{}>]'<{},{}>".format(n, r, n, n, r, n-1, rp))
        
        for i in range(1, n):
            for r in ['t', 'f']:
                self.parse_rule("[ z<{}> --> [z<{},t>;z<{},f>]'#]'<{},{}>".format(i, i+1, i+1, i, r))
    #     #
        for i in range(1, n+1):
            for r in ['t', 'f']:
                self.parse_rule("(z<{},{}>; out)'#".format(i, r))

    def clauses_rules(self, n, p):
        #
        for i in range(1, n+1):
            for j in range(1, p+1):
                self.parse_rule("[ x<{},{}> --> [x<1,{},{},t>;x<1,{},{},f>]'#]'skin".format(i, j, i, j, i, j))
        #
        for i in range(1, n+1):
            for j in range(1, p+1):
                self.parse_rule("[ xb<{},{}> --> [xb<1,{},{},t>;xb<1,{},{},f>]'#]'skin".format(i, j, i, j, i, j))
        #
        for i in range(1, n+1):
            for j in range(1, p+1):
                for ip in range(1, i):
                    for r in ['t', 'f']:
                        self.parse_rule("[ x<{},{},{},{}> --> [x<{},{},{},t>;x<{},{},{},f>]'#]'<{},{}>".format(ip, i, j, r, ip+1, i, j, ip+1, i, j, ip, r))
        #
        for i in range(1, n+1):
            for j in range(1, p+1):
                for ip in range(1, i+1):
                    for r in ['t', 'f']:
                        self.parse_rule("[ xb<{},{},{},{}> --> [xb<{},{},{},t>;x<{},{},{},f>]'#]'<{},{}>".format(ip, i, j, r, ip+1, i, j, ip+1, i, j, ip, r))
        #
        for i in range(1, n+1):
            for j in range(1, p+1):
                for ip in range(1, i+1):
                    for r in ['t', 'f']:
                        self.parse_rule("(x<{},{},{},{}>; out)'#".format(ip, i, j, r))
        #
        for i in range(1, n+1):
            for j in range(1, p+1):
                for ip in range(1, i+1):
                    for r in ['t', 'f']:
                        self.parse_rule("(xb<{},{},{},{}>; out)'#".format(ip, i, j, r))
        #
        for i in range(1, n+1):
            for j in range(1, p+1):
                for ip in range(1, i+1):
                    for r in ['t', 'f']:
                        self.parse_rule("(x<{},{},{},{}>; in)'<{},{}>".format(ip,i,j,r,ip,r))
        #
        for i in range(1, n+1):
            for j in range(1, p+1):
                for ip in range(1, i+1):
                    for r in ['t', 'f']:
                        self.parse_rule("(xb<{},{},{},{}>; in)'<{},{}>".format(ip,i,j,r,ip,r))
        #
        for i in range(1, n):
            for j in range(1, p+1):
                self.parse_rule("[ x<{},{},{},t> --> [c<{},{},t>;c<{},{},f>]'#]'<{},t>".format(i, i, j, i, j, i, j, i))
        #
        for i in range(1, n):
            for j in range(1, p+1):
                self.parse_rule("[ xb<{},{},{},f> --> [c<{},{},t>;c<{},{},f>]'#]'<{},f>".format(i, i, j, i, j, i, j, i))
        #
        for j in range(1, p+1):
            self.parse_rule("[ x<{},{},{},t> --> [c<{},{},t>]'#]'<{},t>".format(n, n, j, n, j, n))
        #
        for j in range(1, p+1):
            self.parse_rule("[ x<{},{},{},f> --> [c<{},{},t>]'#]'<{},f>".format(n, n, j, n, j, n))
        #
        for i in range(1, n+1):
            for j in range(1, p+1):
                for r in ['t', 'f']:
                    self.parse_rule("(c<{},{},{}>; out)'#".format(i, j, r))
        #
        for i in range(1, n):
            for j in range(1, p+1):
                for r in ['t', 'f']:
                    self.parse_rule("(c<{},{},{}>; in)'<{},{}>".format(i, j, r, i+1, r))
        #
        for i in range(1, n+1):
            for j in range(1, p+1):
                for r in ['t', 'f']:
                    for ip in range(i+1, n+1):
                        self.parse_rule("[ c<{},{},{}> --> [c<{},{},t>;c<{},{},f>]'#]'<{},{}>".format(i, j, r, i+1, j, i+1, j, ip, r))

    def all_rules(self, n, p):
        for r in ['t', 'f']:
            self.parse_rule("[ z<{}> --> [d<0>]'#]'<{},{}>".format(n, n, r))
        #
        for j in range(1, p+1):
            for r in ['t', 'f']:
                for rp in ['t', 'f']:
                    self.parse_rule("[ c<{},{},{}> --> [#]'{}]'<{},{}>".format(n, j, r, j, n, rp))
        #
        for j in range(p):
            self.parse_rule("(d<{}>; out)'#".format(j))
            self.parse_rule("(d<{}>; in)'{}".format(j,j+1))
            self.parse_rule("[ d<{}> --> [d<{}>]'#]'{}".format(j, j+1, j+1))
            self.parse_rule("(d<{}>; out)'{}".format(j+1, j+1))
        self.parse_rule("(d<{}>; out)'#".format(p))
        #
        for r in ['t', 'f']:
            self.parse_rule("[ d<{}> --> [D<{},{}>]'#]'<{},{}>".format(p, n, r, n, r))
            self.parse_rule("(D<{},{}>; out)'#".format(n, r))

    def quantifiers_rules(self, n):
        #
        for i in range(1, n+1):
            for r in ['t', 'f']:
                self.parse_rule("(D<{},{}>; out)'<{},{}>".format(i, r, i, r))
        #
        for i in range(1, n, 2):
            for r in ['t', 'f']:
                for rp in ['t', 'f']:
                    self.parse_rule("[D<{},{}> --> [#]'<{},A,{},{}>]'<{},{}>".format(i+1, r, i, r, rp, i, rp))
        #
        for i in range(2, n, 2):
            for r in ['t', 'f']:
                for rp in ['t', 'f']:
                    self.parse_rule("[D<{},{}> --> [#]'<{},E,{}>]'<{},{}>".format(i+1, r, i, rp, i, rp))
        #
        for i in range(1, n, 2):
            for r in ['t', 'f']:
                self.parse_rule("(dA; in)'<{},A,t,{}>".format(i, r))
                self.parse_rule("[ dA --> [dAp]'#]'<{},A,t,{}>".format(i, r))
                self.parse_rule("(dAp; out)'<{},A,t,{}>".format(i, r))
                self.parse_rule("(dAp; in)'<{},A,f,{}>".format(i, r))
                self.parse_rule("[ dAp --> [D<{},{}>]'#]'<{},A,f,{}>".format(i, r, i, r))
        #
        self.parse_rule("(dAp; out)'#")
        #
        for i in range(2, n, 2):
            for r in ['t', 'f']:
                self.parse_rule("(dE; in)'<{},E,{}>".format(i, r))
                self.parse_rule("[ dE --> [D<{},{}>]'#]'<{},E,{}>".format(i, r, i, r))
        
        for i in range(1, n):
            for r in ['t', 'f']:
                self.parse_rule("(D<{},{}>; out)'#".format(i, r))
        #
        for i in range(1, n, 2):
            for r in ['t', 'f']:
                self.parse_rule("(D<{},{}>; out)'<{},A,f,{}>".format(i, r, i, r))
        #
        for i in range(2, n, 2):
            for r in ['t', 'f']:
                self.parse_rule("(D<{},{}>; out)'<{},E,{}>".format(i, r, i, r))


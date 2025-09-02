import constants

class Membrane:

    def __init__(self, parent_membrane, label):
        self.ident = next(constants.next_membrane_ident)
        self.inner_membranes = set()
        self.parent_membrane = parent_membrane
        if parent_membrane:
            parent_membrane.inner_membranes.add(self)
        self.objects = dict()
        self.label = label
        self.blocked = False

    def __str__(self, level, deepness=constants.MAX_INT):
        if self.label == '#' and len(self.objects) == 0:
            return ''
        ret = level * ' '
        # ret += '{} ({}): {}\n'.format(self.label, self.ident, ', '.join(map(lambda x: '{}{}'.format(x, '^' + str(self.objects[x]) if self.objects[x] > 1 else ''), filter(lambda x: not (x == '#'), self.objects))) if self.objects else '{}')
        ret += '{}: {}\n'.format(self.label, ', '.join(map(lambda x: '{}{}'.format(x, '^' + str(self.objects[x]) if self.objects[x] > 1 else ''), filter(lambda x: not (x == '#'), self.objects))) if self.objects else '{}')
        if deepness:
            level += 1
            deepness -= 1
            for membrane in self.inner_membranes:
                ret += membrane.__str__(level, deepness)
        return ret

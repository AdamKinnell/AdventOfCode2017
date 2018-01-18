from math import sqrt
import numpy

# Functions #########################################################

class RuleBook(object):

    def __init__(self):
        self.rules = {}

    @staticmethod
    def parse_pattern(pattern):
        return tuple(map(tuple, pattern.split('/')))

    def _create_permutations(self, pattern):

        # Flipped
        ud = numpy.flipud(pattern)
        lr = numpy.fliplr(pattern)

        # Rotated
        rotated = [numpy.rot90(p, a) for p in [pattern, ud, lr]
                                     for a in [0,1,2,3]]

        return [tuple(map(tuple, p)) for p in rotated]

    def add_rule(self, rule):
        rule = rule.strip()
        _in, _out = map(RuleBook.parse_pattern, rule.split(' => '))
        _ins = self._create_permutations(_in)
        self.rules.update({ i:_out for i in _ins})

    def get_transform(self, pattern):
        return self.rules[pattern]

class Enhancer(object):

    def __init__(self, rulebook):
        self.rulebook = rulebook

    def _split(self, state):
        state = numpy.array(state)
        size = 2 if len(state) % 2 == 0 else 3
        height, _ = state.shape

        # https://stackoverflow.com/questions/16873441
        return (state.reshape(height // size, size, -1, size)
                     .swapaxes(1, 2)
                     .reshape(-1, size, size))

    def _join(self, tiles):
        tiles = numpy.array(tiles)
        _, rows, cols = tiles.shape
        pattern_size = round(sqrt(tiles.size))

        # https://stackoverflow.com/questions/16873441
        return (tiles.reshape(pattern_size // rows, -1, rows, cols)
                     .swapaxes(1, 2)
                     .reshape(pattern_size, pattern_size))

    def _transform(self, tiles):
        tiles = [tuple(map(tuple, t)) for t in tiles]
        return list(map(self.rulebook.get_transform, tiles))

    def enhance(self, state):
        tiles = self._split(state)
        tiles = self._transform(tiles)
        return self._join(tiles)

# Entry Point #######################################################

RULES_FILE = 'day21.txt'
#ITERATIONS = 5
ITERATIONS = 18

rb = RuleBook()
for r in open(RULES_FILE).readlines():
    rb.add_rule(r)

eh = Enhancer(rb)
state = RuleBook.parse_pattern(".#./..#/###")
for i in range(0, ITERATIONS):
    print("Starting Iteration:", i+1)
    state = eh.enhance(state)

final = numpy.array(state)
print('Pixels On:', numpy.count_nonzero(final == '#')) # = 3018423
print('Final state after', ITERATIONS, 'iterations:')
print(final)

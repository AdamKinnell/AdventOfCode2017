from functools import reduce
from operator import xor

# Knot Hash #########################################################

def reverse_elements(lst, start_i, count):
    to_end = min(len(lst) - start_i, count)
    from_start = count - to_end

    elements = lst[start_i:start_i+to_end]
    elements += lst[0:from_start]
    elements = list(reversed(elements))
    lst[start_i:start_i+to_end] = elements[:to_end]
    lst[0:from_start] = elements[to_end:]

    return lst

def hash_round(string, lengths, pos=0, skip=0):
    for length in lengths:
        string = reverse_elements(string, pos, length)
        pos = (pos + length + skip) % len(string)
        skip += 1

    return string, pos, skip

def sparse_hash(size, lengths):
    string = list(range(0, size))
    pos, skip = 0, 0

    for _ in range(0, 64):
        string, pos, skip = hash_round(string, lengths, pos, skip)

    return string

def dense_hash(sparse_hash):
    groups = zip(*[iter(sparse_hash)] * 16)
    reduced = [reduce(xor, g, 0) for g in groups]
    return bytes(reduced).hex()

def knot_hash(string):
    lengths = list(map(ord, string)) + [17, 31, 73, 47, 23]
    return dense_hash(sparse_hash(256, lengths))

# Grid ##############################################################

def hash_to_row(knot_hash):
    return "".join([bin(int(c, 16))[2:].zfill(4) for c in knot_hash])

def generate_defrag_grid(key):
    grid = []
    for row in range(0, 128):
        hash_input = key + "-" + str(row)
        result = knot_hash(hash_input)
        grid.append(hash_to_row(result))
    return grid

# Connected Components ##############################################

class ConnectedComponents(object):

    def __init__(self, grid):
        self.nodes = {}       # (x,y) -> Label mappings
        self.equivalence = {} # Label -> Region mappings
        self.regions = set()  # Unique region ids
        self.next_label = 0

        self._pass1_connect(grid)
        self._pass2_flatten()

    def _region_from_label(self, value):
        parent_value = self.equivalence[value]
        assert value != parent_value
        if parent_value is None:
            return value
        else:
            return self._region_from_label(parent_value)

    def _pass1_connect(self, grid):
        for y in range(len(grid)):
            for x in range(len(grid[0])):

                # Not considering regions of 0s
                if grid[x][y] == '0':
                    continue

                # Calculate neighbor info
                pos = (x,y)
                top_used = y > 0 and grid[x][y-1] == '1'
                top_label = self.nodes[(x, y-1)] if top_used else None
                top_region = self._region_from_label(top_label) if top_used else None
                left_used = x > 0 and grid[x-1][y] == '1'
                left_label = self.nodes[(x-1, y)] if left_used else None
                left_region = self._region_from_label(left_label) if left_used else None

                # Determine neighbor connections
                if top_used and left_used:
                    first = min(left_region, top_region)
                    self.nodes[pos] = first
                    if top_region != left_region:
                        # Merge regions
                        last = max(left_region, top_region)
                        self.equivalence[last] = first

                elif not left_used and not top_used:
                    # Start new region
                    self.nodes[pos] = self.next_label
                    self.equivalence[self.next_label] = None
                    self.next_label += 1

                elif left_used:
                    # Use left region
                    self.nodes[pos] = left_label

                elif top_used:
                    # Use top region
                    self.nodes[pos] = top_label

    def _pass2_flatten(self):
        for pos, label in self.nodes.items():
            label = self.nodes[pos]
            region = self._region_from_label(label)
            self.nodes[pos] = region
            self.regions.add(region)

# Entry Point #######################################################

key = 'amgozmfv'
#key = 'flqrgnkx'

grid = generate_defrag_grid(key)
cc = ConnectedComponents(grid)
print('Regions:', len(cc.regions)) # = 1086

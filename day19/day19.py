import string
import operator as op

# Class #############################################################

class PathFinder(object):

    def __init__(self, grid):
        self.grid = grid
        self.size_x = len(grid[0])
        self.size_y = len(grid)

    # Grid ############################

    def find_entry_point(self):
        x_pos = self.grid[0].index('|')
        return (x_pos, 0), (0, 1) 

    def get_tile(self, pos):
        x,y = pos
        if x < 0 or x >= self.size_x:
            return ' '
        if y < 0 or y >= self.size_y:
            return ' '
        return self.grid[y][x]

    # Tuple ###########################

    def offset(self, a, b,):
        return tuple(map(op.add, a, b))

    def rotate(self, x, y):
        offsets = [(0,1),(1,0),(0,-1),(-1,0)]
        i = (offsets.index(x) + y) % len(offsets)
        return offsets[i]

    # Path ############################

    def move(self, pos, fwd):
        directions = [fwd, self.rotate(fwd, -1), self.rotate(fwd, 1)]
        neighbors = [self.offset(pos, d) for d in directions]
        for n_pos, n_dir in zip(neighbors, directions):
            if self.get_tile(n_pos) != ' ':
                return n_pos, n_dir
        return None, None

    def traverse(self):
        tiles = ['|']
        pos, fwd = self.find_entry_point()

        while True:
            print(pos)
            pos, fwd = self.move(pos, fwd)
            if pos:
                tiles.append(self.get_tile(pos))
            else:
                return tiles

# Entry Point #######################################################

grid = open('day19.txt').readlines()
#grid = open('day19_test.txt').readlines()

pf = PathFinder(grid)
tiles = pf.traverse()
print("Letters:", "".join([t for t in tiles if t in string.ascii_letters])) # = PVBSCMEQHY
print("Steps:", len(tiles)) # = 17736

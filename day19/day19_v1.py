import string
import operator as op

# NOT WORKING

# Class #############################################################

class PathFinder(object):

    def __init__(self, grid):
        self.grid = grid
        self.size_x = len(grid[0])
        self.size_y = len(grid)

    def find_entry_point(self):
        x_pos = self.grid[0].index('|')
        return ((x_pos,-1), (x_pos,0))

    def get_tile(self, x, y):
        if x < 0 or x >= self.size_x:
            return ' '
        if y < 0 or y >= self.size_y:
            return ' '
        return self.grid[x][y]

    def move(self, then, now):
        at = self.get_tile(*now)
        if at == '+':
            # Turn left or right
            pass
        else:
            # Go forward
            direction = tuple(map(op.sub, now, then))
            new = tuple(map(op.add, now, direction))
            then, now = now, new
            
        return then, now

    def traverse(self):
        letters = []
        then, now = self.find_entry_point()
        while True:
            print(now)
            then, now = self.move(then, now)

            c = self.get_tile(*now)
            if c in string.ascii_uppercase:
                letters.append(c)

# Entry Point #######################################################

grid = open('day19_test.txt').readlines()
pf = PathFinder(grid)
letters = pf.traverse()

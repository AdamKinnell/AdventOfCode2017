import unittest
import operator
from collections import defaultdict

"""
    Sum all neighboring tiles.
"""
def sum_neighbors(pos, grid):
    directions = [
        ( 0, 1), # Up
        ( 1, 1), # Up-Right
        ( 1, 0), # Right
        ( 1,-1), # Down-Right
        ( 0,-1), # Down
        (-1,-1), # Down-Left
        (-1, 0), # Left
        (-1, 1), # Up-left
    ]

    neighbor_values = [grid[tuple(map(operator.add, pos, offset))] for offset in directions]
    return sum(neighbor_values)

"""
    Index is 1-based
"""
def calc_value_at_index(exit_requirement):

    grid = defaultdict(int)
    grid[(0,0)] = 1

    direction = 0
    directions = [
        ( 0, 1), # Up
        (-1, 0), # Left
        ( 0,-1), # Down
        ( 1, 0), # Right
    ]

    position = (1, 0)
    index = 2
    ring = 1

    if exit_requirement((0,0), 1, 0, 1):
        return 1

    while True:

        # Calculate value for this tile
        n = sum_neighbors(position, grid)
        grid[position] = n

        # Exit if finished
        if exit_requirement(position, index, ring, n):
            return n

        # Turn left if required
        is_on_corner = abs(position[0]) == abs(position[1]) == ring
        if direction <= 2 and is_on_corner:
            # Stay in current ring
            direction = (direction + 1) % len(directions)
        if direction == 3 and position[0] == ring + 1:
            # Move to next ring
            direction = (direction + 1) % len(directions)   
            ring += 1

        # Move to next tile
        position = tuple(map(operator.add, position, directions[direction]))
        index += 1

# Unit Tests ########################################################

class TestCalcValue(unittest.TestCase):

    def test_1(self):
        self.assertEqual(calc_value_at_index(lambda p,i,r,n: i == 1), 1)

    def test_2(self):
        self.assertEqual(calc_value_at_index(lambda p,i,r,n: i == 2), 1)

    def test_3(self):
        self.assertEqual(calc_value_at_index(lambda p,i,r,n: i == 3), 2)

    def test_4(self):
        self.assertEqual(calc_value_at_index(lambda p,i,r,n: i == 4), 4)

    def test_5(self):
        self.assertEqual(calc_value_at_index(lambda p,i,r,n: i == 5), 5)

    def test_6(self):
        self.assertEqual(calc_value_at_index(lambda p,i,r,n: i == 6), 10)

    def test_7(self):
        self.assertEqual(calc_value_at_index(lambda p,i,r,n: i == 7), 11)

# Entry Point #######################################################

if __name__ == "__main__":
    #unittest.main()
    print(calc_value_at_index(lambda p,i,r,n: n > 361527))

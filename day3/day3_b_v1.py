import unittest
from math import sqrt, ceil

"""
    Get the coordinate of a number <n> on a counter-clockwise spiral lattice.
"""
def get_coord(n):

    if n == 1:
        return (0, 0)

    # Get ring info
    ring = int(ceil((sqrt(n) - 1) / 2)) # 0-based ring around the center.
    side_length = 2*ring + 1            # Length of each of the 4 sides of the ring.
    perimeter = ring * 8                # Count of numbers in this ring
    largest = side_length * side_length # Largest number in this ring.
    smallest = largest - perimeter      # Largest number in the previous ring.

    # Find distance from center of closest side
    ring_pos = n - smallest                             # Position within the current ring, counter-clockwise; (0, perimeter]
    eighth =  (ring_pos / ring)                         # Position within the current ring, counter-clockwise, in eighths; (0,8]
    side_center_pct = ((8 - eighth) % 2) - 1            # Percentage from side center, larger numbers clockwise; [-1,1)
    side_center_offset = round(side_center_pct * ring)  # Offset of x from side center, larger numbers clockwise; [-ring,ring]

    # Get coordinate
    side = ceil(eighth / 2) # Counter-clockwise; [1,4]
    sides = {
        #     x                     y
        1: ( ring, -side_center_offset ),
        2: ( side_center_offset,  ring ),
        3: (-ring,  side_center_offset ),
        4: (-side_center_offset, -ring )
    }

    return sides[side]

"""
    The space/time complexity is O(n) with proper caching.
    Needs recursion depth of n (361527 + 1 for this problem).

    Therefore, this method will not work.
"""
def get_value_at(pos):

    # Base case
    if pos == (0, 0):
        return 1

    # Recursive case
    x, y = pos
    directions = [
        ((-1, 1), lambda: 0), # Up-left
        (( 0, 1), lambda: 0), # Up
        (( 1, 1), lambda: 0), # Up-Right
        (( 1, 0), lambda: 0), # Right
        (( 1,-1), lambda: 0), # Down-Right
        (( 0,-1), lambda: 0), # Down
        ((-1,-1), lambda: 0), # Down-Left
        ((-1, 0), lambda: 0), # Left
    ]

    applicable = filter(lambda x: x[1](), directions)
    return sum([get_value_at((x + x_, y + y_)) for (x_,y_), _ in applicable])

# Unit Tests ########################################################

class TestFindCoord(unittest.TestCase):

    def test_1(self):
        self.assertEqual(get_coord(1), (0,0))

    def test_26(self):
        self.assertEqual(get_coord(26), (3,-2))

    def test_31(self):
        self.assertEqual(get_coord(31), (3,3))

    def test_37(self):
        self.assertEqual(get_coord(37), (-3,3))

    def test_43(self):
        self.assertEqual(get_coord(43), (-3,-3))

    def test_49(self):
        self.assertEqual(get_coord(49), (3,-3))

class TestCalcValue(unittest.TestCase):

    def test_1(self):
        self.assertEqual(get_value_at((0,0)), 1)

    def test_2(self):
        self.assertEqual(get_value_at((1,0)), 1)

    def test_3(self):
        self.assertEqual(get_value_at((1,1)), 2)

    def test_4(self):
        self.assertEqual(get_value_at((0,1)), 4)

    def test_5(self):
        self.assertEqual(get_value_at((-1,1)), 5)

# Entry Point #######################################################

if __name__ == "__main__":

    for x in range(26,50):
        get_coord(x)

    unittest.main()

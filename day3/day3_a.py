import unittest
from math import sqrt, ceil


def count_steps_to_center_from(x):

    if x == 1:
        return 0

    # Get ring info
    ring = int(ceil((sqrt(x) - 1) / 2)) # 0-based ring around the center.
    side_length = 2*ring + 1            # Length of each of the 4 sides of the ring.
    perimeter = ring * 8                # Count of numbers in this ring
    largest = side_length * side_length # Largest number in this ring.
    smallest = largest - perimeter      # Largest number in the previous ring.

    # Find distance from center of closest side.
    ring_pos = x - smallest                             # Position within the current ring; [1, perimeter]
    eighth = ring_pos / ring                            # Position within the current ring, in eighths; [0,8]
    side_center_pct = (eighth % 2) - 1                  # Percentage from side center; [-1,1]
    side_center_offset = round(side_center_pct * ring)  # Offset of x from side center; [-ring,ring]
    side_center_distance = abs(side_center_offset)      # Distance from side center; [0,ring]

    # Find distance to center of grid via Manhattan distance.
    steps_to_center = ring + side_center_distance
    return steps_to_center

# Unit Tests ########################################################

class TestFindSteps(unittest.TestCase):

    def test_1(self):
        self.assertEqual(count_steps_to_center_from(1), 0)

    def test_12(self):
        self.assertEqual(count_steps_to_center_from(12), 3)

    def test_23(self):
        self.assertEqual(count_steps_to_center_from(23), 2)

    def test_1024(self):
        self.assertEqual(count_steps_to_center_from(1024), 31)

# Entry Point #######################################################

if __name__ == "__main__":
    code = 361527
    print(count_steps_to_center_from(code))

    unittest.main()

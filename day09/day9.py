import unittest

def process(stream):
    depth = 0
    score = 0
    garbage = 0
    in_garbage = False

    iter_stream = iter(stream)
    for c in iter_stream:

        if c == '!':
            next(iter_stream)
            continue

        if in_garbage:
            if c == '>':
                in_garbage = False
            else:
                garbage += 1

        if not in_garbage:
            if c == '{':
                depth += 1
                score += depth
            if c == '}':
                depth -= 1
            if c == '<':
                in_garbage = True

    return score, garbage

# Tests #############################################################

class TestProcessStream(unittest.TestCase):

    def test_garbage(self):
        self.assertEqual(process('<>')[1], 0)
        self.assertEqual(process('<random characters>')[1], 17)
        self.assertEqual(process('<<<<>')[1], 3)
        self.assertEqual(process('<{!>}>')[1], 2)
        self.assertEqual(process('<!!>')[1], 0)
        self.assertEqual(process('<!!!>>')[1], 0)
        self.assertEqual(process('<{o"i!a,<{i<a>')[1], 10)


# Entry Point #######################################################

stream = open('day9.txt').read()
score, garbage = process(stream)
print('Score:', score)
print('Garbage:', garbage)

unittest.main()

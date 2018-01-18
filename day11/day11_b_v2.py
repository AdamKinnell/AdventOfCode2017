from itertools import accumulate

mappings = {
    'n':  ( 0,  1, -1),
    's':  ( 0, -1,  1),
    'ne': ( 1,  0, -1),
    'sw': (-1,  0,  1),
    'nw': (-1,  1,  0),
    'se': ( 1, -1,  0),
}

directions = open('day11.txt').read().split(',')

offsets = map(mappings.get, directions)
steps = list(accumulate(offsets, lambda x, y: tuple(map(sum, zip(x, y)))))
distances = list(map(lambda x: max(map(abs, x)), steps))
furthest = max(distances)

print('Final Position:', steps[-1])
print('Furthest Distance:', furthest)
print('Final Distance:', distances[-1])

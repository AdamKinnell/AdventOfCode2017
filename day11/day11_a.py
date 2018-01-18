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
position = tuple(map(sum, zip(*offsets)))
distance = max(map(abs, position))

print('Position:', position)
print('Distance:', distance)

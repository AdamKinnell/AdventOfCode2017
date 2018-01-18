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
furthest = 0
position = (0,0,0)
for offset in offsets:
    position = tuple(map(sum, zip(position, offset)))
    distance = max(map(abs, position))
    furthest = max(furthest, distance)

print('Position:', position)
print('Furthest:', furthest)


moves = open('day16.txt').read().split(',')

programs = list("abcdefghijklmnop")
for move in moves:
    if move[0] == 's':
        # Rotate list
        size = int(move[1:])
        programs = programs[-size:] + programs[:-size]
    if move[0] == 'x':
        # Swap indexes
        i,j = map(int, move[1:].split('/'))
        programs[i], programs[j] = programs[j], programs[i]
    if move[0] == 'p':
        # Swap values
        a,b = move[1:].split('/')
        i,j = programs.index(a), programs.index(b)
        programs[i], programs[j] = programs[j], programs[i]

print("".join(programs))

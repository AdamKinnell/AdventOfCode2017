
moves = open('day16.txt').read().split(',')
start = list("abcdefghijklmnop")

seen = [list(start)]
programs = list(start)
while True:
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

    if programs == seen[0]:
        cycle_length = len(seen)
        print('Repeats after:', cycle_length)
        print('1,000,000 =', "".join(seen[1_000_000 % cycle_length]))
        break
    else:
        seen.append(list(programs))


states = {
# [State]  [  If 0  ]  [  If 1  ]
    'a' : [(1, 1,'b'), (0, 1,'c')],
    'b' : [(0,-1,'a'), (0, 1,'d')],
    'c' : [(1, 1,'d'), (1, 1,'a')],
    'd' : [(1,-1,'e'), (0,-1,'d')],
    'e' : [(1, 1,'f'), (1,-1,'b')],
    'f' : [(1, 1,'a'), (1, 1,'e')],
}        #  |  |  |
         #  |  |  +---- Next state
         #  |  +------- Direction to move
         #  +---------- Value to write

pos = 0
state = 'a'
tape = {}

for step in range(0, 12_368_930):
    val = tape.get(pos, 0)
    tape[pos], move, state = states[state][val]
    pos += move

print("Ones:", len([x for x in tape.values() if x == 1])) # = 2725


# Functions #########################################################

states = [
    ('clean'   , lambda nxt: nxt * -1j), # Turn left
    ('weakened', lambda nxt: nxt *  1 ), # No turn
    ('infected', lambda nxt: nxt *  1j), # Turn right
    ('flagged' , lambda nxt: nxt * -1 ), # Turn around
]
state_names = [n for n,_ in states]

def simulate(grid, iterations):
    pos = 0 + 0j
    nxt = 0 - 1j
    infected = 0

    for _ in range(0, iterations):
        state = grid.get(pos, state_names.index('clean'))
        _, nxt_func = states[state]
        nxt = nxt_func(nxt)

        state = (state + 1) % len(states)
        grid[pos] = state
        if state == state_names.index('infected'):
            infected += 1

        pos += nxt

    return infected

# Entry Point #######################################################

lines = open('day22.txt').readlines()
#lines = open('day22_test.txt').readlines()

# Move origin to center
center = len(lines) // 2
grid = { complex(x-center, y-center) : state_names.index('infected')
            for y,row  in enumerate(lines)
            for x,tile in enumerate(row)
            if tile == '#'}

# Show results
infected = simulate(grid, 10_000_000)
print("Newly Infected:", infected) # = 2512103

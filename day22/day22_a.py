lines = open('day22.txt').readlines()

# Move origin to center
center = len(lines) // 2
grid = set([complex(x-center, y-center)
            for y,row in enumerate(lines)
            for x,tile in enumerate(row)
            if tile == '#'])

# Simulate infection
pos = 0 + 0j
nxt = 0 - 1j
infected = 0
for _ in range(0, 10000):
    
    if pos in grid:
        # Currently infected
        nxt = complex(-nxt.imag, nxt.real) # Turn right
        grid.remove(pos)                   # Disinfect
    else:
        # Currently clean
        nxt = complex(nxt.imag, -nxt.real) # Turn left
        grid.add(pos)                      # Infect
        infected += 1

    # Move
    pos += nxt

# Show results
print("Newly Infected:", infected) # = 5530

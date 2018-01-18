
def redistribute(banks):
    bank = banks.index(max(banks))
    blocks = banks[bank]
    banks[bank] = 0

    while blocks > 0:
        bank = (bank + 1) % len(banks) # Move to next bank
        banks[bank] += 1               # Add a remaining block
        blocks -= 1

    return banks

def find_loop(banks):
    cycles = 0
    seen = {tuple(banks): cycles}

    while True:
        banks = redistribute(banks)
        cycles += 1

        if tuple(banks) in seen:
            return cycles - seen[tuple(banks)]
        else:
            seen[tuple(banks)] = cycles

# Entry Point #######################################################

memory = list(map(int, open("day6.txt").read().split()))
# memory = [0,2,7,0] # = 4

print('Cycle length:', find_loop(memory))

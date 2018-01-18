
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
    seen = set([tuple(banks)])

    while True:
        banks = redistribute(banks)
        cycles += 1

        if tuple(banks) in seen:
            return cycles
        else:
            seen.add(tuple(banks))

# Entry Point #######################################################

memory = list(map(int, open("day6.txt").read().split())) # = 3156
#memory = [0,2,7,0] # = 5

print(memory)
print(find_loop(memory))
print(memory)

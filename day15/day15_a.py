g1_seed = 634
g1_factor = 16807
g2_seed = 301
g2_factor = 48271
g_mod = 2147483647
mask = (2**16) - 1

matches = 0
g1_last = g1_seed
g2_last = g2_seed
for _ in range(0, 40_000_000):
    g1_last = (g1_last * g1_factor) % g_mod
    g2_last = (g2_last * g2_factor) % g_mod

    if g1_last & mask == g2_last & mask:
        matches += 1
        print(matches)

print('Final Count:', matches) # = 573

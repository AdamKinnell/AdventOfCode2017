skip = 328
mask = 2**20 -1

size = 1
pos = 0
after_zero = None
for i in range(1,50_000_000 + 1):
    pos = (pos + skip) % size
    size += 1
    pos += 1

    # Track number after zero (index 0)
    if pos == 1:
        after_zero = i
        print('New Number:', after_zero)

    # Show progress
    if i & mask == 0:
        print('Progress:', i)

print(after_zero)

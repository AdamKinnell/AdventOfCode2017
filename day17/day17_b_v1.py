# Too slow to complete.

skip = 328

lst = [0]
pos = 0
for i in range(1,50_000_000 + 1):
    pos = (pos + skip) % len(lst)
    lst.insert(pos, i)
    pos += 1

    if i & (2**16 -1) == 0:
        print('Progress:', i)

print('Value after 0:', lst[lst.index(0) + 1])

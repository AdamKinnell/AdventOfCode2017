from functools import reduce
from operator import xor

def reverse_elements(lst, start_i, count):
    to_end = min(len(lst) - start_i, count)
    from_start = count - to_end

    elements = lst[start_i:start_i+to_end]
    elements += lst[0:from_start]
    elements = list(reversed(elements))
    lst[start_i:start_i+to_end] = elements[:to_end]
    lst[0:from_start] = elements[to_end:]

    return lst

def hash_round(string, lengths, pos=0, skip=0):
    for length in lengths:
        string = reverse_elements(string, pos, length)
        pos = (pos + length + skip) % len(string)
        skip += 1

    return string, pos, skip

def sparse_hash(size, lengths):
    string = list(range(0, size))
    pos, skip = 0, 0

    for _ in range(0, 64):
        string, pos, skip = hash_round(string, lengths, pos, skip)

    return string

def dense_hash(sparse_hash):
    groups = zip(*[iter(sparse_hash)] * 16)
    reduced = [reduce(xor, g, 0) for g in groups]
    return bytes(reduced).hex()

def knot_hash(string):
    lengths = list(map(ord, string)) + [17, 31, 73, 47, 23]
    return dense_hash(sparse_hash(256, lengths))

def count_bits(hexa):
    return sum([bin(int(c, 16)).count('1') for c in hexa])

# Entry Point #######################################################

key = 'amgozmfv'

used = 0
for row in range(0, 128):
    hash_input = key + "-" + str(row)
    result = knot_hash(hash_input)
    used += count_bits(result)

print('Used Squares:', used)

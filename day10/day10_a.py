
def reverse_elements(lst, start_i, count):
    to_end = min(len(lst) - start_i, count)
    from_start = count - to_end

    elements = lst[start_i:start_i+to_end]
    elements += lst[0:from_start]
    elements = list(reversed(elements))
    lst[start_i:start_i+to_end] = elements[:to_end]
    lst[0:from_start] = elements[to_end:]

    return lst

def hash(size, lengths):
    string = list(range(0, size))
    pos = 0
    skip = 0
    
    for length in lengths:
        string = reverse_elements(string, pos, length)
        pos = (pos + length + skip) % len(string)
        skip += 1

    return string

# Entry Point #######################################################

lengths = list(map(int, open('day10.txt').read().split(',')))
string = hash(256, lengths)

print(string)
print(string[0] * string[1]) # = 46600

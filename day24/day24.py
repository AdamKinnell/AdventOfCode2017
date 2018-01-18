
# Functions #########################################################

def connectable_components(all_components, used_components, to_port):
    for i, (a_port, b_port) in enumerate(all_components):
        if i not in used_components:
            if a_port == to_port:
                yield i, b_port
            elif b_port == to_port:
                yield i, a_port

def build_all_bridges(all_components, used_components, from_port):
    connections = connectable_components(all_components, used_components, from_port)

    for i, to_port in connections:
        with_connection = used_components | set([i])
        yield with_connection
        yield from build_all_bridges(all_components, with_connection, to_port)

def bridge_strength(all_components, used_components):
    return sum((a+b for i in used_components
                    for (a,b) in [all_components[i]]))

# Entry Point #######################################################

#lines = open('day24_test.txt').readlines()
lines = open('day24.txt').readlines()

components = list(l.strip().split('/') for l in lines)
components = list((int(a),int(b)) for a,b in components)

all_bridges = list(build_all_bridges(components, set(), 0))

attributes = [(bridge_strength(components, b), len(b)) for b in all_bridges]
longest           = max((l for s,l in attributes))
strongest         = max((s for s,l in attributes))
strongest_longest = max((s for s,l in attributes if l == longest))

print("Strongest Bridge:"         , strongest)         # = 1695
print("Longest Bridge:"           , longest)           # = 36
print("Strongest, Longest Bridge:", strongest_longest) # = 1673

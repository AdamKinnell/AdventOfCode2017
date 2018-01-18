from functools import partial
from collections import Counter

def parse_program(line):
    parts = "".join([c for c in line if c not in "(),"]).split()
    program = {
        'name'        : parts[0],
        'weight'      : int(parts[1]),
        'children'    : parts[3:],
        'total_weight': None
    }
    return program['name'], program

def build_tree(text):
    return dict(map(parse_program, text))

def find_root_program(tree):
    name_counter = Counter()

    # Find references
    for program in tree.values():
        name_counter[program['name']] += 1
        for a in program['children']:
            name_counter[a] += 1

    # Find the name that only appears once
    name = name_counter.most_common()[-1][0]
    return tree[name]

def update_total_weights(tree, node):
    children = map(tree.get, node['children'])
    node['total_weight'] = node['weight'] + sum(map(partial(update_total_weights, tree), children))
    return node['total_weight']

def fix_invalid_weight(tree, node, expected_total_weight=None):
    children = list(map(tree.get, node['children']))
    weights = [child['total_weight'] for child in children]
    weight_counts = Counter(weights).most_common()

    if len(weight_counts) == 2:
        # Disk is unbalanced; the problem node is above.
        (normal, _), (unbalanced, _) = Counter(weights).most_common()
        problem_node = next(c for c in children if c['total_weight'] == unbalanced)
        return fix_invalid_weight(tree, problem_node, normal)
    elif len(weight_counts) == 1:
        # Disc is balanced; this node's weight is wrong.
        difference = expected_total_weight - node['total_weight']
        node['weight'] += difference
        return node
    else:
        raise NotImplementedError("Unsupported unique weight count.")

# Entry Point #######################################################

tree = build_tree(open("day7.txt").readlines())
#tree = build_tree(open("day7_test.txt").readlines())

root = find_root_program(tree)
update_total_weights(tree, root)
fixed_node = fix_invalid_weight(tree, root)
#update_total_weights(tree, root)
#fixed_node = fix_invalid_weight(tree, root)

print("Fixed:", fixed_node)

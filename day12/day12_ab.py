
# Functions #########################################################

class Graph(object):

    def __init__(self):
        self.nodes = {}      # Node -> Group mappings
        self.groups = {}     # Group -> Node mappings
        self._next_group = 0 # Unique id for new groups

    def parse_node(self, line):
        components = line.split('<->')
        node = int(components[0])
        connections = list(map(int,components[1].split(',')))
        return self.add_node(node, connections)

    def add_node(self, node, connections):

        # Create new group
        new_group = self._next_group
        self._next_group += 1

        # Assume node is disconnected
        self.nodes[node] = new_group
        self.groups[new_group] = [node]

        for c in connections:
            if c in self.nodes:
                old_group = self.nodes[c]
                if old_group != new_group:
                    # Migrate existing nodes to this group
                    self.change_group(old_group, new_group)
            else:
                # Add unseen node to this group
                self.nodes[c] = new_group
                self.groups[new_group].append(c)

    def change_group(self, old_group, new_group):
        # Move to new group
        to_move = self.groups[old_group]
        self.groups[new_group].extend(to_move)
        del self.groups[old_group]

        # Update group references
        for node in to_move:
            self.nodes[node] = new_group

    def compact_groups(self):
        for k,v in self.groups.items():
            self.groups[k] = list(set(v))

# Entry Point #######################################################

lines = open('day12.txt').readlines()

# Build graph
graph = Graph()
for line in lines:
    graph.parse_node(line)
graph.compact_groups()

# Print info
zero_group = graph.nodes[0]
zero_buddies = graph.groups[zero_group]
#print("0's group:", zero_group)
#print("0's buddies:", zero_buddies)
print("Part 1 - Size of 0's group:", len(zero_buddies))
print("Part 2 - Number of groups:", len(graph.groups))

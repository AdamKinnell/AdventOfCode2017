
# Functions #########################################################

class FireWall(object):

    def __init__(self, scanners):
        self.scanners = scanners

    def catches_packet_at(self, layer, time):
        if layer in self.scanners:
            depth = self.scanners[layer]
            return time % (depth*2 - 2) == 0
        else:
            return False

    def traverse(self, start_time):
        caught_layers = []
        severity = 0
        for layer, depth in self.scanners.items():
            if self.catches_packet_at(layer, start_time + layer):
                caught_layers.append(layer)
                severity += layer * depth

        return caught_layers, severity

    def traverse_until_caught(self, start_time):
        for layer, _ in self.scanners.items():
            if self.catches_packet_at(layer, start_time + layer):
                return False
        return True

    def brute_force(self):
        delay = 0
        while True:
            if self.traverse_until_caught(delay):
                return delay
            delay += 1

# Entry Point #######################################################

lines = open('day13.txt').readlines()
#lines = open('day13_test.txt').readlines()

scanners = dict((map(int, l.split(':')) for l in lines))
fw = FireWall(scanners)
print("Severity w/ 0 delay:", fw.traverse(0)[1]) # = 788
print("Picoseconds Delay:", fw.brute_force())    # = 3905748

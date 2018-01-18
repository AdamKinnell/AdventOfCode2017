# Probably not going to work.
#
# This assumes that it is possible to
# choose a delay that results in intercepting every single scanner.

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

    def get_patrol_length(self, depth):
        return depth*2 - 2

    def generate_intercept_delays(self, layer, depth):
        multiple = self.get_patrol_length(depth)
        delay = layer
        while True:
            yield delay       # I'm so sorry...
            yield delay       # Easiest way to enable peeking the next element.
            delay += multiple

    def _check_intercept_all(self, delay, rest):
        if not rest:
            return True

        nxt = next(rest[0])
        while nxt < delay:
            # Skip they delays that can't match
            nxt = next(rest[0])

        print(delay, nxt)
        if nxt == delay:
            # Matching delay! Now check the rest
            return self._check_intercept_all(delay, rest[1:])
        else:
            # Non-matching delay; they will not intercept at this delay.
            return False

    def calc_intercept_all_delay(self):
        longest_patrols = sorted(self.scanners.items(), key=lambda x: self.get_patrol_length(x[1]), reverse=True)
        delay_lists = [self.generate_intercept_delays(l,d) for l,d in longest_patrols]

        # Find a delay which results in intercepting every scanner
        for delay in delay_lists[0]:
            if self._check_intercept_all(delay, delay_lists[1:]):
                return delay

            # Skip duplicate
            next(delay_lists[0]) 


# Entry Point #######################################################

#lines = open('day13.txt').readlines()
lines = open('day13_test.txt').readlines()

scanners = dict((map(int, l.split(':')) for l in lines))
fw = FireWall(scanners)
delay = fw.calc_intercept_all_delay()
print(delay)

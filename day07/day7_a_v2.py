from collections import Counter
import re

# The program at the bottom of the stack
# will only be ever be referenced once in the list.
#
# This is because, otherwise, another program would have to list
# it as being above itself.
#
# Due to this, we can simply find which program name is listed exactly once.

programs = open("day7.txt").read()
names = re.findall(r'[a-z]+', programs)
name_counter = Counter(names)
print('Root:', name_counter.most_common()[-1][0]) # = 'hmvwl'

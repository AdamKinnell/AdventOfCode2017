from collections import namedtuple, Counter

Program = namedtuple('Program', ['name', 'above'])

def parse_program(program):
    parts = program.replace(',','').split()
    return Program(parts[0], parts[3:])

def find_bottom_program(programs):
    name_counter = Counter()

    # Find references
    for program in programs:
        name_counter[program.name] += 1
        for a in program.above:
            name_counter[a] += 1

    # Find the name that only appears once
    return name_counter.most_common()[-1]

# Entry Point #######################################################

#programs = list(map(parse_program, open("day7_test.txt").readlines())) # = tknk
programs = list(map(parse_program, open("day7.txt").readlines())) # = hmvwl
#print(programs)
print('Bottom:', find_bottom_program(programs))

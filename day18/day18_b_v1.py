from collections import defaultdict

# NOT WORKING

# Functions #########################################################

opcodes = {
    'set' : lambda regs, a, b: (a, b),
    'add' : lambda regs, a, b: (a, regs[a] + b),
    'mul' : lambda regs, a, b: (a, regs[a] * b),
    'mod' : lambda regs, a, b: (a, ((regs[a] % b) + b) % b),
    'jgz' : lambda regs, a, b: ('pc', regs['pc'] + (b - 1 if regs[a] > 0 else 0)),
    'snd' : lambda regs, a, _: ('sent', regs['sent'] + 1, regs['_snd'].append(regs[a])),
    'rcv' : lambda regs, a, _: ((a, regs['_rcv'].pop(0)) if regs['_rcv'] else ('_wait', None))
}

def parse_reg_imm(regs, arg):
    if arg[-1].isdigit():
        return int(arg)
    else:
        return regs[arg]

def run(code):
    p0_pipe, p1_pipe = [], []
    p0_regs = defaultdict(int, {'pc':0, 'p':0, '_snd':p1_pipe, '_rcv':p0_pipe})
    p1_regs = defaultdict(int, {'pc':0, 'p':1, '_snd':p0_pipe, '_rcv':p1_pipe})
    while True:
        for regs in (p0_regs, p1_regs):

            # Decode
            opcode, arg1, *arg2 = code[regs['pc']]
            arg2 = parse_reg_imm(regs, arg2[0]) if arg2 else None

            # Execute
            reg, val, *_ = opcodes[opcode](regs, arg1, arg2)
            if reg == '_wait':
                print('Program', regs['p'], 'is awaiting data.')
                regs['_wait'] = True
            else:
                regs[reg] = val
                regs['pc'] += 1
                if regs['_wait']:
                    print('Program', regs['p'], 'has recieved data.')
                    regs['_wait'] = True

            # Debug
            print('Program', regs['p'], 'queue size:', len(regs['_rcv']))

        if p0_regs['_wait'] and p1_regs['_wait']:
            print("Deadlock")
            break

# Entry Point #######################################################

instructions = list(map(str.split, open('day18_test.txt').readlines()))
run(instructions)

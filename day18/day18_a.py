from collections import defaultdict

# Functions #########################################################

opcodes = {
    'set' : lambda regs, a, b: (a, b),
    'add' : lambda regs, a, b: (a, regs[a] + b),
    'mul' : lambda regs, a, b: (a, regs[a] * b),
    'mod' : lambda regs, a, b: (a, regs[a] % b),
    'jgz' : lambda regs, a, b: ('pc', regs['pc'] + (b - 1 if regs[a] > 0 else 0)),
    'snd' : lambda regs, a, _: ('sound', regs[a]),
    'rcv' : lambda regs, a, _: ('result', regs['sound'] if regs[a] != 0 else regs[a])
}

def parse_reg_imm(regs, arg):
    if arg[-1].isdigit():
        return int(arg)
    else:
        return regs[arg]

def run(code):
    regs = defaultdict(int, {'pc' : 0,})
    while 'result' not in regs:

        # Decode
        opcode, arg1, *arg2 = code[regs['pc']]
        arg2 = parse_reg_imm(regs, arg2[0]) if arg2 else None

        # Execute
        reg, val = opcodes[opcode](regs, arg1, arg2)
        regs[reg] = val
        regs['pc'] += 1

    return regs['result']

# Entry Point #######################################################

instructions = list(map(str.split, open('day18.txt').readlines()))
print('Recovered:', run(instructions))

from collections import defaultdict

# Functions #########################################################

def parse_reg_imm(regs, arg):
    if arg[-1].isdigit():
        return int(arg)
    else:
        return regs[arg]

def run(code):
    p0_pipe, p1_pipe = [], []
    p0_regs = defaultdict(int, {'pc':0, 'p':0, '_wait':False, '_snd':p1_pipe, '_rcv':p0_pipe})
    p1_regs = defaultdict(int, {'pc':0, 'p':1, '_wait':False, '_snd':p0_pipe, '_rcv':p1_pipe})
    while True:
        for regs in (p0_regs, p1_regs):

            # Fetch
            opcode, arg1, *arg2 = code[regs['pc']]
            arg2 = parse_reg_imm(regs, arg2[0]) if arg2 else None

            # Decode & Execute
            if opcode == 'set':
                regs[arg1] = arg2
            if opcode == 'add':
                regs[arg1] += arg2
            if opcode == 'mul':
                regs[arg1] *= arg2
            if opcode == 'mod':
                regs[arg1] %= arg2
            if opcode == 'jgz':
                if parse_reg_imm(regs, arg1) > 0:
                    regs['pc'] += arg2
                    continue
            if opcode == 'snd':
                regs['_snd'].append(parse_reg_imm(regs,arg1))
                regs['_sent'] += 1
            if opcode == 'rcv':
                if regs['_rcv']:
                    regs[arg1] = regs['_rcv'].pop(0)
                    regs['_wait'] = False
                else:
                    regs['_wait'] = True
                    continue

            # Increment
            regs['pc'] += 1

        if p0_regs['_wait'] and p1_regs['_wait']:
            print("!!!Deadlock!!!")
            break

    return p0_regs, p1_regs

# Entry Point #######################################################

instructions = list(map(str.split, open('day18.txt').readlines()))
#instructions = list(map(str.split, open('day18_test.txt').readlines()))

p0, p1 = run(instructions)
print('Program 1 sent:', p1['_sent']) # = 6858

from collections import defaultdict

# Functions #########################################################

def parse_reg_imm(regs, arg):
    if arg[-1].isdigit():
        return int(arg)
    else:
        return regs[arg]

def run(code):
    pc = 0
    mul_count = 0
    regs = defaultdict(int)
    while pc in range(0, len(code)):

        # Fetch
        opcode, arg1, *arg2 = code[pc]
        arg2 = parse_reg_imm(regs, arg2[0]) if arg2 else None

        # Decode & Execute
        if opcode == 'set':
            regs[arg1] = arg2
        if opcode == 'sub':
            regs[arg1] -= arg2
        if opcode == 'mul':
            regs[arg1] *= arg2
            mul_count += 1
        if opcode == 'jnz':
            if parse_reg_imm(regs, arg1) != 0:
                pc += arg2
                continue

        # Increment
        pc += 1
    return mul_count

# Entry Point #######################################################

instructions = list(map(str.split, open('day23_a.txt').readlines()))
mul_count = run(instructions)
print('MUL run:', mul_count)

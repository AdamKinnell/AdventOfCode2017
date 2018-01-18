import operator
from collections import defaultdict

comparisons = {
    '<'  : operator.lt,
    '>'  : operator.gt,
    '<=' : operator.le,
    '>=' : operator.ge,
    '==' : operator.eq,
    '!=' : operator.ne,
}

operations = {
    'inc' : operator.add,
    'dec' : operator.sub,
}

# Entry Point #######################################################

#instructions = open('day8_test.txt').readlines()
instructions = open('day8.txt').readlines()

highest = 0
registers = defaultdict(int)
for instruction in instructions:
    op_reg, op, op_amt, _, cmp_reg, cmp, cmp_amt = instruction.split()
    if comparisons[cmp](registers[cmp_reg], int(cmp_amt)):
        registers[op_reg] = operations[op](registers[op_reg], int(op_amt))
        highest = max(highest, registers[op_reg])

print('Part 1:', max(registers.values()))
print('Part 2:', highest)


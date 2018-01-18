
def execute(code):
    pc, step = 0, 0

    while pc in range(0, len(code)):
        code[pc] += 1
        pc += code[pc] - 1
        step += 1
        
    return step

instructions = list(map(int,open("day5.txt").readlines())) # = 342669
#instructions = [0, 3 ,0, 1, -3] # = 5

print("Steps 'till exit:", execute(instructions))

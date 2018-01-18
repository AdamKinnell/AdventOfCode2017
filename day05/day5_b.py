
def execute(code):
    pc, step = 0, 0

    while pc in range(0, len(code)):
        
        jump = code[pc]
        if code[pc] >= 3:
            code[pc] -= 1
        else:
            code[pc] += 1

        pc += jump
        step += 1
        
    return step

instructions = list(map(int,open("day5.txt").readlines())) # = 25136209
#instructions = [0, 3 ,0, 1, -3] # = 10

print("Steps 'till exit:", execute(instructions))

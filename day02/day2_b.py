def rowfunc(row):
    row = sorted(row, reverse=True)
    for i, a in enumerate(row):
        for _, b in enumerate(row[i+1:]):
            if a / b == a // b:
                return a // b

file = open("day2.txt")
lines = file.readlines()
rows = [list(map(int, line.split('\t'))) for line in lines]

checksum = sum([rowfunc(row) for row in rows])
print('Checksum:', checksum) # = 303

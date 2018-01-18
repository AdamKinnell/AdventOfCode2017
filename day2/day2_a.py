file = open("day2.txt")
lines = file.readlines()
rows = [list(map(int, line.split('\t'))) for line in lines]
checksum = sum([max(row) - min(row) for row in rows])
print(checksum)

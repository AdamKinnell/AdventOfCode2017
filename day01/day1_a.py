captcha = open("day1.txt").read()
neighbors = zip(captcha, captcha[1:] + captcha[:1])
print(sum([int(a) for a,b in neighbors if a == b]))

# = 1119

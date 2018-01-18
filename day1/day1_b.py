captcha = open("day1.txt").read()
rotate = len(captcha) // 2
neighbors = zip(captcha, captcha[rotate:] + captcha[:rotate])
print(sum([int(a) for a,b in neighbors if a == b]))

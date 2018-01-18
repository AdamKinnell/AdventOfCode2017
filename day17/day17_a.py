
skip = 328
#skip = 3

lst = [0]
pos = 0
for i in range(1,2018):
    pos = (pos + skip) % len(lst)
    lst.insert(pos, i)
    pos += 1

print('Value after 2017:', lst[lst.index(2017) + 1]) # = 1670

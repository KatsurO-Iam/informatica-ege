from re import*
s = open('24_31129.txt').readline()

pat = compile('(?:([1234][0-4]*)|[0])([-*](([1-4][0-4]*)|[0]))*')
m = 0
for x in pat.finditer(s):
    m = max(m, len(x.group()))
print(m)
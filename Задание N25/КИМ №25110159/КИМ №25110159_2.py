from fnmatch import fnmatch

s = set()
for i in range(10, 100, 2):
    if fnmatch(str(i), '1?'):
        s.add(i)
s = list(s)
c = 0
for i in range(320400, 10**6):
    if all(i % x == 0 for x in s):
        print(i, i//max(s))
        c+=1
    if c == 5:
        break
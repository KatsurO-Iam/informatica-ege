from fnmatch import *
maxx = []
k = 0
for x in range(2 * 10**8, 1, -1):
    if fnmatch(str(x), '?2*4*0') and not fnmatch(str(x), '1*7*') and x % 42 == 0:
        print(x, x//42)
        k+=1
    if k == 5:
        break
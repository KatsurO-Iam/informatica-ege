from fnmatch import *

for x in range(253, 10**8, 253):
    if fnmatch(str(x), '12??15*6') and x % 253 == 0:
        print(x, x//253)
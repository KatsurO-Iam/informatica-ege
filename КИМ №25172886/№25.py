from fnmatch import *
from math import *
k  = 0
for n in range(750122, 10**9):
    if n % 8387 == 0 and fnmatch(str(n), '*75?122*'):
        print(n, n//8387)


# 550014 275007
# 550017 1567
# 550032 34377
# 550035 110007
# 550037 9017
from fnmatch import *
k  = 0
for n in range(700_001, 10**7):
    if n % 13 == 0 and not fnmatch(str(n), '*0??3*') and not fnmatch(str(n), '*4??2') and not fnmatch(str(n), '*1*'):
        print(n, sum(map(int, str(n))))
        k+=1
    if k == 5:
        break


# 550014 275007
# 550017 1567
# 550032 34377
# 550035 110007
# 550037 9017
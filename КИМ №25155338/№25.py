from fnmatch import *
def f(n):
    s = set()
    ans = []
    for i in range(2, int(n**0.5)+1):
        if n % i == 0:
            s.add(i)
            s.add(n//i)
    for x in s:
        if g(x) == True:
            ans.append(x)
    return ans
def g(n):
    for i in range(2, int(n**0.5)+1):
        if n % i == 0:
            return False
    return True

k = 0
for i in range(310001, 500000):
    t = f(i)
    if len(t) > 0:
        a = sum(t)//len(t)
        if a%6 == 0 and a% 10 !=4:
            print(i, a)
            k +=1
    if k == 6:
        break
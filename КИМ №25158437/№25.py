from fnmatch import *
# def f(n):
#     s = set()
#     ans = []
#     for i in range(2, int(n**0.5)+1):
#         if n % i == 0:
#             s.add(i)
#             s.add(n//i)
#     for x in s:
#         if g(x) == True:
#             ans.append(x)
#     return ans
# def g(n):
#     for i in range(2, int(n**0.5)+1):
#         if n % i == 0:
#             return False
#     return True

def f(n):
    c = 0
    for x in str(n):
        c+=int(x)
    return c

k = 0
for i in range(700_001, 10**6):
    if i % 13 == 0 and not fnmatch(str(i), '*0??3*') and not fnmatch(str(i), '*4??2') and not fnmatch(str(i), '*1*'):
        print(i, f(i))
        k+=1
    if k == 5:
        break
from itertools import combinations
cnt = 0
p = {1,2,3,4,5,6,7,8,9,10}
q = {2,4,8,10}
def f(x):
    Q = x in q
    P = x in p
    A = x in a
    return (Q <= A) and (A <= P)

for i in range(1,11):
    for a in combinations(p, i):
        if all(f(x) for x in p):
            cnt += 1
print(cnt)
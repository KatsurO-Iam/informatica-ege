from itertools import *

def f(n):
    p = 69 <= n <= 91
    q = 77 <= n <= 114
    a = a1 <= n <= a2

    return q <= ((p == q) or ((not p) <= a))
# ox = [i//4 for i in range(68*4, 120*4)]
ox = [*range(68, 120)]
m = float('inf')

for a1, a2 in combinations(ox, 2):
    if all(f(x) for x in ox):
        m = min(m, abs(a2 - a1))
print(m)
print(ox)

print(*combinations([1,2,3,4,5],3))
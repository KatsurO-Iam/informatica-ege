def f(n):
    s = ''
    while n > 0:
        s += str(n%3)
        n = n//3
    return s[::-1]

for n in range(1, 1000):
    r = f(n)
    R = ''
    if n % 3 == 0:
        r = r+ r[-2:]
    if n % 3 != 0:
        s = (r.count('1')+2*r.count('2'))*3
        r = r + f(s)
    R = int(r,3)
    if R % 2 != 0 and R > 208:
        print(R)
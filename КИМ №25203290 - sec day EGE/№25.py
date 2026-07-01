def prime(n):
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def f(n):
    s = set()
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            s.add(i)
            s.add(n//i)
    s = list(s)
    for x in s[:]:
        if prime(x) == False:
            s.remove(x)
    return sorted(list(s))

for i in range(8_117_600_757, 10**10):
    t = f(i)
    if len(t) > 0:
        if min(t) == 2 and max(t) % 2 != 0:
            m = max(t) - min(t)
            if prime(m) and str(m).count('1') >=4:
                print(i, m)

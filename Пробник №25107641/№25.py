def f(n):
    s = set()
    for i in range(3, int(n**0.5), 2):
        if n % i == 0:
            s.add(i)
            s.add(n // i)
    if len(s) > 70:
        return s
    return False
for x in range(321654, 654322):
    t = f(x)
    if all(map(lambda a: a % 2 != 0, t)):
        print(x, max(t))
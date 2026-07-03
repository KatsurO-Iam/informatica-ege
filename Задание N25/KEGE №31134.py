def f(n):
    for i in range(2, int(n ** 0.5)):
        if n % i == 0:
            return [i] + f(n // i)
    return [n]

for i in range(8_007_494_155, 8_107_494_155):
    t = list(set(f(i)))
    if len(t) > 1:
        m = max(t)+ min(t)
        if m > 80_000 and len(f(m)) == 1 and str(m).count('567') == 1:
            print(i, m)

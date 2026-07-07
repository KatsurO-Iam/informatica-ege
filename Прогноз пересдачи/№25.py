def f(n):
    for i in range(2,int(n**0.5)):
        if n % i == 0:
            return [i]+f(n//i)
    return [n]

for i in range(8_007_459_809, 8_207_459_809):
    t = f(i)
    if len(t) > 1:
        t = sorted(set(t), reverse=True)
        m = t[0] + t[1]
        if m > 70_000 and len(f(m)) == 1 and str(m).count('23') == 1:
            print(i, m, set(t))
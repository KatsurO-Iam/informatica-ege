def p(n):
    for i in range(2,int(n**0.5)+1):
        if n % i == 0:
            return False
    return True

def f(n):
    s = set()
    for i in range(2,int(n**0.5)+1):
        if n % i == 0:
            s.add(i)
            s.add(n//i)
    s = list(s)
    for x in s[:]:
        if p(x) == False:
            s.remove(x)
    return sorted(list(s))

for x in range(1_104_285_718, 10**10):
    t = f(x)
    if len(t) == 0:
        continue
    else:
        if len(t) == 2:
            p1 = str(t[0]).count('16') == 1
            p2 = str(t[1]).count('16') == 1
            if p1 + p2 == 2:
                print(x, min(t))
        elif len(t) == 1:
            if t[0]*t[0] == x:
                if ('16' in str(t[0]) or '61' in str(t[0])):
                    print(x, t)

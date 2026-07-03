sp = [[int(x) for x in y.split()] for y in open('9')]
i = 0
ans = 0
for x in sp:
    i += 1
    p1 = [i for i in x if x.count(i) == 1]
    if len(set(p1)) == len(x):
        x = sorted(x)
        s1 = (min(x) + max(x)) * 2
        s2 = x[1] + x[2] + x[3]
        if s1 > s2:
            print(i , sum(x), x)

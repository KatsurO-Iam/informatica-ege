sp = [[int(x) for x in i.split()] for i in open('9')]
c = 0
for x in sp:
    c += 1
    p1 = [i for i in x if x.count(i) == 1]
    if len(set(p1)) == len(x):
        x = sorted(x)
        s1 = x[0] + x[1] + x[2]
        s2 = x[3] + x[4] + x[5]
        if s1*2 < s2:
            print(x)
            print(c)
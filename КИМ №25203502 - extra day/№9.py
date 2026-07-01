sp = [[int(x) for x in i.split()] for i in open('9')]

c = 0
for x in sp:
    p1 = [i for i in x if x.count(i) == 2]
    p2 = [i for i in x if x.count(i) == 1]
    if len(set(p1)) == 2 and len(p2) == 2:

        s1 = sum(p1)
        s2 = sum(p2)
        print(p1, p2, s1,s2)
        if s1 > s2:
            c += 1
print(c)
sp = [[int(i) for i in x.split()]for x in open('9')]
i = 0
for x in sp:
    i+=1
    p1 = [i for i in x if x.count(i) == 3]
    p2 = [i for i in x if x.count(i) == 2]
    p3 = [i for i in x if x.count(i) == 1]

    if len(set(p1)) == 1 and len(set(p2)) == 1 and len(set(p3)) == 2:
        m1 = max(max(p1), max(p2))
        m2 = max(p3)
        if m1 < m2:
            print(i)
with open('9') as f:
    sp = [[int(x) for x in y.split()] for y in f]
c = 0
for x in sp:
    p1 = [i for i in x if x.count(i) == 3]
    p2 = [i for i in x if x.count(i) == 1]

    if len(set(p1)) == 1 and len(set(p2)) == 3:
        ps = 3 * p1[0]
        arif = sum(p2) / 3
        if arif>= ps:
            c += 1
print(c)
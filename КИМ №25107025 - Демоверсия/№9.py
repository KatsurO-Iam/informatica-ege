sp = [[int(x) for x in y.split()] for y in open('9')]

for x in sp:
    p1 = [i for i in x if x.count(i) == 3]
    p2 = [i for i in x if x.count(i) == 1]
    if len(set(p1)) == 1 and len(set(p2)) == 4:
        sr = sum(p2)/4
        if sr <= p1[0]:
            print(sum(x))
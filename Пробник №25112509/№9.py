with open('9') as f:
    sp = [[int(x) for x in y.split()] for y in f]

k = 0
for x in sp:
    p1 = [i for i in x if x.count(i) == 2]
    p2 = [i for i in x if x.count(i) == 1]
    if len(p1) == 2 and len(p2) == 1:
        k += 1
print(k)
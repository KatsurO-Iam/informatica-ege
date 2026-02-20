with open('9') as f:
    sp = [[int(x) for x in y.split()] for y in f]

k = 0
for x in sp:
    p1 = [i for i in x if x.count(i) == 3]
    p2 = [i for i in x if x.count(i) == 1]
    if len(set(p1)) == 1 and len(p2) == 3:
        print(p1,p2)
        sr = sum(p2)/len(p2)
        ss = sum(p1)
        if sr <= ss:
            k += 1
print(k)
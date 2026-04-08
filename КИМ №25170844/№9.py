with open('9') as f:
    sp = [[int(x) for x in y.split()] for y in f]
k = 0
for x in sp:
    p1 = [i for i in x if x.count(i) == 2]
    p2 = [i for i in x if x.count(i) == 1]

    sr = (min(x) + max(x))/2
    if len(set(p1)) == 3 and len(set(p2)) == 1 and sr < p2[0]:
        k+=1
print(k)
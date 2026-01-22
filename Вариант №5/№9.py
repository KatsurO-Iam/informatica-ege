sp = [[int(x) for x in y.split()] for y in open('9')]
k = 0
for x in sp:
    x = sorted(x)
    ss = x[0] + x[1] + x[2]
    mm = max(x)
    p1 = [i for i in x if x.count(i) == 1]
    if len(p1) == 4 and mm < ss:
        k +=1
print(k)

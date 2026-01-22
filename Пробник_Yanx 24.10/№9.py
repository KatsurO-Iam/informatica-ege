with open('9') as f:
    sp = [[int(x) for x in y.split()] for y in f]

k = 0
for x in sp:
    p1 = [i for i in x if x.count(i) == 1]
    x = sorted(x)
    arif_mima = (x[0] + x[-1])/ 2
    arif = (x[1] + x[2])/ 2
    if len(p1) == 4 and arif_mima <= arif:
        k+=1

print(k)
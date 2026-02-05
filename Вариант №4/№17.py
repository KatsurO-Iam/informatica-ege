sp = [int(x) for x in open('17')]

minn = min([x for x in sp if abs(x) % 1000 == 250])
print(minn)
res = []
c = 0
for i in range(len(sp) - 2):
    p1 = abs(sp[i]) % 2 == 0
    p2 = abs(sp[i + 1]) % 2 == 0
    p3 = abs(sp[i + 2]) % 2 == 0
    s = sp[i] + sp[i + 1] + sp[i + 2]
    if p1 + p2 + p3 == 3 and s > minn:
        c += 1
        res.append(sp[i] + sp[i + 1] + sp[i + 2])
print(c, max(res))
#801 273218

sp = [int(x) for x in open('17')]

minn = min(sp)
res = []
c = 0
for i in range(len(sp) - 1):
    p1 = sp[i] % 30 == minn
    p2 = sp[i + 1] % 30 == minn
    if p1 + p2 >= 1:
        c += 1
        res.append(sp[i] + sp[i + 1])
print(c, min(res))
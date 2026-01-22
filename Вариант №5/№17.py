sp = [int(x) for x in open('17.txt')]

minn = min(sp)
res = []
c = 0
for i in range(len(sp) - 1):
    p1 = sp[i] % 27 == minn
    p2 = sp[i + 1] % 27 == minn
    if p1 + p2 >= 1:
        c += 1
        res.append(sp[i] + sp[i + 1])
print(c, max(res))
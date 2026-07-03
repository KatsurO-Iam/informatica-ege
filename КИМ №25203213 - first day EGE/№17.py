sp = [int(x) for x in open('17')]

minn = min([x for x in sp if x > 0 and abs(x) % 33 == 0])
res = []
for i in range(len(sp) - 1):
    p1 = sp[i] != sp[i + 1]
    p2 = abs(sp[i] - sp[i + 1]) % minn == 0
    if p1 + p2 == 2:
        res.append(sp[i] + sp[i + 1])
print(len(res), max(res))
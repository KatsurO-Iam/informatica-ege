sp = [int(x) for x in open('17')]

maxx = max([x for x in sp if abs(x) % 10 == 9 and len(str(abs(x))) == 4])
res = []
for i in range(len(sp) - 2):
    p1 = abs(sp[i]) % 10 == 9 and len(str(abs(sp[i]))) == 4
    p2 = abs(sp[i + 1]) % 10 == 9 and len(str(abs(sp[i + 1]))) == 4
    p3 = abs(sp[i + 2]) % 10 == 9 and len(str(abs(sp[i + 2]))) == 4

    s = sp[i]+sp[i+1]+sp[i+2]

    if p1 + p2 + p3 == 2 and s < maxx:
        res.append(s)

print(len(res), max(res))
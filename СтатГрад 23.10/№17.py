sp = [int(x) for x in open('17.txt')]

maxx = max([x for x in sp if x < 0 and len(str(abs(x))) == 3 and abs(x) % 6 == 0])

cnt = 0
ans = []
for i in range(len(sp) - 1):
    p1 = sp[i] < 0
    p2 = sp[i + 1] < 0

    ss = sp[i] + sp[i + 1]
    if p1 + p2 == 1 and ss > maxx:
        cnt += 1
        ans.append(sp[i]**2 + sp[i + 1]**2)

print(cnt, max(ans))
#2553 19701728317
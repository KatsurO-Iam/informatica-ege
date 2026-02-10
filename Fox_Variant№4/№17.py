sp = [int(x) for x in open('17')]
cnt = 0
for s in sp:
    if abs(s) % 10 == 5:
        cnt += 1

s = []
c = 0
for i in range(len(sp) - 1):
    p1 = sp[i] < 0
    p2 = sp[i + 1] < 0
    ss = sp[i + 1] + sp[i]
    if p1 + p2 == 1 and ss <= cnt:
        s.append(ss)
        c +=1
print(c, max(s))
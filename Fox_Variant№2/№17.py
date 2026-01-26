sp = [int(x) for x in open('17')]
minn = min([x for x in sp if abs(x) % 10 == 7])

s = []
cnt = 0
for i in range(len(sp) - 1):
    p1 = abs(sp[i]) % 10 == 7
    p2 = abs(sp[i + 1])%10 == 7
    ss = sp[i + 1] + sp[i]
    if p1 + p2 == 1 and ss**2 >= minn**2:
        s.append(ss**2)
        cnt +=1
print(cnt, max(s))
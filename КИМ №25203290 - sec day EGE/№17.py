sp = [int(x) for x in open('17')]
krat = [x for x in sp if abs(x) % 100 == 0]
print(krat)
k = 0
for x in sp:
    if abs(x) % 100 == 0:
        k +=1
print(k)

res = []
cnt = 0
for i in range(len(sp) - 1):
    p1 = sp[i] < 0
    p2 = sp[i + 1] < 0
    if p1 + p2 <= 2 and (sp[i] + sp[i + 1] < k):
        cnt+=1
        print(p1 , p2)
        res.append(sp[i] + sp[i + 1])

print(len(res), max(res))

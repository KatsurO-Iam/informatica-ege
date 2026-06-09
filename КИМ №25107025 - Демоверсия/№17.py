sp = [int(x) for x in open('17')]

minn = min([x for x in sp if len(str(x)) == 2])

res = []
cnt = 0
for i in range (len(sp) - 1):
    p1 = len(str(sp[i])) == 2
    p2 = len(str(sp[i + 1])) == 2

    if p1 + p2 == 1 and (sp[i] + sp[i+1])% minn == 0:
        cnt+=1
        res.append(sp[i] + sp[i+1])

print(cnt, max(res))
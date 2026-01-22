with open('17.txt') as f:
    sp = [int(x) for x in f]

minn = min([x for x in sp if x % 6 == 0])
cnt = 0
maxx = []
for i in range(len(sp)-1):
    p1 = sp[i] % minn == 0
    p2 = sp[i+1] % minn == 0
    if p1 and p2:
        cnt += 1
        maxx.append((sp[i] + sp[i+1]))

print(cnt, max(maxx))
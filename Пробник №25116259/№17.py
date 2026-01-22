sp = [int(x) for x in open('17.txt')]

minn = min(sp)
maxx = []
cnt = 0
for i in range(len(sp)-1):
    p1 = sp[i] % 117 == minn
    p2 = sp[i+1] % 117 == minn
    if p1 + p2 >=1:
        cnt += 1
        maxx.append(sp[i]+sp[i+1])

print(cnt, max(maxx))
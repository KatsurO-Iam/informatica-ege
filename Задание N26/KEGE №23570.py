with open('kege23570') as f:
    n,m = map(int,f.readline().split())
    power = []
    for _ in range(n):
        power.append(int(f.readline()))
    cnt = []
    for _ in range(m):
        a,b = map(int,f.readline().split())
        cnt.append((a,b))

power.sort()
cnt.sort(key=lambda x: (x[1], -x[0]))
summ = 0
poww = 0
for i in range(len(power)):
    for j in range(len(cnt)):
        if power[i] <= cnt[j][0]:
            summ += cnt[j][1]
            poww = max(poww, cnt[j][0])
            break
print(summ, poww)
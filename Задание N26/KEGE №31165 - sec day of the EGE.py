with open('26_31165.txt') as f:
    k, n = map(int, f.readline().split())
    sbor = []
    for x in range(n):
        st, en, t = f.readline().split()
        sbor.append([int(st), int(en), t])

sbor.sort()
res = [0]*(k + 1)
ans = []
for st,en, t in sbor:
    if t == 'A':
        for i in range(1, len(res), 2):
            if st >= res[i]:
                res[i] = en + 5
                ans.append(i)
                break
    if t == 'B':
        for i in range(2, len(res), 2):
            if st >= res[i]:
                res[i] = en + 5
                ans.append(i)
                break
print(len(ans), ans[-1])
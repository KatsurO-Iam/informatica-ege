with open('26') as f:
    n, m, k = map(int, f.readline().split())

    sp = []
    for _ in range(n):
        a, b = map(int, f.readline().split())

        sp.append([a, b])
vert = []
gor = []
sp = sorted(sp, key = lambda x: (-x[1], -x[0]))
# for st, en in sp:
#     gor.append(st)
#     vert.append(en)
res = []
# for i in range(len(gor)-1):
#     for j in range(len(vert)-1):
#         if gor[i] != gor[i+1]:
#             break
#

for i in range(len(sp)-1):
    if sp[i][0] != sp[i + 1][0]:
        continue
    if sp[i][0] == sp[i + 1][0]:
        if abs(sp[i][1] - sp[i + 1][1]) < 2:
            continue
        else:
            res.append((sp[i][0], max(sp[i][1], sp[i+1][1])))
print(res)

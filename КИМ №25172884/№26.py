# from functools import total_ordering
# from itertools import combinations
#
with open('26') as f:
    n, m = map(int, f.readline().split())
    sp = []
    for x in range(n):
        sp.append(int(f.readline()))
sp = sorted(sp, reverse=True)
total_waste = 0
total_weild = 0
while True:
    cabell = 0
    weild = -1
    while cabell < m and sp:
        if cabell == 0:
            val = sp.pop(0)
        else:
            need = m - cabell
            inx = -1
            for i in range(len(sp) - 1, -1, -1):
                if sp[i] >= need:
                    inx = i
                    break
            if inx != -1:
                val = sp.pop(inx)
            else:
                val = sp.pop(0)
        weild += 1
        cabell += val
    if cabell >= m:
        total_weild+=weild
        total_waste += cabell - m
        if cabell - m > 0:
            sp.append(cabell - m)
            sp.sort(reverse=True)
    else:
        break

print(total_weild, total_waste)


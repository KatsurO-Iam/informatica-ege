def g(n):
    if sum(map(int, str(n))) % 2 == 0:
        return True
    return False
with open('9') as f:
    sp = [[int(x) for x in y.split()] for y in f]
k = 0
summ = 0
for x in sp:
    k +=1
    p1 = [i for i in x if x.count(i) == 1]
    x = sorted(x)
    kv = (x[0] + x[-1])**2
    ku = x[1]**3 + x[2]**3
    if len(p1) == 4  and kv > ku:
        summ += k
print(summ)
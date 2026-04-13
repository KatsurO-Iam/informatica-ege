def g(n):
    if sum(map(int, str(n))) % 2 == 0:
        return True
    return False
with open('9') as f:
    sp = [[int(x) for x in y.split()] for y in f]
k = 0
for x in sp:
    k +=1
    p1 = [i for i in x if x.count(i) >= 2 and g(i) == True]
    if sorted(x) == x and len(p1) >= 1:
        print(k, x)

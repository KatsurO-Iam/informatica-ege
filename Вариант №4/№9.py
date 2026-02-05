sp = [[int(x) for x in y.split()] for y in open('9')]
summ = 0
k = 0
ans = []
for x in sp:
    p1 = [i for i in x if x.count(i)==2]
    p2 = [i for i in x if x.count(i) == 1]
    print(p1, p2)
    ss = sum(p2)
    if len(set(p1)) == 1 and len(p2) == 4 and p1[0] > ss:
        k+=6
        summ += sum(x)

print(summ//k)
#47
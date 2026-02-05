sp = [[int(x) for x in y.split()] for y in open('9')]
k = 0
ans = []
for x in sp:
    p1 = [i for i in x if x.count(i)==2]
    p2 = [i for i in x if x.count(i) == 1]

    s2 = sum(p2)
    s1 = sum(list(set(p1)))
    if len(set(p1)) == 2 and len(p2) == 2 and s2 <= s1:
        k+=1
        ans.append((k, sum(x)))

print(max(ans, key=lambda x: x[0]))
#331
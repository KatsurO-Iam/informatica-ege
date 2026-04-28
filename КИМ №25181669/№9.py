sp = [[int(x) for x in y.split()] for y in open('9')]
cnt = 0
for x in sp:
    p1 = [i for i in x if x.count(i) ==  4]
    p2 = [i for i in x if x.count(i) ==  2]
    p3 = [i for i in x if x.count(i) ==  1]

    if len(set(p1)) == 1 and len(set(p2)) == 1 and len(p3) == 3:
        mm = max(max(p1), max(p2))
        sr = sum(p3) / len(p3)
        if sr>=mm:
            cnt +=1
print(cnt)
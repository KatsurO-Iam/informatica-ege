sp = [[int(x) for x in i.split()] for i in open('№28930')]

c = 0
for x in sp:
    p1 = [i for i in x if x.count(i) == 1]
    if x == sorted(x) and len(p1) == 5:
        mm = x[0]+x[-1]
        ss = x[1]+x[2]+x[3]
        if mm <= ss:
            c+=1
print(c)
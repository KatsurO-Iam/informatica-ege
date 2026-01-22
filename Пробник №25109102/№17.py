sp = [int(x) for x in open('17.txt')]

minn = min([x for x in sp if abs(x) % 100 == 68])
cnt = 0
maxx = []
for i in range(len(sp) - 1):
    p1 = (abs(sp[i]) % 100 != 68 and abs(sp[i+1]) % 100 == 68) or (abs(sp[i]) % 100 == 68 and abs(sp[i+1]) % 100 != 68)
    p2 = sp[i]**2 + sp[i+1]**2 >= minn**2
    if p1 and p2:
        cnt +=1
        maxx. append(sp[i]**2 + sp[i+1]**2)
print(cnt, max(maxx))
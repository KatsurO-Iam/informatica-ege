maxx = []
for i in range(1000):
    r = bin(2 + i)[2:]
    ss = r.count('1')
    r += str(ss%2)
    ss1 = r.count('1')
    r += str(ss1%2)
    if int(r,2) < 61:
        maxx.append(i)

print(max(maxx))

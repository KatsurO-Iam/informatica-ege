with open('9') as f:
    sp = [[int(x) for x in y.split()] for y in f]

k = 0
for x in sp:
    x = sorted(x)
    mm = (max(x) + min(x))**3
    ss = x[1]**3 + x[2]**3 + x[3]**3
    if mm > ss:
        k += 1
print(k)
sp = [[int(x) for x in y.split()] for y in open('9')]

k = 0
for x in sp:
    p1 = [i for i in x if i % 10 == 5]
    x = sorted(x, reverse=True)
    mm = (x[0] + x[1]) * 2
    ss = (x[2] + x[3] + x[4]) * 3

    if len(p1) >= 2 and mm > ss:
        print(p1, mm, ss)
        k += 1
print(k)
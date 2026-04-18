base = 67
max_x = -1
res = []
for x in range(66, -1, -1):
    for y in range(x, -1, -1):
        num1 = (7 * (base ** 4) +
                3 * (base ** 3) +
                x * (base ** 2) +
                1 * (base ** 1) +
                y * (base ** 0))
        num2 = (4 * (x ** 3) +
                9 * (x ** 2) +
                y * (x ** 1) +
                6 * (x ** 0))
        t = num1 + num2
        res.append(t)
print(len(res))
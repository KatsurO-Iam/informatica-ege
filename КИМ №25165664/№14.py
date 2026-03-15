base = 37
max_x = -1
res = 0
for x in range(36, -1, -1):
    num1 = (9 * (base ** 4) +
            8 * (base ** 3) +
            x * (base ** 2) +
            3 * (base ** 1) +
            1 * (base ** 0))
    num2 = (1 * (base ** 4) +
            x * (base ** 3) +
            9 * (base ** 2) +
            2 * (base ** 1) +
            4 * (base ** 0))
    t = num1 + num2
    if t % 21 == 0:
        max_x = x
        res = t // 21
        break
print(res)
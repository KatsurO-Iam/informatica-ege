def f(s,e):
    if s > e:
        return 0
    if s == e:
        return 1
    ways = f(s + 1, e)

    tens = (s // 10) % 10
    units = s % 10

    if tens < units:
        neww = (s// 100)*100 + units * 10 + tens

        ways += f(neww, e)
    return ways

print(f(101, 123) * f(123, 146))
def f(start, end):
    if start < end or start == 7:
        return 0
    elif start == end:
        return 1
    else:
        return f(start - 1, end) + f(start - 4, end) + f(start // 2, end)

print(f(25, 10)*f(10,3))
#546
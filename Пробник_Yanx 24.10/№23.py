def f(start, end):
    if start > end or start == 35:
        return 0
    elif start == end:
        return 1
    else:
        return f(start + 1, end) + f(start + 2, end) + f(start + 4, end)

print(f(24, 33)*f(33,42))

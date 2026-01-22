def f(start, end):
    if start < end:
        return 0
    elif start == end:
        return 1
    else:
        return f(start - 2, end) + f(start//2, end)

print(f(50, 11)*f(11,2))

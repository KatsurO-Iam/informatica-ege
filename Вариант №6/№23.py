def f(start, end):
    if start < end:
        return 0
    elif start == end:
        return 1
    else:
        return f(start - 2, end) + f(start//2, end)

print(f(52, 14)*f(14,2))

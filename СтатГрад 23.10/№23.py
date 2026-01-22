
def f(start, end, h):
    if start > end:
        return 0
    elif start == end:
        return h
    elif start == 14 or start == 18:
        h = True
    return f(start + 1, end, h) + f(start * 2, end,h) + f(start * 3, end,h)

print(f(6, 48, False))
# 69
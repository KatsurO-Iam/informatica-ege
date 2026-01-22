def f(start, end, comm):
    if end == 24:
        return {start}
    elif comm == 0:
        return f(start + 1, end+1, 1) | f(start + 7, end + 1, 7) | f(start * 4, end + 1, 4)
    elif comm == 1:
        return f(start + 7, end + 1, 7) | f(start * 4, end + 1, 4)
    elif comm == 7:
        return f(start + 1, end + 1, 1) | f(start * 4, end + 1, 4)
    elif comm == 4:
        return f(start + 1, end + 1, 1) | f(start + 7, end + 1, 7)

print(len(f(1,0,0)))
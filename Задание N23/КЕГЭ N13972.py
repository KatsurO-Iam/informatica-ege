def f(start, end, comm):
    if start > end:
        return 0
    elif start == end and (comm[0] == 'A' or comm[0] == 'C'):
        return 1
    else:
        return f(start + 2, end,comm + 'A') + f(start + 5, end, comm + 'B') + f(start*2, end, comm + 'C')

def x(start, end, comm):
    if start > end:
        return 0
    elif start == end:
        return 1
    else:
        return x(start + 2, end,comm + 'A') + x(start + 5, end, comm + 'B') + x(start*2, end, comm + 'C')

print(f(7, 23, '')* x(23,35, ''))
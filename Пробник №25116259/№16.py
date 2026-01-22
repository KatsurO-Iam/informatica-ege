def f(n):
    if n == 1:
        return 1
    elif n % 2 == 0 and n > 1:
        return (2 * n + f(n-1))
    else:
        return (4*n + 2*f(n-2))

print(f(12))
def f(s, e, k):
    if s % 2 == 0:
        k = k + 1
    if s>e or k > 6:
        return 0
    if s == e:
        return 1 if k == 6 else 0

    return (f(s + 1, e, k) + f(s + 3, e, k) + f(s + 5, e, k))

print(f(3, 25, 0))
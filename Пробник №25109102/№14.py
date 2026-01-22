for N in range(5, 50):
    try:
        left = int("4646", N) + int("387", N + 2)
        right = int("3746", N + 1)
        if left == right:
            print(N)
    except ValueError:
        continue

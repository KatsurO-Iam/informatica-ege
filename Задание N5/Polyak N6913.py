def f(n):
    oct_str = oct(n)[2:]
    new_str = ''.join(['2' if int(c) % 2 == 1 else c for c in oct_str])
    remainder = n % 8
    new_str += str(remainder)
    return int(new_str, 8)

summ = 0
for N in range(10000, 100000):
    r1 = f(N)
    r = f(r1)
    if r % 2023 == 0:
        summ += N

print(summ)
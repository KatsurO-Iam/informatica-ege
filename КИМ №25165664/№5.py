k = 0
for n in range(1, 5000):
    r = 0
    if n % 3 == 0:
        r = n / 3
    else:
        r = n - 1
    a = 0
    if r % 5 == 0:
        a = r / 5
    else:
        a = r - 1
    b = 0
    if a % 11 == 0:
        b = a / 11
    else:
        b = a - 1
    if b == 8:
        k +=1
print(k)

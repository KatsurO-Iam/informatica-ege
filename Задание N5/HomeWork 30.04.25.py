def is_prime(number):
    for i in range(2, int(number ** 0.5) + 1):
        if number % i == 0:
            return False
    return True

for N in range(100_000,1_000_000):
    r = str(N)
    K = 0
    L = 0
    #if '22' not in r and '33' not in r and '44' not in r and '55' not in r and '66' not in r and '77' not in r and '88' not in r and '99' not in r and '00' not in r:
    for d in range(0, 6, 2):
        K += int(r[d])
    for d in range(0, 6):
        if is_prime(int(r[d])):
            L += int(r[d])
    R = abs(K-L)
    if R == 407:
        print(N)
        break



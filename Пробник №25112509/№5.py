
for n in range(100000, 10**7):
    s = str(n)
    k = str(int(s[0]) + int(s[1])) + str(int(s[2]) + int(s[3])) + str(int(s[4]) + int(s[5]))
    r = int(k)
    R = bin(r)[2:]
    if n % 2 == 0:
        R = R + '0'
    elif n % 2 != 0:
        R = R + '1'
    otv = int(R)
    if str(otv)[-2] == '9.txt' and str(otv).count('2') == 1 and otv == 1519:
        print(n)
        break
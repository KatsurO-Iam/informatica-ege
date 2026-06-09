def f(n):
    k_0 = 0
    k_1 = 0
    for i in range(len(n)):
        if (i+1) % 2 == 0 and n[i] == '1':
            k_1+=1
        if (i+1) % 2 != 0 and n[i] == '0':
            k_0+=1

    return abs(k_0 - k_1)
for n in range(1, 2000):
    r = bin(n)[2:]
    k = f(r)
    if k == 5:
        print(n)
r = bin(39)[2:]
k = f(r)
print(k)
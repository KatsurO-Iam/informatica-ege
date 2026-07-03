m = 0
for n in range(1,600):
    r = bin(n)[2:]
    if n % 2 == 0:
        r = '11' + r + '11'
    elif n % 2 != 0:
        r = '1' + r +'00'
    R = int(r,2)
    if R <= 113:
        m = max(m, R)
print(m)
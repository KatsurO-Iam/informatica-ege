
for n in range(1, 1000):
    r = bin(n)[2:]
    if n % 2 == 0:
        r = r.replace('0', '1')
    if n % 2 != 0:
        inx = r.find('1')
        r = '1' + r[inx+1:].replace('1', '00')
    R = int(r, 2)
    if R <= 600:
        print(n, R)
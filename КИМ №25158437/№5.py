for n in range(1, 1000):
    r = bin(n)[2:]
    if r.count('1') % 2 == 0:
        r = r + '1'
    elif r.count('1') % 2 != 0:
        r = r + '0'
    if int(r,2) % 2 ==0:
        r = r + '10'
    elif int(r,2) % 2 != 0:
        r = r + '01'
    if int(r,2) < 1000:
          print(int(r,2))
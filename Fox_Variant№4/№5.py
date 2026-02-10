s = []
for n in range(19):
    r = bin(n)[2:]
    if n %2 != 0:
        r = r + '01'
    elif n % 2 == 0:
        r = '11'+ r[:-2]+ '10'
    R = int(r,2)

    s.append(R)
print(max(s))
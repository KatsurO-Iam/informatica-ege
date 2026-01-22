for i in range(1,10000):
    s = '5' + '2'*i
    while '52' in s or '2222' in s or '1112' in s:
        if '52' in s:
            s = s.replace('52', '11', 1)
            s = s.replace('2222', '5', 1)
        else:
            s = s.replace('1112', '2', 1)

    summ = sum([int(x) for x in s])
    if summ == 1685:
        print(i)



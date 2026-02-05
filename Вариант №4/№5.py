for k in range(1000,9999):
    s = sum(map(int,str(k)))
    m = max(map(int,str(k)))
    n = min(map(int,str(k)))
    p1 = s - m
    p2 = s - n
    l = ''
    if p1 > p2:
        l = str(p1)+str(p2)
    else:
        l = str(p2)+str(p1)
    if int(l) == 2013:
        print(k)
#1488
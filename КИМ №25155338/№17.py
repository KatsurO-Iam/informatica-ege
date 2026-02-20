sp = [int(x) for x in open('17')]

maxx_chet = max([x for x in sp if x % 2 == 0])
maxx_nechet = max([x for x in sp if x % 2 != 0])

if maxx_chet > maxx_nechet:
    k = 0
    for x in sp:
        if x % 2 == 0:
          k+=1
    min_chet = min([x for x in sp if x % 2 == 0])
    print(k, min_chet)
else:
    k = 0
    for x in sp:
        if x % 2 != 0:
            k += 1
    min_nechet = min([x for x in sp if x % 2 != 0])
    print(k, min_nechet)
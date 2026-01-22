print('w x y z')
k = 0
for w in 0,1:
    for x in 0,1:
        for y in 0,1:
            for z in 0,1:
                if ((y <= x) and (not z) and w) == 1:
                    print(w,x, y,z)
                    k+=1
                if k == 3:
                    exit()


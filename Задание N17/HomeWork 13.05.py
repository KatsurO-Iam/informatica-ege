sp = [int(x) for x in open('13.05.txt')]
cnt = 0
minn = []
for i in range(2, len(sp) - 3):
    sum1 = sp[i - 1] + sp[i - 2]
    summ = sp[i] + sp[i+1]
    sum2 = sp[i+2] + sp[i + 3]

    p1 = summ > sum1 and summ > sum2
    if ((p1 == True) and (summ > 0) and (sum1 > 0) and (sum2 > 0)):
        cnt +=1
        minn.append(sp[i] * sp[i+1])

print(cnt, min(minn))
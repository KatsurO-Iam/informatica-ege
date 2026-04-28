sp = [int(x) for x in open('17')]

minn = min([x for x in sp if len(str(x)) == 3 and x% 100 == 11])
cnt = 0
ss = []
for i in range(len(sp) - 1):
    p1 = len(str(sp[i])) != 3
    p2 = len(str(sp[i + 1])) != 3

    q1 = abs(sp[i] - sp[i + 1]) % minn == 0
    if p1 + p2 == 1 and q1 == True:
        cnt +=1
        ss.append(sp[i]+sp[i+1])

print(cnt, max(ss))
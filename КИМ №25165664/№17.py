sp = [int(x) for x in open('17')]

mm = []
cnt = 0
for i in range(len(sp) - 2):
    p1 = str(sp[i])[0] == str(sp[i])[-1]
    p2 = str(sp[i + 1])[0] == str(sp[i + 1])[-1]
    p3 = str(sp[i + 2])[0] == str(sp[i + 2])[-1]

    q1 = len(str(sp[i])) == 4 and str(sp[i])[1] == '2'
    q2 = len(str(sp[i + 1])) == 4 and str(sp[i + 1])[1] == '2'
    q3 = len(str(sp[i + 2])) == 4 and str(sp[i + 2])[1] == '2'

    if p1 + p2 + p3 == 1 and q1 + q2 + q3 == 2:
        print(sp[i], sp[i + 1], sp[i + 2])
        cnt += 1
        mm.append(max(sp[i], sp[i + 1], sp[i + 2]))
print(cnt, sum(mm))
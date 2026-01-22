sp = [int(x) for x in open('17 (3).txt')]

maxx = max([x for x in sp if abs(x) % 100 == 42 and len(str(abs(x))) == 4])
cnt = 0
ans = []
for i in range(len(sp) - 2):
    p1 = abs(sp[i]) % 100 == 42 and len(str(abs(sp[i]))) == 4
    p2 = abs(sp[i + 1]) % 100 == 42 and len(str(abs(sp[i + 1]))) == 4
    p3 = abs(sp[i + 2]) % 100 == 42 and len(str(abs(sp[i + 2]))) == 4

    ss = sp[i]+sp[i+1]+sp[i+2]

    if p1 + p2 + p3>=2 and ss > maxx:
        cnt +=1
        ans.append(ss)

print(cnt, max(ans))

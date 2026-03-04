sp = [int(x) for x in open('17')]

mm = []
cnt = 0
for i in range(len(sp) - 1):
    p1 = abs(sp[i]) + abs(sp[i+1]) > 17043
    p2 = (abs(sp[i]) + abs(sp[i+1]))%3==0
    if p1 + p2 == 2:
        cnt += 1
        mm.append(sp[i]+sp[i+1])
print(cnt, min(mm))
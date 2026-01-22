with open('9') as f:
    sp = [[int(x) for x in y.split()] for y in f]
cnt = 0
for x in sp:
    p1 = [n for n in x if x.count(n) == 1]
    p2 = [n for n in x if x.count(n) > 1]
    if min(x) in p2 and 2 <= len(p2) <= 3 :
        minn = min(p1)
        maxx = max(p1)
        ss = minn**2 + maxx**2
        if ss <= ((sum(p1) - maxx - minn)**2):
            cnt +=1

print(cnt)
#752
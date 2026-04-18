sp = [int(x) for x in open('17')]

def f(n):
    s = str(n)
    return len(s) == 3 and len(set(s)) == 3
minn = min([x for x in sp if f(x)])
sp_1 = sp[:2500]
sp_2 = sp[2500:]
sp_2 = sp_2[::-1]
cnt = 0
ss = []
for i in range(0,2500):
    if (sp_1[i]*sp_2[i]) % minn == 0:
        cnt+=1
        ss.append(sp_1[i]+sp_2[i])
print(cnt, min(ss))
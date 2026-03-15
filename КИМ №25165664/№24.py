from re import*
with open('24') as f:
    sp = f.readline()
ans = ''
mm = []
s = sp[0]
for i in range(1,len(sp)-1):
    if sp[i+1] > sp[i]:
        s +=sp[i+1]
    else:
        mm.append((len(s), s))
        s = ''
print(max(mm))
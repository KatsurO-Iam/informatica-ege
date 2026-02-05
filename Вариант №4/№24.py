with open('24') as f:
    sp = f.readline()
maxx = 0
k = ''
sp = sp.split('2')
for i in range(len(sp) - 301):
    s = '2'.join(sp[i:i+301])
    if s.count('DOG') == 3:
        inx = s.rfind('DOG')
        maxx = max(maxx, len(s[:inx]))

print(maxx + 3)
#11487
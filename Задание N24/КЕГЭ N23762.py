with open('24_23762.txt') as f:
    sp = f.readline()

sp = sp.replace('2025', '*')
sp = sp.split('Y')
maxx = 0
for i in range(len(sp) - 81):
    s = 'Y'.join(sp[i:i+81])
    if s.count('*') >= 90:
        s = s.replace('*', '2025')
        maxx = max(maxx, len(s))

print(maxx)
with open('24') as f:
    sp = f.readline()
maxx = 0
k = ''
sp = sp.split('F')
for i in range(len(sp) - 77):
    s = 'F'.join(sp[i:i+77])
    s = s.replace('0', '*')
    s = s.replace('2', '*')
    s = s.replace('4', '*')
    s = s.replace('6', '*')
    s = s.replace('8', '*')
    if s.count('*') == 1:
        inx = s.find('*')
        if s[inx:].count('F') == 76:
            maxx = max(maxx, len(s[inx:]))
            k = s[inx:]

print(maxx, k.count('F'), k)
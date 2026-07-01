from re import*
s = open('24_31230.txt').readline()
s = s.replace('ABC','#')[::-1]
s = s.split('#')
m = float('inf')
a = ''
for i in range(len(s) - 110):
    x = '#'.join(s[i:i+111])
    if x.count('#') != 110:
        continue
    if x.count('#') == 110:
        if x[0] != '#':
            inx = x.find('#')
            x = x[inx:]
        if x[-1] != '#':
            inx = x.rfind('#')
            x = x[:inx + 1]
        if x.count('#') == 110:
            if m > len(x):
                m = min(m, len(x.replace('#', 'CBA')))
                a = x.replace('#', 'CBA')
print(m,a)
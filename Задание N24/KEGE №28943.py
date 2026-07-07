s = open('24_28943.txt').readline()
s = s.replace('20', '#')
for x in 'AEIOUY':
    s = s.replace(x, '*')
s = s.split('#')
m = float('inf')
for i in range(len(s) - 26):
    x = '#'.join(s[i:i+27])
    if x.count('#') == 26 and x.count('*') == 1:
        if x[0] != "#":
            inx = x.find("#")
            x = x[inx:]
        if x[-1] != '*':
            inx = x.find("*")
            x = x[:inx + 1]
        if x.count('#') == 26 and x.count('*') == 1:
            m = min(m ,len(x.replace('#', '20')))
print(m)
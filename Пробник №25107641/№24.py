from email.policy import default
from re import*

with open('24 (3).txt') as f:
    sp = f.readline()
print(sp)
sp = sp.replace('NPYNYN', '@')
sp = sp.replace('NYNNPY', '@')
sp = sp.replace('HPY', '0')
sp = sp.replace('NYN', '1')

reg = r'(?:[01@])+'
s = findall(reg, sp)
ans = max(len(x) for x in s)
print(ans)


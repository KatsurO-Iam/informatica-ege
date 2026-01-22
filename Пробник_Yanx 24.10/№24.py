
from re import*
with open("24 (10).txt") as f:
    sp = f.readline()

pattern = '(SQRP)+'
max_len = 0
for x in finditer(pattern, sp):
    print(x.group())

from re import*
with open("24.txt") as f:
    sp = f.readline()

reg = compile(r"(?:[1-4][0-4]+(?:[-+][1-4]+)+)")
max_len = 0
for x in reg.finditer(sp):
    if max_len < len(x.group()):
        max_len = len(x.group())
print(max_len)
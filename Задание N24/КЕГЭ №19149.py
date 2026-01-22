import re
from re import*
with open('24_19149.txt') as f:
    sp = f.readline()

reg = compile(
    r"\("
    r"(?:[1-4]+(?:\+[1-4]+)*)"
    r"\)"
)
maxx = 0
for x in reg.finditer(sp):
    if eval(x.group()) % 2 == 0:
        if maxx < len(x.group()):
            maxx = len(x.group())
print(maxx)


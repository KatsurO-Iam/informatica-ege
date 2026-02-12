import re
from re import*
with open("24") as f:
    sp = f.readline()


reg = re.compile('(?:[+-][5678][05678]*|(?:0|[5678][05678]*))(?:[+-](?:0|[5-8][05678]*))*')
maxx = 0
s = ''
for x in reg.finditer(sp):
    if eval(x.group()):
        if maxx < len(x.group()):
            maxx = max(maxx, len(x.group()))
            s = x.group()
print(maxx, s)

# num = r"(?:0|[1-4][0-4]*)"
# start = rf"(?:[+-][1-4][0-4]*|{num})"
# tail = rf"(?:[+-]{num})*"
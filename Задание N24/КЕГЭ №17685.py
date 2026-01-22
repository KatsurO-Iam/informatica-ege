from re import*
with open('24_17685.txt') as f:
    sp = f.readline()

reg = compile(r"(?:[1-9.txt]+(?:[*+][0-9.txt]+)+)")
maxx = 0
s = ''
for x in reg.finditer(sp):
    if eval(x.group()) == 0:
        if maxx < len(x.group()):
            maxx = max(maxx, len(x.group()))
            s = x.group()
print(maxx, s)
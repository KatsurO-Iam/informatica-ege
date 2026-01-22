from re import*
with open('24(4).txt') as f:
    sp = f.readline()

reg = compile(r'[1-9.txt][0-9.txt]*[13579]')
mmm = 0
for i in reg.finditer(sp):
    i = i[0]
    if int(i) > mmm:
        mmm = int(i)
print(mmm)

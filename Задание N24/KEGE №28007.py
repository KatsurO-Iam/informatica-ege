from re import *

st = open('24_28007.txt').readline()
pat = compile(r'(?=((\([1-9][0-9]*[98764321][+-][1-9][0-9]*[05]\))+))')
s = '(((56+-+00(0678-89)(7182-15)(3222+745))'
for i in pat.finditer(s):
    print(i[1])

mm = [x[1] for x in pat.finditer(st)]
print(max(mm, key=len))

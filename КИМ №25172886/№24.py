from re import*

line = open('24.txt').readline()
reg = compile(r'(XYZ){3,}')
for x in reg.finditer(line):
    print(x.group())
s = 'XYZXYZXYZXYZXYZ'
print(len(s))
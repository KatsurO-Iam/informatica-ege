from re import*

line = open('KEGE_KIM №25138308.txt').readline()
for x in 'AEU':
    line = line.replace(x,'*')

for x in 'BCDF':
    line = line.replace(x,'#')


pat = compile(r'(#\*#)+')
m = 0
s = ''
for i in pat.finditer(line):
    if m < len(i.group()):
        s = i.group()
        m = max(m,len(i.group()))
print(m//3, s)
print(line)
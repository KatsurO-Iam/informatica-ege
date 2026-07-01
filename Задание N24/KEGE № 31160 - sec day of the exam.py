s = open('24-secday.txt').readline()
alph = dict()
for x in open('secday'):
    d,r = x.split()
    alph[int(d)] = r
m = 0
for i in range(1,4000):
    if alph[i] in s:
        if len(alph[i]) == 13:
            print(i , alph[i])
        m = max(m,len(alph[i]))
print(m)
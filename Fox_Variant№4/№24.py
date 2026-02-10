# 1. Читаем файл
with open('24') as f:
    s = f.readline()

s = s.replace('A', '@')
s = s.replace('E', '@')
s = s.replace('O', '@')

s = s.replace('B', '#')
s = s.replace('C', '#')
s = s.replace('D', '#')

s = s.replace('@#', '*')
s = s.replace('#', '$')
s = s.replace('@', '$')
s = s.split('$')
m = -float('inf')
for i in range(len(s)):
    if s[i] != '':
        m = max(m, len(s[i]))
print(m)

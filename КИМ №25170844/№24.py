s = open('24').readline()
k = 0
f = '0123456789ABCDEF'
m = float('inf')
for i in range(0,len(s)):
    if s[i] == '0':
        k = 1
        for j in range(i + 1,len(s)):
            if s[j] == f[k]:
                k += 1
                if k == 16:
                    m = min(m ,j - i + 1)
                    break
print(m)
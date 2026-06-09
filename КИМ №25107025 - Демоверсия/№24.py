s = open('24.txt').readline()

ans = 0
s = s.split('Y')
for i in range(1,len(s) - 80):
    x = 'Y'.join(s[i:i+81])
    if x.count('Y') == 80 and x.count('2025') >= 90:
        ans = max(ans,len(x))
print(ans)
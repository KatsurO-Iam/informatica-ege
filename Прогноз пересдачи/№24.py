from re import*
s = open('24.txt').readline()

def f(s):
    alph = {
        'M':1000,
        'CM': 900,
        'D':500,
        'CD':400,
        'C':100,
        'XC':90,
        'L':50,
        'XL':40,
        'X':10,
        'IX':9,
        'V':5,
        'IV':4,
        'I':1
    }
    ans = 0
    i = 0
    while i < len(s):
        if (i < len(s) - 1) and ((s[i] + s[i + 1]) in alph):
            ans += alph[s[i] + s[i + 1]]
            i +=2
        else:
            ans += alph[s[i]]
            i +=1
    return ans

pat = compile('(?=[MDCLXVI])(M{,3}(CM|CD|D?C{,3})(XC|XL|L?X{,3})(IX|IV|V?I{,3}))')
a = ''
m = 0
res = []
for x in pat.finditer(s):
    if len(x.group()) >= m:
        m = len(x.group())
        res.append((f(x.group()), x.group()))

for x, i in sorted(res):
    if x % 2 == 0:
        print(x, i)

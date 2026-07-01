from re import*

s = open('24-secday.txt').readline()
# alph = dict()
# for x in open('24_secday'):
#     d,r = x.split()
#     alph[int(d)] = r
# m = 0
# for i in range(1,4000):
#     if alph[i] in s:
#         if len(alph[i]) == 13:
#             print(i , alph[i])
#         m = max(m,len(alph[i]))
# print(m)

def f(s):
    alph = {
        'M':1000,
        'CM':900,
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
    i = 0
    ans = 0
    while i < len(s):
        if (i < len(s) -1) and ((s[i] + s[i + 1]) in alph):
            ans +=alph[s[i] + s[i+1]]
            i +=2
        else:
            ans+=alph[s[i]]
            i+=1
    return ans
pat = compile('(?=[MDCLXVI])(M{0,3}(CM|CD|D?C{0,3})(XC|XL|L?X{0,3})(IX|IV|V?I{0,3}))')
m = 0
res = ''
for x in pat.finditer(s):
    if len(x.group()) > m:
        m = len(x.group())
        res = x.group()
    elif m == len(x.group()):
        if f(res) > f(x.group()):
            res = x.group()
print(f(res))
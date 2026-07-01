from re import*

def f(s):
    aplh = {
        "M": 1000,
        "CM": 900,
        "D": 500,
        "CD": 400,
        "C": 100,
        "XC": 90,
        "L": 50,
        "XL": 40,
        "X": 10,
        "IX": 9,
        "V": 5,
        "IV": 4,
        "I":1
    }
    ans = 0
    i = 0
    while i < len(s):
        if (i < len(s) - 1) and (s[i] + s[i+1]) in aplh:
            ans += aplh[s[i] + s[i + 1]]
            i +=2
        else:
            ans +=aplh[s[i]]
            i +=1
    return ans

def main():
    s = open('24_31160.txt').readline()
    reg = compile('(?=[MDCLXVI])(M{0,3}(CM|CD|D?C{0,3})(XC|XL|L?X{0,3})(IX|IV|V?I{0,3}))')
    ans = ''
    t = 0
    for i in reg.finditer(s):
        k = i.group()
        if len(k) > t:
            ans = k
            t = len(k)
        elif len(k) == t:
            if f(ans) > f(k):
                ans = k
    print(f(ans))

main()

#II вариант решения через Exele
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
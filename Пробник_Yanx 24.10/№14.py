from  string import ascii_lowercase, digits
def f(n):
    s = ''
    while n > 0:
        s += str(n % 9)
        n = n // 9
    return s[::-1]

maxx = -float('inf')
for x in range(1,1950):
    k = 72020 + 7400 - x
    r = f(k)
    if r.count('0') > maxx:
        maxx = max(r.count('0'), maxx)
print(maxx)
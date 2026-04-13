def f(sub):
    tag = 'DANOV'
    dif = 0
    for j in range(5):
        if sub[j] != tag[j]:
            dif+=1
    return dif == 1

s = open('24').readline()
print(s[-4:])
k = 0
n_words = [0]*len(s)
for i in range(len(s) - 4):
    if f(s[i:i+5]):
        for j in range(i, i+5):
            n_words[j] = 1
ans = 0
for x in n_words:
    if x == 0:
        k +=1
        ans = max(ans, k)
    else:
        k = 0
print(ans)
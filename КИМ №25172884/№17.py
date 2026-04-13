sp = [int(x) for x in open('17')]

def div(n):
    s = set()
    for i in range(1, int(n**0.5)+1):
        if n % i == 0:
            s.add(i)
            s.add(n // i)
    return s

maxx = 0
maxx_div = []
for i in range(len(sp)):
    t = div(sp[i])
    if len(t) > len(maxx_div):
        maxx = sp[i]
        maxx_div = t
print(maxx)
cnt = 0
mm = []
for i in range(len(sp) - 1):
    p1 = len(list(set(div(sp[i])) & set(maxx_div)))>=3
    p2 = len(list(set(div(sp[i + 1])) & set(maxx_div)))>=3

    if p1 + p2 == 2:
        cnt += 1
        mm.append(len(list(set(div(sp[i])) & set(div(sp[i+1])))))
print(cnt, max(mm))

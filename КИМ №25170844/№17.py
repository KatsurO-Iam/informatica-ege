sp = [int(x) for x in open('17')]

mm = []
cnt = 0
def f(n):
    return n > 0 and n % 10 == 9
for i in range(len(sp) - 2):

    if f(sp[i]) == False and f(sp[i+1]) == True and f(sp[i+2]) == False:
        cnt += 1
        mm.append(sum(sp[i:i + 3]))
print(cnt, max(mm))
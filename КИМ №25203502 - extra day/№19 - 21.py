def f(a,b,h,ph):
    if a + b <= 53:
        return h % 2 == ph % 2
    if h == ph:
        return 0
    comb = [f(a-3, b,h + 1, ph), f(a,b - 3, h + 1,ph),
           f(int(a/3),b,h+1,ph), f(a,int(b/3),h+1,ph)]
    return any(comb) if (h + 1)%2 == ph % 2 else any(comb)

for x in range(35,1000): #неудачный
    if f(19,x,0,2):
        print(x)

print(f(19,38,0,1))
# for x in range(35, 1000):
#     if not f(19,x,0,1) and f(19,x,0,3):
#         print(x)
#
# for x in range(35, 1000):
#     if not f(19,x,0,2) and f(19,x,0,4):
#         print(x)
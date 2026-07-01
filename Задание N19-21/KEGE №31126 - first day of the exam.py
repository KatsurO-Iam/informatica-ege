def f(a,b,h,ph):
    if a + b >= 155:
        return h%2 == ph%2
    if h == ph:
        return 0
    comb = [f(a + 1, b, h + 1, ph), f(a,b+1, h +1 ,ph), f(a * 3, b, h + 1, ph), f(a, b*3,h +1, ph)]
    return any(comb) if (h +1)%2 == ph %2 else all(comb)

# for x in range(1, 139):
#     if f(15, x, 0,2):
#         print(x) # 16 - неудачный ход
#         break

# for x in range(1,139):
#     if not f(15, x, 0, 1) and f(15, x,0,3):
#         print(x) # 19 46

for x in range(1,139):
    if not f(15, x,0,2) and f(15,x,0,4):
        print(x) # 45
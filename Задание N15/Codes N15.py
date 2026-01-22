# b = range(50,71)
#
# for a in range(1,100):
#     f = 1
#     for x in range(1,100):
#         for y in range(1,100):
#             f *= ((2*x + y != 150) or (x not in b) or (a > y))
#     if f:
#         print(a)
#         break


b = range(132, 151)
for a in range(2, 1000):
    f = 1
    for x in range(1, 1000):
        f *= (((x % a != 0) and (x in b)) <= (x % 13 != 0))
    if f:
        print(a)
        break
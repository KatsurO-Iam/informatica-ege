# maxx = 0
# minn = float('inf')
# with open ('27-A_23.txt') as f:
#
#     n = int(f.readline())
#     for x in f:
#         a, b = map(int, x.split())
#         maxx += max(a, b)
#         if abs(a-b)%3 != 0:
#             minn = min(minn, abs(a-b))
#
# if maxx % 3 ==0:
#     print(maxx - minn)
# else:
#     print(maxx)

maxx = 0
minn = float('inf')
with open('Поляков N2662 A.txt') as f:
    n = int(f.readline())
    for x in f:
        a,b = map(int, x.split())
        maxx += max(a,b)
        if abs(a-b)%3 != 0:
            minn = min(minn, abs(a-b))
if maxx%3==0:
    print(maxx)
else:
    print(maxx - minn)


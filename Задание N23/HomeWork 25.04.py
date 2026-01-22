# def f(st, en):
#     if st > en:
#         return 0
#     elif st == en:
#         return 1
#     else:
#         return f(st + 1, en) + f(st*2, en)
#
# print(f(1,30))  - N1

# def f(st, en):
#     if st < en:
#         return 0
#     elif st == en:
#         return 1
#     else:
#         return f(st - 2, en) + f(st//2,en)
#
# print(f(31, 2)) - N2

# def f(st, en):
#     if st > en:
#         return 0
#     elif st == en:
#         return 1
#     return f(st + 1, en) + f(st * 2, en)
#
# print(f(3,6)*f(6,12)*f(12,16)) - N3

def f(st, en):
    if st > en or st == 50:
        return 0
    elif st == en:
        return 1
    return f(st + 3, en) + f(st * 2 + 1, en) + f(st*3, en)

print(f(5,23) * f(23,89))

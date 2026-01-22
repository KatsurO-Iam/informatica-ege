# def f(s,e):
#     if s < e or s == 12:
#         return 0
#     if s == e:
#         return 1
#     return f(s - 3, e) + f(s//2, e)
#
# print(f(80,23)*f(23,3))

# def f(s,e):
#     if s > e or s == 33:
#         return 0
#     if s == e:
#         return 1
#     return f(s + 1, e) + f(s * 2,e) + f(s*s, e)
#
# print(f(8,32) * f(32,115))

def f(s,e,c):
    if c != 4:
        if s > e:
            return 0
        elif s == e:
            return 1
        return (f(s + 2, e, c) + f(s * 3,e,c))
        c += 1



# cnt = 0
# for end in range(1,100,2):
#     k = f(1,end,0)
#     if k != 0:
#         cnt +=1
# print(cnt)
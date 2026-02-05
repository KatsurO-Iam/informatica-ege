sp = [[int(x) for x in i.split()] for i in open('9_2702_Рогов')]
total_sum = 0

# for x in sp:
#     x.sort()
#     a, b, c = x
#     d_candidate = 0
#
#     if a == b:
#         d_candidate = c
#         L, W = a, c
#     elif b == c:
#         d_candidate = a
#         L, W = b, a
#     else:
#         continue
#
#     if L * W <= 5 * (2 * (L + W)):
#         total_sum += d_candidate
#
# print(total_sum)

for x in sp:
    p1 = [i for i in x if x.count(i) == 2]
    p2 = [i for i in x if x.count(i) == 1]
    if len(p1) == 2 and len(p2) == 1:
        # if p2[0] == 21:
            print(p1, p2)
            area = p1[0]*p2[0]
            per = p1[0] * 2 + p2[0] * 2
            print(area, per)
            if area <= 5 * per:
                total_sum += p2[0]

print(total_sum)
# from math import *
#
# def f(klast):
#     centroid, summ1 = None, float('inf')
#     for star in range(len(klast)):
#         summ = 0
#         for next_star in range(len(klast)):
#             if star == next_star:
#                 continue
#             x1, y1, h1 = klast[star]
#             x2, y2, h2 = klast[next_star]
#             summ += sqrt((x2-x1)**2 + (y2 - y1)**2) * h2
#         if summ < summ1:
#             centroid = klast[star]
#             summ1 = summ
#     return centroid
#
#
# file = open('27_A.txt')
# klasts = [[float(j) for j in i.replace(',', '.').split()] for i in file]
#
# klaster1 = [star for star in klasts if star[0] < 160]                                    ###
# klaster2 = [star for star in klasts if star[0] > 340]   ### 27A
#
# centr1 = f(klaster1)
# centr2 = f(klaster2)
#
# sr_x = (centr1[0] + centr2[0]) / 2
# sr_y = (centr1[1] + centr2[1]) / 2
# print(int(sr_x * 100000))
# print(int(sr_y * 100000))


from math import *

def f(klast):
    centroid, summ1 = None, float('inf')
    for star in range(len(klast)):
        summ = 0
        for next_star in range(len(klast)):
            if star == next_star:
                continue
            x1, y1, h1 = klast[star]
            x2, y2, h2 = klast[next_star]
            summ += sqrt((x2-x1)**2 + (y2 - y1)**2) * h2
        if summ < summ1:
            centroid = klast[star]
            summ1 = summ
    return centroid


file = open('27_B.txt')
klasts = [[float(j) for j in i.replace(',', '.').split()] for i in file]

klaster1 = [star for star in klasts if ((star[0] < -145) and (star[1] > -210) and (star[1] < -85))]
klaster2 = [star for star in klasts if ((star[1] > 95) and (star[0] > -95) and (star[0] < -5))]
klaster3 = [star for star in klasts if ((star[0] > 105) and (star[0] < 200) and (star[1] < 50) and (star[1] > -55))]

centr1 = f(klaster1)
centr2 = f(klaster2)
centr3 = f(klaster3)

print(centr1[0] + centr2[0] + centr3[0]) / 3
print(centr1[1] + centr2[1] + centr3[1]) / 3
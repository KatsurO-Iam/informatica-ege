from math import *
from time import *

def f(klast):
    centroid, summ1 = None, -float('inf')
    res = []
    for star in range(len(klast)):
        summ = 0
        for next_star in range(len(klast)):
            if star == next_star:
                continue
            x1, y1 = klast[star]
            x2, y2 = klast[next_star]
            summ += sqrt((x2-x1)**2 + (y2 - y1)**2)
        if summ > summ1:
            centroid = klast[star]
            summ1 = summ
    return centroid

start = time()
file = open('27.19.A_20497.txt')
klasts = [[float(j) for j in i.replace(',', '.').split()] for i in file]

# klaster1 = [star for star in klasts if (star[0] < 0 and star[1] < 0)]                       #
# klaster2 = [star for star in klasts if (star[0] > 0.5 and star[1] < 0 and star[1] > -5.5)]  # A
# klaster3 = [star for star in klasts if (star[0] > -1 and star[1] > 1 and star[1] < 6.5)]    #
#
# klaster1 = [star for star in klasts if ((star[0] < -37) and (star[1] < 40))]
# klaster2 = [star for star in klasts if ((star[1] < 35) and (star[0] > -27) and (star[0] < -9.txt))]
# klaster3 = [star for star in klasts if ((star[0] > 0) and (star[1] < 35))]                          #B
# klaster4 = [star for star in klasts if ((star[1] > 35) and (star[0] > -40) and (star[0] < -22))]
# klaster5 = [star for star in klasts if ((star[1] > 35) and (star[0] > -12) and (star[0] < 5))]
#
# centr1 = f(klaster1)
# centr2 = f(klaster2)
# centr3 = f(klaster3)
# centr4 = f(klaster4)
# centr5 = f(klaster5)
#
# sr_x = (centr1[0] + centr2[0] + centr3[0] + centr4[0] + centr5[0]) / 5
# sr_y = (centr1[1] + centr2[1] + centr3[1] + centr4[1] + centr5[1]) / 5
# print(int(sr_x * 10000), int(sr_y * 10000))
# end = time()
# print(end - start)
clusters = []
while klasts:
    clusters.append([klasts.pop()])
    for p1 in clusters[-1]:
        neigh = [star for star in klasts if dist(p1, star) < 0.45]
        clusters[-1] += neigh
        for star in neigh:
            klasts.remove(star)
print(len(clusters), [len(cl) for cl in clusters])

centroids = [f(clas) for clas in clusters if len(clas) > 5]

l = len(centroids)

x = sum([p[0] for p in centroids])/3
y = sum([p[1] for p in centroids])/3

print(int(x * 10_000), int(y * 10_000))
end = time()
print(end - start)

# from math import dist
# from turtle import *
# from time import *
#
# # def f(klast):
# #     centroid, summ1 = None, float('inf')
# #     for star in range(len(klast)):
# #         summ = 0
# #         for next_star in range(len(klast)):
# #             if star == next_star:
# #                 continue
# #             x1, y1 = klast[star]
# #             x2, y2 = klast[next_star]
# #             summ += sqrt((x2-x1)**2 + (y2 - y1)**2)
# #         if summ < summ1:
# #             centroid = klast[star]
# #             summ1 = summ
# #     return centroid
# #
#
# def vis():
#     up(); tracer(0); screensize(1000, 1000)
#     for cluster, colour in zip(clusters, ('red', 'green', 'black', 'blue', 'orange', 'pink', 'purple')):
#         for x,y in cluster:
#             goto(x*50, y*50)
#             dot(4 if colour != 'black' else 7, colour)
#     done()
# def centr(clust):
#     res = []
#     for point in clust:
#         res+= [(sum(dist(point, point1) for point1 in clust), point)]
#     return min(res)[1]
#
# start = time()
# klasts = [tuple(map(float, points.replace(',', '.').split())) for points in open('27.19.A_20497.txt')]
# clusters = []
#
# while klasts:
#     clusters.append([klasts.pop()])
#     for p1 in clusters[-1]:
#         neigh = [star for star in klasts if dist(p1, star) < 1]
#         clusters[-1] += neigh
#         for star in neigh:
#             klasts.remove(star)
# print(len(clusters), [len(cl) for cl in clusters])
# vis()
# centroids = [centr(clas) for clas in clusters]
#
# l = len(centroids)
#
# x = sum([p[0] for p in centroids])/l
# y = sum([p[1] for p in centroids])/l
#
# print(int(x * 100_000), int(y * 100_000))
# end = time()
# print(end - start)

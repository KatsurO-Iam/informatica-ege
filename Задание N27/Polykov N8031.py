from math import dist, sqrt
from turtle import *
from time import *

def f(klast):
    centroid, summ1 = None, float('inf')
    for star in range(len(klast)):
        summ = 0
        for next_star in range(len(klast)):
            if star == next_star:
                continue
            summ += dist(klast[star], klast[next_star])
        if summ < summ1:
            centroid = klast[star]
            summ1 = summ
    return centroid

#DBSCAN
#

# def vis():
#     up(); tracer(0); screensize(1000, 1000)
#     for cluster, colour in zip(clusters, ('red', 'green', 'black', 'blue', 'orange', 'pink', 'purple')):
#         for x,y in cluster:
#             goto(x*50, y*50)
#             dot(3 if colour != 'black' else 7, colour)
#     done()
# def centr(clust):
#     res = []
#     for point in clust:
#         res+= [(sum(dist(point, point1) for point1 in clust), point)]
#     return min(res)[1]
#
# start = time()
# klasts = [tuple(map(float, points.replace(',', '.').split())) for points in open('27-93b.txt')]
# clusters = []
# while klasts:        1ый вариант кластеризации
#     clusters.append([klasts.pop()])
#     for p1 in clusters[-1]:
#         for p2 in klasts[:]:
#             if dist(p1, p2) < 0.45:
#                 clusters[-1].append(p2)
#                 klasts.remove(p2)

# # while klasts:      2ой вариант кластеризации
# #     clusters.append([klasts.pop()])
# #     for p1 in clusters[-1]:
# #         neigh = [star for star in klasts if dist(p1, star) < 1.5 ]
# #         clusters[-1] += neigh
# #         for star in neigh:
# #             klasts.remove(star)
# print(len(clusters), [len(cl) for cl in clusters])
# vis()
# centroids = [centr(clas) for clas in clusters if len(clas) > 86]
#
# l = len(centroids)
#
# x = sum([p[0] for p in centroids])/l
# y = sum([p[1] for p in centroids])/l
#
# print(int(x * 100_000), int(y * 100_000))
# end = time()
# print(end - start)
# #DBSCAN

data = [[float(j) for j in i.replace(',', '.').split()] for i in open('27-93b.txt')]
# data = []
# for s in open('27-93b.txt'):
#     x,y = s.replace(',', '.').split()
#     data.append((float(x), float(y)))
#
def x(p1, p2):
    x1,y1 = p1
    x2, y2 = p2
    return sqrt((x2-x1)**2 + (y2 - y1)**2)

#К-средних
K = 4 # К-средних
centers = [(5.00000000, 11.00000000), (9.00000000, 5.00000000), (13.00000000,11.00000000),(9.00000000,9.00000000)]
oldCentrs = []
while centers != oldCentrs:
    oldCentrs = centers
    clusters = [[] for i in range(K)]
    for p in data:
        distToCentrov = [ dist(p, center) for center in centers]
        k = distToCentrov.index(min(distToCentrov))
        clusters[k].append(p)
        centers = [f(cluster) for cluster in clusters]

x = sum([p[0] for p in centers])/3
y = sum([p[1] for p in centers])/3

print(int(x * 100_000), int(y * 100_000))


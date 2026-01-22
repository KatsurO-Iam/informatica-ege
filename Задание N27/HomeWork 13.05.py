from math import dist, sqrt
from time import *

def centr(clust):
    res = []
    for point in clust:
        res+= [(sum(dist(point, point1) for point1 in clust), point)]
    return min(res)[1]

start = time()
klasts = [tuple(map(float, points.replace(',', '.').split())) for points in open('27A(13.КЕГЭ).txt')]
clusters = []
while klasts:
    clusters.append([klasts.pop()])
    for p1 in clusters[-1]:
        for p2 in klasts[:]:
            if dist(p1, p2) < 1:
                clusters[-1 ].append(p2)
                klasts.remove(p2)
# while klasts:
#     clusters.append([klasts.pop()])
#     for p1 in clusters[-1]:
#         neigh = [star for star in klasts if dist(p1, star) < 1.5 ]
#         clusters[-1] += neigh
#         for star in neigh:
#             klasts.remove(star)
print(len(clusters), [len(cl) for cl in clusters])

centroids = [centr(clas) for clas in clusters]

l = len(centroids)

x = sum([p[0] for p in centroids])/l
y = sum([p[1] for p in centroids])/l

print(int(x * 10_000), int(y * 10_000))
end = time()
print(end - start) #DBSCAN
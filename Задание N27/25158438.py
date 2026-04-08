from math import dist, sqrt
from time import *

def centr(clust):
    res = []
    for point in clust:
        res+= [(sum(dist(point, point1) for point1 in clust), point)]
    return min(res)[1]

start = time()
klasts = [tuple(map(float, points.replace(',', '.').split())) for points in open('27А 25158438.txt')]
clusters = []
while klasts:
    clusters.append([klasts.pop()])
    for p1 in clusters[-1]:
        for p2 in klasts[:]:
            if dist(p1, p2) < 1.1:
                clusters[-1 ].append(p2)
                klasts.remove(p2)



c1 = centr(clusters[0])
c2 = centr(clusters[1])

print((c1[0] + c2[0])/2 * 100000)
print((c1[1] + c2[1])/2 * 100000)
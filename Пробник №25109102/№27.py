#19782 

from math import dist

def centr(klast):
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

def diametr(clast):
    maxx = 0
    for p in clast:
        for p1 in clast:
            if p == p1:
                continue
            maxx = max(maxx, dist(p, p1))
    return maxx

klastsA = [[float(j) for j in i.replace(',', '.').split()] for i in open('27A.txt')]
klastsB = [[float(j) for j in i.replace(',', '.').split()] for i in open('27B.txt')]
clustersA = []
while klastsA:
    clustersA.append([klastsA.pop()])
    for p1 in clustersA[-1]:
        for p2 in klastsA[:]:
            if dist(p1, p2) < 1:
                clustersA[-1].append(p2)
                klastsA.remove(p2)
print(len(clustersA), [len(cl) for cl in clustersA])

clustersB = []
while klastsB:
    clustersB.append([klastsB.pop()])
    for p1 in clustersB[-1]:
        for p2 in klastsB[:]:
            if dist(p1, p2) < 0.5:
                clustersB[-1].append(p2)
                klastsB.remove(p2)
print(len(clustersB), [len(cl) for cl in clustersB])

rad_A = [diametr(clas) for clas in clustersA]
rad_B = [diametr(clas) for clas in clustersB]
print(rad_A, rad_B)

min_RA = min(rad_A)*10_000
max_RA = max(rad_A)*10_000

min_RB = min(rad_B)*10_000
max_RB = max(rad_B)*10_000
print(round(min_RA)//2, round(max_RA)//2, round(min_RB)//2, round(max_RB)//2)
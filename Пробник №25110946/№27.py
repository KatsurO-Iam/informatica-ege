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

klastsA = [[float(j) for j in i.replace(',', '.').split()] for i in open('27A.txt')]
klastsB = [[float(j) for j in i.replace(',', '.').split()] for i in open('27B.txt')]
clustersA = []
while klastsA:
    clustersA.append([klastsA.pop()])
    for p1 in clustersA[-1]:
        for p2 in klastsA[:]:
            if dist(p1, p2) < 2:
                clustersA[-1].append(p2)
                klastsA.remove(p2)
print(len(clustersA), [len(cl) for cl in clustersA])

clustersB = []
while klastsB:
    clustersB.append([klastsB.pop()])
    for p1 in clustersB[-1]:
        for p2 in klastsB[:]:
            if dist(p1, p2) < 1:
                clustersB[-1].append(p2)
                klastsB.remove(p2)
print(len(clustersB), [len(cl) for cl in clustersB])

c_A = [centr(clas) for clas in clustersA if len(clas) > 10]
c_B = [centr(clas) for clas in clustersB if len(clas) > 10]
print(c_A, c_B)

lA = len(c_A)

xA = sum([p[0] for p in c_A])/lA
yA = sum([p[1] for p in c_A])/lA

print(xA * 100_000, yA * 100_000)

lB = len(c_B)

xB = sum([p[0] for p in c_B])/lB
yB = sum([p[1] for p in c_B])/lB

print(xB * 100_000, yB * 100_000)

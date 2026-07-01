from math import *
from fnmatch import fnmatch


def cen(kl):
    centr, summ = None, float('inf')
    for i in range(len(kl)):
        s1 = 0
        for j in range(len(kl)):
            if i == j:
                continue
            s1 += dist(kl[i][0:2], kl[j][0:2])
        if s1 < summ:
            summ = s1
            centr = kl[i]
    return centr

def A1(kl, cen):
    m = float('inf')
    for x in kl:
        if fnmatch(x[2], 'K?III'):
            m = min(m, dist(x[0:2], cen[0:2]))
    return m

def B12(kl):
    m = 0
    for x in kl:
        if fnmatch(x[2], 'K?III'):
            m +=1
    return m

pointsA = [[float(j) for j in i.split()[0:2]] + [i.split()[2]] for i in open('27_A_31163.txt')]
pointsB = [[float(j) for j in i.split()[0:2]] + [i.split()[2]] for i in open('27_B_31163.txt')]

clustersA = []
while pointsA:
    clustersA.append([pointsA.pop()])
    for p1 in clustersA[-1]:
        for p2 in pointsA[:]:
            if dist(p1[0:2],p2[0:2]) < 1:
                pointsA.remove(p2)
                clustersA[-1].append(p2)
print(len(clustersA), [len(kl) for kl in clustersA])

clustersB = []
while pointsB:
    clustersB.append([pointsB.pop()])
    for p1 in clustersB[-1]:
        for p2 in pointsB[:]:
            if dist(p1[0:2],p2[0:2]) < 1:
                pointsB.remove(p2)
                clustersB[-1].append(p2)
print(len(clustersB), [len(kl) for kl in clustersB])

centrsA = [cen(kl) for kl in clustersA]
centrsB = [cen(kl) for kl in clustersB]
print(centrsA)
print(centrsB)

rast_a1 = min(A1(clustersA[0], centrsA[0]), A1(clustersA[-1], centrsA[-1]))
rast_a2 = dist((-1, -2), centrsA[0][0:2]) + dist((-1, -2), centrsA[-1][0:2])
print(A1(clustersA[0], centrsA[0]), A1(clustersA[-1], centrsA[-1]))
print(int(rast_a1*10_000), int(rast_a2 * 10_000))

print(int(centrsB[2][0]*10_000), int(centrsB[2][1] * 10_000))


from math import dist
from fnmatch import fnmatch

def a1(cluster, cent):
    minn = float('inf')
    maxx = float('-inf')
    for x in cluster:
        if fnmatch(x[2], 'Y?III'):
            minn = min(minn, dist(x[0:2], cent[0:2]))
            maxx = max(maxx, dist(x[0:2], cent[0:2]))
    return (minn, maxx)


def centr(kl):
    cen, s = None, float('inf')
    for i in range(len(kl)):
        s1 = 0
        for j in range(len(kl)):
            if i == j:
                continue
            s1 += dist(kl[i][0:2], kl[j][0:2])
        if s1 < s:
            s = s1
            cen = kl[i]
    return cen

pointsA = [[float(j) for j in i.split()[0:2]] + [str(i.split()[2])] for i in open('27_A_28766.txt')]
pointsB = [[float(j) for j in i.split()[0:2]] + [str(i.split()[2])] for i in open('27_B_28766.txt')]

clustersA = []
while pointsA:
    clustersA.append([pointsA.pop()])
    for p1 in clustersA[-1]:
        for p2 in pointsA[:]:
            if dist(p1[0:2], p2[0:2]) < 1:
                pointsA.remove(p2)
                clustersA[-1].append(p2)
print(len(clustersA), [len(kl) for kl in clustersA])

clustersB = []
while pointsB:
    clustersB.append([pointsB.pop()])
    for p1 in clustersB[-1]:
        for p2 in pointsB[:]:
            if dist(p1[0:2], p2[0:2]) < 1:
                pointsB.remove(p2)
                clustersB[-1].append(p2)
print(len(clustersB), [len(kl) for kl in clustersB])

centrsA = [centr(kl) for kl in clustersA]
centrsB = [centr(kl) for kl in clustersB]

print(centrsA)
print(centrsB)

A1, A2 = a1([[float(j) for j in i.split()[0:2]] + [str(i.split()[2])] for i in open('27_A_28766.txt')], centrsA[1])
print(int(A1*10_000), int(A2*10_000))

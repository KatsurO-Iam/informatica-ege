from math import *

def centr(klast):
    centroid,  summ1 = None, float('inf')
    for star in range(len(klast)):
        summ = 0
        for nx_star in range(len(klast)):
            if nx_star == star:
                continue
            summ += dist(klast[nx_star], klast[nx_star])
        if summ < summ1:
            centroid = klast[star]
            summ1 = summ
    return centroid

def acentr(cl):
    m = []
    for p in cl:
        s = sum(dist(p,p1) for p1 in cl)
        m.append([s,p])
    return max(m)[1]


klastsA = [[float(i) for i in j.replace(',','.').split()] for j in open('27_A_25114777.txt')]
klastsB = [[float(i) for i in j.replace(',','.').split()] for j in open('27_B_25114777.txt')]

clastersA = []
while klastsA:
    clastersA.append([klastsA.pop()])
    for p1 in clastersA[-1]:
        for p2 in klastsA[:]:
            if dist(p1, p2) < 1:
                clastersA[-1].append(p2)
                klastsA.remove(p2)
print(len(clastersA), [len(cl) for cl in clastersA])


clastersB = []
while klastsB:
    clastersB.append([klastsB.pop()])
    for p1 in clastersB[-1]:
        for p2 in klastsB[:]:
            if dist(p1, p2) < 1:
                clastersB[-1].append(p2)
                klastsB.remove(p2)
print(len(clastersB), [len(cl) for cl in clastersB])


mnA = min(clastersA, key=len)
mxA = max(clastersA, key=len)
pxA = acentr(mnA)[0]
pyA = acentr(mxA)[1]
print(int(pxA*10000), int(pyA*10000))

mnB = min(clastersB, key=len)
mxB = max(clastersB, key=len)
pxB = acentr(mnB)[0]
pyB = acentr(mxB)[1]
print(int(pxB*10000), int(pyB*10000))

# centroidsA = [centr(clas) for clas in clastersA if len(clas) > 50]
#
# l = len(centroidsA)
#
# x = sum([p[0] for p in centroidsA])/l
# y = sum([p[1] for p in centroidsA])/l
#
# print(int(x * 10_000), int(y * 10_000))
#
# centroidsB = [centr(clas) for clas in clastersB if len(clas) > 50]
#
# l = len(centroidsB)
#
# x = sum([p[0] for p in centroidsB])/l
# y = sum([p[1] for p in centroidsB])/l
#
# print(int(x * 10_000), int(y * 10_000))
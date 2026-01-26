from math import dist

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
#-------------------------------------------------------------------#
#-------------------------------------------------------------------#
pointsA = [[float(j) for j in i.replace(',', '.').split()] for i in open('27A.txt')]
pointsB = [[float(j) for j in i.replace(',', '.').split()] for i in open('27B.txt')]
#-------------------------------------------------------------------#

#-------------------------------------------------------------------#
klastsA = []
while pointsA:
    klastsA.append([pointsA.pop()])
    for p1 in klastsA[-1]:
        for p2 in pointsA[:]:
            if dist(p1, p2) < 1:
                klastsA[-1].append(p2)
                pointsA.remove(p2)
print(len(klastsA), [len(x) for x in klastsA])
#-------------------------------------------------------------------#
klastsB = []
while pointsB:
    klastsB.append([pointsB.pop()])
    for p1 in klastsB[-1]:
        for p2 in pointsB[:]:
            if dist(p1, p2) < 1:
                klastsB[-1].append(p2)
                pointsB.remove(p2)
print(len(klastsB), [len(x) for x in klastsB])
#-------------------------------------------------------------------#
centrsA = [f(klast) for klast in klastsA if len(klast) > 10]
rastX = abs(centrsA[0][0] - centrsA[1][0])*10_000
rastY = abs(centrsA[0][1] - centrsA[1][1])*10_000
#-------------------------------------------------------------------#
centrsB = [f(klast) for klast in klastsB if len(klast) > 10]
rast_centersB = []
for cents1 in range(len(centrsB) - 1):
        rast_centersB.append(dist(centrsB[cents1], centrsB[cents1 + 1]))

minB = min(rast_centersB)*10_000
maxB = max(rast_centersB)*10_000
#-------------------------------------------------------------------#
#-------------------------------------------------------------------#
print(int(rastX), int(rastY))
print(int(minB), int(maxB))
#-------------------------------------------------------------------#
# 23684 65128
# 72353 130974



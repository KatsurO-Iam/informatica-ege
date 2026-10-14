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
pointsA = [[float(j) for j in i.replace(',', '.').split()] for i in open('27A')]
pointsB = [[float(j) for j in i.replace(',', '.').split()] for i in open('27B')]
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
            if dist(p1, p2) < 0.2:
                klastsB[-1].append(p2)
                pointsB.remove(p2)
print(len(klastsB), [len(x) for x in klastsB])
#-------------------------------------------------------------------#
centrsA = [f(klast) for klast in klastsA if len(klast) > 10]
print(centrsA)
max_X = max(centrsA[0][0], centrsA[1][0])
max_Y = max(centrsA[0][1], centrsA[1][1])
#-------------------------------------------------------------------#
centrsB = [f(klast) for klast in klastsB if len(klast) > 10]
print(centrsA)
arifB_X = (centrsB[0][0] + centrsB[1][0] + centrsB[2][0]) / 3
arifB_Y = (centrsB[0][1] + centrsB[1][1] + centrsB[2][1]) / 3
#-------------------------------------------------------------------#
#-------------------------------------------------------------------#
print(abs(int(max_X * 10_000)), abs(int(max_Y * 10_000)))
print(abs(int(arifB_X * 10_000)), abs(int(arifB_Y * 10_000)))
#-------------------------------------------------------------------#

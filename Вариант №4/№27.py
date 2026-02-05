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
            if dist(p1, p2) < 0.2:
                klastsB[-1].append(p2)
                pointsB.remove(p2)
print(len(klastsB), [len(x) for x in klastsB])
#-------------------------------------------------------------------#
centrsA = [f(klast) for klast in klastsA if len(klast) > 10]
max_absc = max(centrsA[0][0], centrsA[1][0])*10_000
max_ord = max(centrsA[0][1], centrsA[1][1])*10_000
#-------------------------------------------------------------------#
centrsB = [f(klast) for klast in klastsB if len(klast) > 10]
print(centrsB)
arif_absc = ((centrsB[0][0]+centrsB[1][0]+centrsB[2][0])/3)*10_000
arif_ord = ((centrsB[0][1] + centrsB[1][1]+centrsB[2][1])/3)*10_000

#-------------------------------------------------------------------#
#-------------------------------------------------------------------#
print(int(max_absc), int(max_ord))
print(int(abs(arif_absc)), int(arif_ord))
#-------------------------------------------------------------------#
# 13330 110130
# 9612 48927



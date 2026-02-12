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

def rast(cent, kl):
    maxx = -float('inf')
    for p in kl:
        if dist(p, cent) > maxx:
            maxx = dist(p, cent)
    return maxx

def sum_rast(kl, cent):
    summ = 0
    for i in range(len(kl)):
        summ += dist(kl[i], cent)
    arif = summ / (len(kl) - 1)
    return arif

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
            if dist(p1, p2) < 2:
                klastsA[-1].append(p2)
                pointsA.remove(p2)
print(len(klastsA), [len(x) for x in klastsA])
#-------------------------------------------------------------------#
klastsB = []
while pointsB:
    klastsB.append([pointsB.pop()])
    for p1 in klastsB[-1]:
        for p2 in pointsB[:]:
            if dist(p1, p2) < 0.25:
                klastsB[-1].append(p2)
                pointsB.remove(p2)
print(len(klastsB), [len(x) for x in klastsB])
#-------------------------------------------------------------------#

#-------------------------------------------------------------------#
centrsA = [f(klast) for klast in klastsA if len(klast) > 10]
print(centrsA)
rast1 = abs(centrsA[0][0]-centrsA[1][0])
rast2 = abs(centrsA[0][1]-centrsA[1][1])
#-------------------------------------------------------------------#
centrsB = [f(klast) for klast in klastsB if len(klast) > 10]
print(centrsB)
dist_mm = dist(centrsB[1], centrsB[2])
dist_1 = rast(centrsB[0], klastsB[0])
dist_2 = rast(centrsB[1], klastsB[1])
dist_3 = rast(centrsB[2], klastsB[2])
#-------------------------------------------------------------------#

#-------------------------------------------------------------------#
print(int(rast1 * 10_000), int(rast2 * 10_000))
print(int(dist_mm*10_000), max(int(dist_1*10_000), int(dist_2*10_000), int(dist_3*10_000)))
#-------------------------------------------------------------------#
# 18236 93042
# 9163 1646

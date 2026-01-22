from math import dist

def f(klast):
    centroid, summ1 = None, -float('inf')
    for star in range(len(klast)):
        summ = 0
        for next_star in range(len(klast)):
            if star == next_star:
                continue
            summ += dist(klast[star], klast[next_star])
        if summ > summ1:
            centroid = klast[star]
            summ1 = summ
    return centroid
#-------------------------------------------------------------------#
def d(cents):
    cent_with_dist = []
    for koord in cents:
        cent_with_dist.append([dist((0,0), koord), koord[0], koord[1]])
    return cent_with_dist
#-------------------------------------------------------------------#
pointsA = [[float(j) for j in i.replace(',', '.').split()] for i in open('27_A.txt')]
pointsB = [[float(j) for j in i.replace(',', '.').split()] for i in open('27_B.txt')]
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
            if dist(p1, p2) < 1:
                klastsB[-1].append(p2)
                pointsB.remove(p2)
print(len(klastsB), [len(x) for x in klastsB])
#-------------------------------------------------------------------#
centrsA = [f(klast) for klast in klastsA]
sum_firstA = centrsA[0][0] + centrsA[0][1]
sum_secondA = centrsA[1][0] + centrsA[1][1]
#-------------------------------------------------------------------#
centrsB = [f(klast) for klast in klastsB if len(klast) > 10]
distB = sorted(d(centrsB))
maxXB = distB[2][1]
minYB = distB[0][2]
#-------------------------------------------------------------------#

#-------------------------------------------------------------------#
print(int(abs(sum_firstA)*10_000), int(abs(sum_secondA) * 10_000))
print(int(abs(maxXB) * 10_000), int(abs(minYB) * 10_000))
#-------------------------------------------------------------------#

# 1126711 1517181
# 213883 264132



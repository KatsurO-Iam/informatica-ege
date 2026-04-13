from math import dist

def f(klast):
    summ = -float('inf')
    for i in range(len(klast)):
        for j in range(len(klast)):
            if i == j:
                continue
            summ = max(summ, dist(klast[i], klast[j]))
    return summ
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
            if dist(p1, p2) < 0.4:
                klastsB[-1].append(p2)
                pointsB.remove(p2)
print(len(klastsB), [len(x) for x in klastsB])
#-------------------------------------------------------------------#
diamA = [f(klast) for klast in klastsA if len(klast) > 10]
minDiamA = min(diamA)
arifA = sum(diamA) / len(diamA)
#-------------------------------------------------------------------#
diamB = [f(klast) for klast in klastsB if len(klast) > 10]
minDiamB = min(diamB)
arifB = sum(diamB) / len(diamB)
#-------------------------------------------------------------------#
#-------------------------------------------------------------------#
print(int(minDiamA * 100_000), int(arifA * 100_000))
print(int(minDiamB * 100_000), int(arifB * 100_000))
#-------------------------------------------------------------------#

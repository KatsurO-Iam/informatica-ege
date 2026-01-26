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


klastsA = [[float(j) for j in i.replace(',', '.').split()] for i in open('27_A')]
klastsB = [[float(j) for j in i.replace(',', '.').split()] for i in open('27_B')]

centroidsA = []
while klastsA:
    centroidsA.append([klastsA.pop()])
    for p1 in centroidsA[-1]:
        for p2 in klastsA[:]:
            if dist(p1, p2) < 1:
                centroidsA[-1].append(p2)
                klastsA.remove(p2)
print(len(centroidsA), [len(x) for x in centroidsA])

centroidsB = []
while klastsB:
    centroidsB.append([klastsB.pop()])
    for p1 in centroidsB[-1]:
        for p2 in klastsB[:]:
            if dist(p1, p2) < 0.3:
                centroidsB[-1].append(p2)
                klastsB.remove(p2)
print(len(centroidsB), [len(x) for x in centroidsB])

centrsA = [f(klast) for klast in centroidsA]
centrsB = [f(klast) for klast in centroidsB]
print(centrsA, centrsB)

xA = sum([p[0] for p in centrsA])/2
yA = sum([p[1] for p in centrsA])/2

xB = sum([p[0] for p in centrsB])/3
yB = sum([p[1] for p in centrsB])/3

print(int(xA * 10_000), int(yA * 10_000))
print(int(xB * 10_000), int(yB* 10_000))





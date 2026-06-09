from math import dist

def f(kl):
    cent, summ = None, float('inf')
    for i in range(len(kl)):
        summ1 =0
        for j in range(len(kl)):
            if i == j:
                continue
            summ1 += dist(kl[i],kl[j])
        if summ > summ1:
            summ = summ1
            cent = kl[i]
    return cent

pointsA = [[float(x) for x in y.replace(',', '.').split()] for y in open('27A')]
pointsB = [[float(x) for x in y.replace(',', '.').split()] for y in open('27B')]

clustersA = []
while pointsA:
    clustersA.append([pointsA.pop()])
    for p1 in clustersA[-1]:
        for p2 in pointsA[:]:
            if dist(p1,p2) < 1:
                pointsA.remove(p2)
                clustersA[-1].append(p2)
print(len(clustersA), [len(x) for x in clustersA])

clustersB = []
while pointsB:
    clustersB.append([pointsB.pop()])
    for p1 in clustersB[-1]:
        for p2 in pointsB[:]:
            if dist(p1,p2) < 1:
                pointsB.remove(p2)
                clustersB[-1].append(p2)
print(len(clustersB), [len(x) for x in clustersB])

centrsA = [f(x) for x in clustersA]
centrsB = [f(x) for x in clustersB if len(x)>10]
print(centrsA)
print(centrsB)

min_Ax = int(min([centrsA[i][0] for i in range(len(centrsA))]) * 10_000)
min_Ay = int(min([centrsA[i][1] for i in range(len(centrsA))]) * 10_000)

rast_mm = int(dist(centrsB[1], centrsB[2]) * 10_000)

def rast(kl, cent):
    mm = 0
    for x in kl:
        if mm < dist(x, cent):
            mm = dist(x, cent)
    return mm

rast1 = rast(clustersB[0], centrsB[0])
rast2 = rast(clustersB[1], centrsB[1])
rast3 = rast(clustersB[2], centrsB[2])
max_rast = int(max(rast1, rast2, rast3)*10_000)

print(min_Ax, min_Ay)
print(rast_mm, max_rast)
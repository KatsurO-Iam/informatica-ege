from math import dist

def f(klast):
    summ, k = 0, 0
    for i in range(len(klast)):
        for j in range(len(klast)):
            if i == j:
                continue
            summ += dist(klast[i], klast[j])
            k+=1
    arif = summ/k
    return arif

klastsA = [[float(j) for j in i.replace(',', '.').split()] for i in open('27A.txt')]
klastsB = [[float(j) for j in i.replace(',', '.').split()] for i in open('27B.txt')]

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
            if dist(p1, p2) < 0.4:
                centroidsB[-1].append(p2)
                klastsB.remove(p2)
print(len(centroidsB), [len(x) for x in centroidsB])

arif_rastA = [f(cl) for cl in centroidsA]
min_arifA = min(arif_rastA)*100_000
max_arifA = max(arif_rastA)*100_000

arif_rastB = [f(cl) for cl in centroidsB]
min_arifB = min(arif_rastB)*100_000
max_arifB = max(arif_rastB)*100_000

print(int(min_arifA), int(max_arifA))
print(int(min_arifB), int(max_arifB))


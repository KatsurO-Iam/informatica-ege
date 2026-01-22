from math import dist, ceil


def centr(klast):
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

def diametr(clast):
    maxx = 0
    for p in clast:
        for p1 in clast:
            if p == p1:
                continue
            maxx = max(maxx, dist(p, p1))
    return maxx

klastsA = [[float(j) for j in i.replace(',', '.').split()] for i in open('27A.txt')]
klastsB = [[float(j) for j in i.replace(',', '.').split()] for i in open('27B.txt')]
clustersA = []
while klastsA:
    clustersA.append([klastsA.pop()])
    for p1 in clustersA[-1]:
        for p2 in klastsA[:]:
            if dist(p1, p2) < 1:
                clustersA[-1].append(p2)
                klastsA.remove(p2)
print(len(clustersA), [len(cl) for cl in clustersA])

clustersB = []
while klastsB:
    clustersB.append([klastsB.pop()])
    for p1 in clustersB[-1]:
        for p2 in klastsB[:]:
            if dist(p1, p2) < 0.4:
                clustersB[-1].append(p2)
                klastsB.remove(p2)
print(len(clustersB), [len(cl) for cl in clustersB])


centroidsA = [diametr(clas) for clas in clustersA if len(clas) > 0]
centroidsB = [diametr(clas) for clas in clustersB if len(clas) > 0]

min_DA = min(centroidsA)*100_000
sr_DA = sum([di for di in centroidsA])/len(centroidsA)*100_000
min_DB = min(centroidsB)*100_000
sr_DB = sum([di for di in centroidsB])/len(centroidsB)*100_000
print(min_DA, sr_DA)
print(min_DB, sr_DB)



# klastsA = [[float(j) for j in i.replace(',', '.').split()] for i in open('27A.txt')]
#
# centr1 = diametr([star for star in klastsA if star[0] < 0 and star[1] > 0])
# centr2 = diametr([star for star in klastsA if star[0] > 2 and star[1] > 2])
# centr3 = diametr([star for star in klastsA if star[0] > 4 and star[1] < 2])
# centr4 = diametr([star for star in klastsA if star[0] < 1 and star[1] < 0])
# print(centr1, centr2, centr3, centr4)
#
#
# min_D = min(centr1, centr2, centr3, centr4) * 100_000
#
# # sr_x = (centr1[0] + centr2[0] + centr3[0] + centr4[0]) / 4
# # sr_y = (centr1[1] + centr2[1] + centr3[1] + centr4[1]) / 4
# # print(abs(int(sr_x * 100000)), abs(int(sr_y * 100000)))
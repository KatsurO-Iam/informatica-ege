from math import dist

#-------------------------------------------------------------------#
#-------------------------------------------------------------------#
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
def x(klast):
    point, maxx, minn = None,0,0
    for i in range(len(klast)):
        for j in range(len(klast)):
            if i == j:
                continue
            elif klast[i][0] > klast[j][0]:
                maxx+=1
            elif klast[i][0] < klast[j][0]:
                minn+=1
        if maxx == minn:
            point = klast[i]
        maxx = 0
        minn = 0
    return point
#-------------------------------------------------------------------#
def y(klast):
    point, maxx, minn = None,0,0
    for i in range(len(klast)):
        for j in range(len(klast)):
            if i == j:
                continue
            elif klast[i][1] > klast[j][1]:
                maxx+=1
            elif klast[i][1] < klast[j][1]:
                minn+=1
        if maxx == minn:
            point = klast[i]
        maxx = 0
        minn = 0
    return point
#-------------------------------------------------------------------#
#-------------------------------------------------------------------#
klastsA = [[float(j) for j in i.replace(',', '.').split()] for i in open('27A')]
klastsB = [[float(j) for j in i.replace(',', '.').split()] for i in open('27B')]
#-------------------------------------------------------------------#
#-------------------------------------------------------------------#
centroidsA = []
while klastsA:
    centroidsA.append([klastsA.pop()])
    for p1 in centroidsA[-1]:
        for p2 in klastsA[:]:
            if dist(p1, p2) < 1:
                centroidsA[-1].append(p2)
                klastsA.remove(p2)
print(len(centroidsA), [len(x) for x in centroidsA])
#-------------------------------------------------------------------#

centroidsB = []
while klastsB:
    centroidsB.append([klastsB.pop()])
    for p1 in centroidsB[-1]:
        for p2 in klastsB[:]:
            if dist(p1, p2) < 0.3:
                centroidsB[-1].append(p2)
                klastsB.remove(p2)
print(len(centroidsB), [len(x) for x in centroidsB])
#-------------------------------------------------------------------#
#-------------------------------------------------------------------#
centrsA_X = [x(klast) for klast in centroidsA]
centrsA_Y = [y(klast) for klast in centroidsA]
#-------------------------------------------------------------------#
centrsB_X = [x(klast) for klast in centroidsB]
centrsB_Y = [y(klast) for klast in centroidsB]
#-------------------------------------------------------------------#
#-------------------------------------------------------------------#
arif_Ax = ((centrsA_X[0][0] + centrsA_X[1][0])/2)*10_000
arif_Ay = ((centrsA_Y[0][1] + centrsA_Y[1][1])/2)*10_000
#-------------------------------------------------------------------#
arif_Bx = ((centrsB_X[0][0] + centrsB_X[1][0] + centrsB_X[2][0])/3)*10_000
arif_By = ((centrsB_Y[0][1] + centrsB_Y[1][1] + centrsB_Y[2][1])/3)*10_000
#-------------------------------------------------------------------#
#-------------------------------------------------------------------#
print(int(arif_Ax), int(arif_Ay))
print(int(arif_Bx), int(arif_By))

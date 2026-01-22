from math import dist, sin, cos, pi, sqrt

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

def main():
    klastsA = [[float(j) for j in i.replace(',', '.').split()] for i in open('27_A (3).txt')]
    klastsB = [[float(j) for j in i.replace(',', '.').split()] for i in open('27_B (3).txt')]
    # -------------------------------------------------------------------#
    dec_klastsA = []
    for point in klastsA:
        x = point[1] * cos(((point[0]* pi)/180))
        y = point[1] * sin(((point[0]* pi)/180))
        dec_klastsA.append([x, y])

    centroidsA = []
    while dec_klastsA:
        centroidsA.append([dec_klastsA.pop()])
        for p1 in centroidsA[-1]:
            for p2 in dec_klastsA[:]:
                if dist(p1, p2) < 2:
                    centroidsA[-1].append(p2)
                    dec_klastsA.remove(p2)
    print(len(centroidsA), [len(x) for x in centroidsA])
#-------------------------------------------------------------------#
    dec_klastsB = []
    for point in klastsB:
        x = point[1] * cos(((point[0] * pi) / 180))
        y = point[1] * sin(((point[0] * pi) / 180))
        dec_klastsB.append([x, y])

    centroidsB = []
    while dec_klastsB:
        centroidsB.append([dec_klastsB.pop()])
        for p1 in centroidsB[-1]:
            for p2 in dec_klastsB[:]:
                if dist(p1, p2) < 1:
                    centroidsB[-1].append(p2)
                    dec_klastsB.remove(p2)
    print(len(centroidsB), [len(x) for x in centroidsB])
    # -------------------------------------------------------------------#
    centrsA = [f(klast) for klast in centroidsA]
    centrsB = [f(klast) for klast in centroidsB]
    print(centrsA, centrsB)
    # -------------------------------------------------------------------#
    xA = sum([p[0] for p in centrsA])/2
    yA = sum([p[1] for p in centrsA])/2
    # -------------------------------------------------------------------#
    xB = sum([p[0] for p in centrsB])/3
    yB = sum([p[1] for p in centrsB])/3
    # -------------------------------------------------------------------#
    print(int(xA * 10_000), int(yA * 10_000))
    print(int(xB * 10_000), int(yB* 10_000))

if __name__ == '__main__':
    main()



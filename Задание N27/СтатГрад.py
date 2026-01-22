from math import *
from time import *

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

start = time()
file = open('27_Б.txt')
klasts = [[float(j) for j in i.replace(',', '.').split()] for i in file]


# klaster1 = [star for star in klasts if star[1] < -6]                                    ###
# klaster2 = [star for star in klasts if ((star[1] < star[0] - 11) and (star[1] > -6))]   ### 27A
# klaster3 = [star for star in klasts if star[1] > star[0] - 11]                          ###


# klaster1 = [star for star in klasts if star[1] < -5]
# klaster2 = [star for star in klasts if ((star[1] < star[0]*0.8 + 0.8) and (star[1] > -5))]
# klaster3 = [star for star in klasts if ((star[1] > star[0]*0.8 + 0.8) and (star[1] < star[0]*(4/3) + 8))]
# klaster4 = [star for star in klasts if ((star[1] > star[0]*(4/3) + 8) and (star[0] > -9.txt.9.txt))]
# klaster5 = [star for star in klasts if ((star[1] > star[0]*(-1.5) - 19.5) and (star[0] < -9.txt.9.txt))]
# klaster6 = [star for star in klasts if star[1] < star[0]*(-1.5) - 19.5]
#
# centr1 = f(klaster1)
# centr2 = f(klaster2)
# centr3 = f(klaster3)
# centr4 = f(klaster4)
# centr5 = f(klaster5)
# centr6 = f(klaster6)


centr1 = f([star for star in klasts if star[1] < -5])
centr2 = f([star for star in klasts if ((star[1] < star[0]*0.8 + 0.8) and (star[1] > -5))])
centr3 = f([star for star in klasts if ((star[1] > star[0]*0.8 + 0.8) and (star[1] < star[0]*(4/3) + 8))])
centr4 = f([star for star in klasts if ((star[1] > star[0]*(4/3) + 8) and (star[0] > -9.9))])
centr5 = f([star for star in klasts if ((star[1] > star[0]*(-1.5) - 19.5) and (star[0] < -9.9))])
centr6 = f([star for star in klasts if star[1] < star[0]*(-1.5) - 19.5])

sr_x = (centr1[0] + centr2[0] + centr3[0] + centr4[0] + centr5[0] + centr6[0]) / 6
sr_y = (centr1[1] + centr2[1] + centr3[1] + centr4[1] + centr5[1] + centr6[1]) / 6
print(abs(int(sr_x * 10000)), abs(int(sr_y * 10000)))
end = time()
print(end - start)
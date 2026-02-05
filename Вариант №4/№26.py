from django.conf.locale import ko

with open('26') as f:
    n,m = f.readline().split()
    kom = []
    sam = []
    for x in range(int(n)):
        kom.append(int(f.readline()))
    for x in range(int(m)):
        sam.append(int(f.readline()))

pas = []
sam.sort(reverse=True)
kom.sort(reverse=True)

for i in range(len(sam)):
    for j in range(len(kom)):
        if sam[i]//kom[j] >=2 and j not in pas:
            pas.append(j)
            break
print(len(pas))
m = 0
for i in pas:
    m = max(m, kom[i])
print(m)
# 398
# 96867
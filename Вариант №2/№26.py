with open('26') as f:
    n,m = map(int,f.readline().split())
    kom = []
    for _ in range(n):
        kom.append(int(f.readline()))
    sam = []
    for _ in range(m):
        sam.append(int(f.readline()))

kom = sorted(kom, reverse=True)
sam = sorted(sam, reverse=True)
pas = []

for i in range(len(sam)):
    for j in range(len(kom)):
        if sam[i] > kom[j] and j not in pas:
            pas.append(j)
            break
print(len(pas))
ans2 = 0
for i in pas:
    ans2 = max(ans2, kom[i])
print(ans2)
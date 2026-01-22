with open('24.txt') as f:
    sp = f.readline()

sp = sp.replace('RUSTEM', '*')
print(sp.count('RUS'))
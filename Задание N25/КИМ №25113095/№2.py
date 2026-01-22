from fnmatch import fnmatch

for x in range(2658, 10**9, 2658):
    if fnmatch(str(x), '85?16*4') and x % 2658 == 0:
        print(x, x//2658)
from fnmatch import fnmatch

for i in range(154682, 10**11, 154682):
    if fnmatch(str(i), '*192?3*68') and i % 154682 == 0:
        print(i, i//154682)
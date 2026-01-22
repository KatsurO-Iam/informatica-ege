from fnmatch import fnmatch
for i in range(2025, 10**10 + 1, 2025):
    if fnmatch(str(i), '21?5846*?'):
        print(i, i//2025)
from  string import ascii_lowercase, digits

key = (digits+ascii_lowercase)[:15]
print(key)
for i in key:
    x = int(f'99658{i}29', base=15) + int(f'102{i}023', 15)
    if x % 14 == 0:
        print(x//14)
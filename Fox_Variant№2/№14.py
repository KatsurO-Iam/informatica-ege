from  string import ascii_lowercase, digits

key = (digits+ascii_lowercase)[:16]
print(key)
for i in key:
    x = int(f'153{i}4', base=16) + int(f'1{i}325', 16)
    if x % 15 == 0:
        print(x//14)
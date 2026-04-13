from string import digits, ascii_lowercase
alpf = (digits + ascii_lowercase)[:17]
for x in alpf:
    a = int(f'12346{x}17', 17) + int(f'7{x}171', 17)
    if a % 16 == 0:
        print(a//16)
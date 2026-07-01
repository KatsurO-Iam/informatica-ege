from  string import digits,ascii_letters

alph = (digits + ascii_letters)[:19]
for x in alph:
    a = int(f'76{x}79645',19) + int(f'35{x}42', 19) + int(f'332{x}6', 19)
    if a % 18 ==0:
        print(x, a//18)
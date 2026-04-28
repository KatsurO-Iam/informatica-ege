from  string import digits,ascii_letters

alph = (digits + ascii_letters)[:15]
for x in alph:
    a = int(f'97531{x}19',15)+int(f'3{x}519',15)
    if a % 11 == 0:
        print(a//11, x)
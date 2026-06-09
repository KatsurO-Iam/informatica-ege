from string import digits, ascii_letters

a = (2*2187**2020 + 729**2021 - 2*243**2022 + 81**2023 - 2 *27**2024 - 6561)
c = 0
while a > 0:
    if a % 27 > 9:
        c +=1
    a = a//27
print(c)

# alph = (digits + ascii_letters)[:29]
# for x in alph:
#     a = int(f'923{x}874', 29) + int(f'524{x}6152', 29)
#     if a % 28 == 0:
#         print(x, a//28)


# for x in range(3000):
#     a = 9*(11**210) + 8*(11**150) - x
#     c = 0
#     while a > 0:
#         if a % 11 == 0:
#             c +=1
#         a = a//11
#     if c == 60:
#         print(x)
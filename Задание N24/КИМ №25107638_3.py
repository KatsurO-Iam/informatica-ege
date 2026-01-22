from re import*
with open("24(2).txt") as f:
    sp = f.readline()

pattern = "[1-9.txt][0-9.txt]*(?:[+*][1-9.txt][0-9.txt]*)*"
max_len = 0
for x in finditer(pattern, sp):
    if x.group().count("*") + x.group().count("+") > max_len:
        max_len = x.group().count("*") + x.group().count("+")

print(max_len+1)

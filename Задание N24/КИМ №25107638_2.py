import re

with open("24(1).txt", "r") as f:
    s = f.read().strip()

pattern = r"A([^A]+)A\1A\1A"
max_len = 0
for match in re.finditer(pattern, s):
    max_len = max(max_len, len(match.group(0)))
print(max_len)


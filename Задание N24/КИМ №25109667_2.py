import re
print(len(max(re.findall(r'[AD]*DAD+[AD]*', open('24 (5).txt').readline()), key=len)))
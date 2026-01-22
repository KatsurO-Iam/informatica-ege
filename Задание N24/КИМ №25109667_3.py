import sys
from re import*



reg = compile('[CD]*[ABEF]+[CD]*')
print(len(max(reg.findall(open('24 (6).txt').readline()))))
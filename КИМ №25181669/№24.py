from re import*

line = open('24.txt').readline()
strip = line[:].replace('f', ' f ')
strp = strip.split(' ')
k = 0
for i in range(1, len(strp) - 1):
    if strp[i] == 'f':
        k+=1
    if k == 123:
        print(strp[i - 1], strp[i], strp[i + 1])
        break
print(line.find('picyb4g9jybhb7k57i3ez5hrm'))
print(len('picyb4g9jybhb7k57i3ez5hrm'))
print(line.find('picyb4g9jybhb7k57i3ez5hrm') + len('picyb4g9jybhb7k57i3ez5hrm') + 1)
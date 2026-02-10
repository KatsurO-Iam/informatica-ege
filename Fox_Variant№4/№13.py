# ip = '111.91.200.28'
# print('.'.join([bin(int(x) + 256)[3:] for x in ip.split('.')]))
# ip = '111.91.192.0'
# print('.'.join([bin(int(x) + 256)[3:] for x in ip.split('.')]))
from ipaddress import *

net = ip_network('204.152.228.160/255.255.255.224')
c = 0
for ip in net:
    x = bin(int(ip))[2:]
    if x.count('1') > x.count('0'):
        c +=1
print(c)
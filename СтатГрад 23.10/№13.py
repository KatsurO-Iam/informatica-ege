from ipaddress import *

ip = '255.254.0.0'
print('.'.join([bin(int(x) + 256)[3:] for x in ip.split('.')]))
ip = '167.66.0.1'
print('.'.join([bin(int(x) + 256)[3:] for x in ip.split('.')]))
print(167 + 66 + 1)
#234


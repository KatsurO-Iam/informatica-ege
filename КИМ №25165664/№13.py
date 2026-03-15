ip = '192.214.127.184'
print('.'.join([bin(int(x) + 256)[3:] for x in ip.split('.')]))
ip = '255.255.255.224'
print('.'.join([bin(int(x) + 256)[3:] for x in ip.split('.')]))

from ipaddress import *

# cnt = 0
# for a in range(0,255):
#     for ip in ip_network(f'192.214.{a}.184/255.255.255.224'):
#         x = bin(int(ip))[2:]
#         if x.count('1') > 15:
#             print(a)

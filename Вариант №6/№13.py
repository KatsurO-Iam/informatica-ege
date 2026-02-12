from ipaddress import *

# ip = '111.91.200.28'
# print('.'.join([bin(int(x) + 256)[3:] for x in ip.split('.')]))
# ip = '111.91.192.0'
# print('.'.join([bin(int(x) + 256)[3:] for x in ip.split('.')]))

net = ip_network('200.33.100.0/255.255.248.0',0)
cnt = 0
for ip in net:
    x = bin(int(ip))[2:]
    if x.count('1') % 7 != 0:
        cnt += 1
print(cnt)
from ipaddress import *

net = ip_network('105.224.200.224/255.255.255.224')
cnt = 0
for ip in net:
    x = bin(int(ip))[2:]
    if x.count('1') % 4 == 0:
        cnt += 1
print(cnt)
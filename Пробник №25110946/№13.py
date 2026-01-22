from ipaddress import *

net = ip_network('112.160.0.0/255.240.0.0')

cnt =0
for ip in net:
    ip = bin(int(ip))[2:]
    if ip.count('1') % 3 != 0:
        cnt += 1
print(cnt)
from ipaddress import *

ip = '89.16.43.107'
print('.'.join([bin(int(x) + 256)[3:] for x in ip.split('.')]))
ip = '255.224.0.0'
print('.'.join([bin(int(x) + 256)[3:] for x in ip.split('.')]))

# net = ip_network('204.16.168.0/255.255.248.0')
# cnt = 0
# for ip in net:
#     x = bin(int(ip))[2:]
#     if x.count('1') % 5 != 0:
#         cnt += 1
# print(cnt)
s = '01011001.00011111.11111111.11111110'
s = s.split('.')
for x in s:
    print(int(x, 2), end='')
#8931255254

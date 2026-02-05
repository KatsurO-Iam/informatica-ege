from ipaddress import *

ip = '153.196.115.75'
print('.'.join([bin(int(x) + 256)[3:] for x in ip.split('.')]))
ip = '255.248.0.0'
print('.'.join([bin(int(x) + 256)[3:] for x in ip.split('.')]))

# net = ip_network('204.16.168.0/255.255.248.0')
# cnt = 0
# for ip in net:
#     x = bin(int(ip))[2:]
#     if x.count('1') % 5 != 0:
#         cnt += 1
# print(cnt)
s = '10011001.11000111.11111111.11111110'
s = s.split('.')
for x in s:
    print(int(x, 2), end='')
#153199255254

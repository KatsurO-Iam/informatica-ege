from ipaddress import *
#
# net = ip_network('99.165.134.0/255.255.254.0')
# cnt = 0
# for ip in net:
#     x = bin(int(ip))[2:]
#     k = sum([int(q) for q in x])
#     if k % 3 == 0:
#         cnt +=1
# print(cnt)




# ip = '27.9.txt.142.131'
# print('.'.join([bin(int(x) + 256)[3:] for x in ip.split('.')]))
# ip = '134.92.104.0'
# print('.'.join([bin(int(x) + 256)[3:] for x in ip.split('.')]))
# l = list()
# for i in range(255):
#     k = int(bin(i)) & int((bin(2)))
#     l.append(f'01110101.10011101.{k}.00001000')
#
# print(int('11111110', 2))
#
# from ipaddress import *
# for i in range(253, 256):
#     mask = f'255.255.{str(i)}.0'
#     net = ip_network(f'134.97.250.117/{mask}', 0)
#     for ip in net:
#         x = bin(int(ip))[2:]
#         if x[:16].count('1') >= x[16:].count('1'):
#             print(i)

# from ipaddress import *
# net = ip_network("172.17.167.18/255.255.240.0")




# from ipaddress import ip_network
#
# net = ip_network('172.16.160.0/255.255.240.0')
#
# cnt = 0
#
# for ip in net:
#     x = bin(int(ip))[2:]
#     k = sum([int(q) for q in x])
#     if k % 4 != 0:
#         cnt +=1
#
# print(cnt)


# ip = '255.255.240.0'
# print('.'.join([bin(int(x) + 256)[3:] for x in ip.split('.')]))


# from ipaddress import *
#
# def f(n):
#     if n != n[::-1]:
#         return False
#     return True
#
# net = ip_network('95.112.224.0/255.255.255.128')
# cnt = 0
# for ip in net:
#     x = bin(int(ip))[2:]
#     k = x[-8:]
#     b = f(k)
#     if b == True:
#         cnt +=1
# print(cnt)

# ip = '191.128.66.83'
# print('.'.join([bin(int(x) + 256)[3:] for x in ip.split('.')]))
# ip = '255.192.0.0'
# print('.'.join([bin(int(x) + 256)[3:] for x in ip.split('.')]))
#
# s = '10111111.10111111.11111111.11111110'
# s = s.split('.')
# for x in s:
#     print(int(x,2) , end = '')
c = 0
net = ip_network('172.30.0.0/255.254.0.0')
for ip in net:
    x = bin(int(ip))[2:]
    k = sum([int(q) for q in x])
    if k % 12 != 0:
        c+=1
print(c)
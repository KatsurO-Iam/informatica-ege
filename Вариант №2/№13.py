from ipaddress import ip_network
ip = '255.255.240.0'
print('.'.join([bin(int(x) + 256)[3:] for x in ip.split('.')]))
ip = '10.100.202.34'
print('.'.join([bin(int(x) + 256)[3:] for x in ip.split('.')]))
s = '00001010.01100100.11001111.11111110'
s = s.split('.')
for x in s:
    print(int(x, 2), end='')
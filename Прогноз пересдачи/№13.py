ip = '111.91.200.28'
print('.'.join([bin(int(x) + 256)[3:] for x in ip.split('.')]))
ip = '111.91.192.0'
print('.'.join([bin(int(x) + 256)[3:] for x in ip.split('.')]))

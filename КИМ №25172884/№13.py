ip = '246.51.128.202'
print('.'.join([bin(int(x) + 256)[3:] for x in ip.split('.')]))
ip = '255.255.254.0'
print('.'.join([bin(int(x) + 256)[3:] for x in ip.split('.')]))

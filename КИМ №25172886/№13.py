ip = '95.24.2.9'
print('.'.join([bin(int(x) + 256)[3:] for x in ip.split('.')]))
ip = '95.24.3.10'
print('.'.join([bin(int(x) + 256)[3:] for x in ip.split('.')]))

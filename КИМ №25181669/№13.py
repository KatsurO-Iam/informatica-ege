ip = '203.155.64.0'
print('.'.join([bin(int(x) + 256)[3:] for x in ip.split('.')]))
ip = '203.155.64.98'
print('.'.join([bin(int(x) + 256)[3:] for x in ip.split('.')]))

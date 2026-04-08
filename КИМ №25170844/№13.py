ip = '95.24.2.9'
print('.'.join([bin(int(x) + 256)[3:] for x in ip.split('.')]))
ip = '95.24.3.10'
print('.'.join([bin(int(x) + 256)[3:] for x in ip.split('.')]))

from ipaddress import *

for mask in range(33):
    net1 = ip_network(f'95.24.2.9/{mask}', 0)
    net2 = ip_network(f'95.24.3.10/{mask}', 0)
    if net1.network_address != net2.network_address:
        print(sum(1 for ip in net1.hosts() if f'{ip:b}'[-1] == '0'))
        print(sum(1 for ip in net2.hosts() if f'{ip:b}'[-1] == '0'))

from ipaddress import *

net = ip_network('189.163.226.71/255.255.255.240', 0)

for x in net:
    print(x)
    break


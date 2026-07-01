from ipaddress import *

net = ip_network('64.237.228.143/255.255.248.0',0)
for x in net:
    print(x)
    break
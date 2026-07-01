from ipaddress import *

net = ip_network('185.249.55.138/18', 0)
for i in net:
    print(i)
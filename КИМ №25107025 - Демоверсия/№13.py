from ipaddress import ip_network, ip_address

net = ip_network('191.128.66.83/255.192.0.0', 0)
for ip in net:
    print(ip)
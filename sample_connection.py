#!/usr/bin/env python

#this examples provides 3ways of establishing communication with the network devices through Ip addr or domain name

# method -1:
from netmiko import ConnectHandler


with ConnectHandler( ip = 'ip addr',
                    port = 22, #optional, if not provided default port is 22
                    device_type='Cisco_nxos', #mandatory to define the device we are communicating
                    username = "cisco",
                    password = "admin") as ch:
    
    print(ch.send_command("ip a")) 

### another way of connecting, creating a dictionary with device login creds.
cisco_router = {
    'device_type': 'Cisco_Ios',
    'host' : 'cisco.domain.com', #for using site address use host variable instead of IP.
    'username' : 'cisco',
    'password' : 'cisco',
}

ch = ConnectHandler(**cisco_router) # ** before cisco_router, defines cisco_router is a dictionary


##method -3 to embed connection in other codes

net_cnt = ConnectHandler(device_type = 'cisco_ios', host = 'ip addr', username = 'cisco', password = 'cisco')
#!/usr/bin/env python

""" this examples show how to send commands and receive the outputs for 
    those commands and also to check the current prompt of the device 
"""

from netmiko import Netmiko
from getpass import getpass
from easyad import EasyAD
from json import dumps

 #first creating devices and its login creds and dict
 
 # after the password is given check and verify it with AD
 username = input("Enter username: ")
 password = getpass("Enter password:")
 cisco1 = {
     'device_type' : 'cisco_ios',
     'ip' : 'ip addr',
     'username' : username,
     'password' : password,
     'port' : 22,
      }
#creating a dict for setting up configuration of our active directory

Config = dict(
        AD_SERVER = "in.ril.com",
        AD_DOMAIN = "ril.com",
        CA_CERT_FILE = ""
)

ad = EasyAD(Config)

 user = ad.authenticate(username, password, json_safe = True)
 
 if user:
     print(dumps(user, sort_keys=True, indent=2, ensure_ascii=False))
     
 else:
     print("invalid credentials")
  
# connection with WLC or network device is done through below code
 cnet = ConnectHandler(**cisco1)
 
 print ("Connection established")
 
 prompt = cnet.find_prompt()
 print (prompt)
 
 if (prompt == 'r1#') :
     output = cnet.send_command('show running-config')
     
 else:
     print(' router not configured ')
    
#results for that command

print (output)

cnet.enable()

cnet.send_command('conf t', 'vlan 200', 'name vlan', 'no sh')
    
cnet.disconnect()
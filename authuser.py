
from netmiko import ConnectHandler
from getpass import getpass

username = input("enter username: ")
password = getpass("enter pwd: ")

try:
   with ConnectHandler( ip = 'x.x.x.x',
                    port = 22, #optional, if not provided default port is 22
                    device_type='cisco_ios', #mandatory to define the device we are communicating
                    username = username,
                    password = password) as ch:

except NetmikoAuthenticationException:
   print("Incorrect credentials")

print("Connection established")

from netmiko import ConnectHandler
from getpass import getpass


username = input("Enter Username: ")
password = getpass("Enter Password: ")
interface = input("Enter the interface to configure: " )
ip = input("Enter the Ip address: ")
mask = input("Enter the mask: ")

with ConnectHandler( ip = '192.168.122.226',
                    port = 22, #optional, if not provided default port is 22
                    device_type='cisco_ios', #mandatory to define the device we are communicating
                    username = username,
                    password = password) as ch:


  print ("connection esatblished")

  interface_config = [
     "interface {}".format(interface),
     "ip address {} {}".format(ip,mask),
     "no shut"
  ]
  result = ch.send_config_set(interface_config)
  print (result)

  new = ch.send_command("sh ip int br")
  print (new)
  ch.disconnect()

  
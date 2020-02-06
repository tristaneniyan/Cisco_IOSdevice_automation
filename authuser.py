
from netmiko import ConnectHandler
from getpass import getpass

username = input("enter username: ")
password = getpass("enter pwd: ")

try:
   with ConnectHandler( ip = '192.168.122.226',
                    port = 22, #optional, if not provided default port is 22
                    device_type='cisco_ios', #mandatory to define the device we are communicating
                    username = username,
                    password = password) as ch:

except NetmikoAuthenticationException:
   print("Incorrect credentials")

  prompt = ch.find_prompt()
  print (prompt)
  if (prompt == "R1#"):
    print ("connection made")
    result = ch.send_command( "sh ip int br")
    print (result)
  else:
    print ("error")

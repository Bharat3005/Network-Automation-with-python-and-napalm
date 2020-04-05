import getpass
import telnetlib

#!/usr/bin/env python

HOST = "192.168.122.101"
user = input("Enter your telnet Username: ")
password = getpass.getpass()

tn = telnetlib.Telnet(HOST)

tn.read_until(b"Username: ")
tn.write(user.encode('ascii') + b"\n")

#Username and password are stored in the router

if password:
    tn.read_until(b"Password: ")
    tn.write(password.encode('ascii') + b"\n")

tn.write(b"enable\n")
tn.write(b"config t\n")

#Range for VLAN Configurtion
for n in range(2,101):
    tn.write(b"vlan " + str(n).encode('ascii') + b"\n")
    tn.write(b"name Python_VLAN_" + str(n).encode('ascii') + b"\n")

tn.write(b"end\n")
tn.write(b"exit\n")
# Printing the script output on the remote machine
print(tn.read_all().decode('ascii'))

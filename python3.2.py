import getpass
import telnetlib

#!/usr/bin/env python

HOST = "192.168.122.100"
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
tn.write(b"int lo0\n")
tn.write(b"ip address 10.122.10.1 255.255.255.255\n")
tn.write(b"int lo1\n")
tn.write(b"ip add 10.122.11.1 255.255.255.255\n")
tn.write(b"int lo2\n")
tn.write(b"ip add 10.122.12.1 255.255.255.255\n")
tn.write(b"router ospf 100\n")
tn.write(b"network 0.0.0.0 255.255.255.255 area 0\n")
tn.write(b"do wr\n")
tn.write(b"end\n")
tn.write(b"exit\n")

print(tn.read_all().decode('ascii'))

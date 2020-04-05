#!/usr/bin/env python

from netmiko import ConnectHandler

iosv_l2_s1 = {
    'device_type': 'cisco_ios',
    'ip': '192.168.122.50',
    'username': 'Bharat',
    'password': 'cisco',
}

iosv_l2_s2 = {
    'device_type': 'cisco_ios',
    'ip': '192.168.122.51',
    'username': 'Bharat',
    'password': 'cisco',
}

iosv_l2_s3 = {
    'device_type': 'cisco_ios',
    'ip': '192.168.122.52',
    'username': 'Bharat',
    'password': 'cisco',
}

iosv_l2_s4 = {
    'device_type': 'cisco_ios',
    'ip': '192.168.122.53',
    'username': 'Bharat',
    'password': 'cisco',
}


iosv_l2_s5 = {
    'device_type': 'cisco_ios',
    'ip': '192.168.122.54',
    'username': 'Bharat',
    'password': 'cisco',
}

with open('core_sw_config') as f:
    lines = f.read().splitlines()
print(lines)

core_devices = [iosv_l2_s1, iosv_l2_s2]

for devices in core_devices:
    net_connect = ConnectHandler(**devices)
    output = net_connect.send_config_set(lines)
    print(output) 


with open('access_sw_config') as f:
    lines = f.read().splitlines()
print(lines)

access_devices = [iosv_l2_s3, iosv_l2_s4, iosv_l2_s5]

for devices in access_devices:
    net_connect = ConnectHandler(**devices)
    output = net_connect.send_config_set(lines)
    print(output) 

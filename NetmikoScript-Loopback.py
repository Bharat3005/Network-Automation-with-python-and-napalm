#!/usr/bin/env python

from netmiko import ConnectHandler

iosv_l2 = {
    'device_type': 'cisco_ios',
    'ip': '192.168.122.99',
    'username': 'Bharat',
    'password': 'cisco',
}

net_connect = ConnectHandler(**iosv_l2)
#net_connect.find_prompt()
output = net_connect.send_command('show ip int brief')

print(output)

config_commands = ['int loop 0', 'ip address 1.1.1.1 255.255.255.0']
output = net_connect.send_config_set(config_commands)
config_commands = ['int loop 1', 'ip address 1.1.2.1 255.255.255.0']
output = net_connect.send_config_set(config_commands)
config_commands = ['int loop 2', 'ip address 1.1.3.1 255.255.255.0']
output = net_connect.send_config_set(config_commands)
config_commands = ['int loop 3', 'ip address 1.1.4.1 255.255.255.0']
output = net_connect.send_config_set(config_commands)
config_commands = ['int loop 4', 'ip address 1.1.5.1 255.255.255.0']
output = net_connect.send_config_set(config_commands)
config_commands = ['int loop 5', 'ip address 1.1.6.1 255.255.255.0']
output = net_connect.send_config_set(config_commands)
config_commands = ['int loop 6', 'ip address 1.1.7.1 255.255.255.0']
output = net_connect.send_config_set(config_commands)
config_commands = ['int loop 7', 'ip address 1.1.8.1 255.255.255.0']
output = net_connect.send_config_set(config_commands)

print(output)

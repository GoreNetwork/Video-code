from build_conn_base import *

for ip in ips:
	net_connect = netmiko.ConnectHandler(device_type='cisco_ios', ip=ip, username=username, password=password)
	command = 'show ver'
	output = net_connect.send_command_expect(command)
	print (output)
from build_conn_base import *
from common_functions import *
from pprint import pprint

for ip in ips:

	net_connect = make_connection(ip, username, password)
	command = 'show interfaces'
	output = net_connect.send_command(command, use_textfsm=True)
	for port in output:
		if port['link_status'] == 'up':
			pprint (port)
	
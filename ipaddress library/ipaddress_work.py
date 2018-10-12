import ipaddress
from common_functions import *
from swap_wcm_snm_cider import *
from build_conn_base import *


for ip in ips:
	net_connect = make_connection(ip, username, password)
	show_run = send_command(net_connect,'show run')
	show_run = show_run.split('\n')
	interfaces = find_child_text (show_run, 'nterface')
	for interface in interfaces:
		for config_line in interface:
			if 'ip address' in config_line and 'no' not in config_line:
				tmp_ip, snm = get_ip (config_line)
				#print (tmp_ip, snm,interface[0])
				cider = snm_to_cider(snm)
				temp= tmp_ip+cider
				print (temp)
				subnet = ipaddress.ip_network(temp, strict = False)
				tmp_ip = ipaddress.ip_address(tmp_ip)
				print (subnet, tmp_ip,interface[0] )
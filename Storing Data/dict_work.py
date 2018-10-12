import ipaddress
from common_functions import *
from swap_wcm_snm_cider import *
from build_conn_base import *
from pprint import pprint

def pull_subnet_ip_int_from_device(net_connect):
	device = {}
	hostname = get_hostname (net_connect)
	device[hostname] ={}
	device[hostname]['interfaces']={}
	show_run = send_command(net_connect,'show run')
	show_run = show_run.split('\n')
	interfaces = find_child_text (show_run, 'nterface')
	for interface in interfaces:
		device[hostname]['interfaces'][interface[0]]={}
		device[hostname]['interfaces'][interface[0]]['ips'] =[]
		device[hostname]['interfaces'][interface[0]]['subnets'] =[]
		for config_line in interface:
			if 'ip address' in config_line and 'no' not in config_line:
				tmp_ip, snm = get_ip (config_line)
				#print (tmp_ip, snm,interface[0])
				cider = snm_to_cider(snm)
				temp= tmp_ip+cider

				subnet = ipaddress.ip_network(temp, strict = False)
				tmp_ip = ipaddress.ip_address(tmp_ip)
				device[hostname]['interfaces'][interface[0]]['ips'].append(tmp_ip)
				device[hostname]['interfaces'][interface[0]]['subnets'].append(subnet)
	return device

all_devices=[]
for ip in ips:
	print (ip)
	net_connect = make_connection(ip, username, password)
	if net_connect == None:
		print (ip, ' Did not work')
		continue
	all_devices.append(pull_subnet_ip_int_from_device(net_connect))

pprint (all_devices)


for device in all_devices:
	for host in device:
		if host =='R2':
			pprint(device[host]['interfaces']['interface FastEthernet0/0']['ips'])













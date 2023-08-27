import ipaddress
import csv

nets = ["atffk_guest", "atffk_wifi", "wired", "acs"]
prefixes = []
headers = ['Prefix', 'Description']
import_list = [headers]

base = ipaddress.ip_network('172.18.0.0/22')
l1 = list(base.subnets(prefixlen_diff=2)) #/24 nets

atffk_guest = str(l1[0])
atffk_wifi = str(l1[1])
    
infra = l1[2]

for line in l1:
    print(line)


infra_net = ipaddress.ip_network(infra)

wired = str(list(infra_net.subnets(prefixlen_diff=2))[0]) #/26 nets
acs = str(list(infra_net.subnets(prefixlen_diff=3))[2])  #/27 nets

print(wired)

for i in [atffk_guest, atffk_wifi, wired, acs]:
    prefixes.append(i)
    
for i in range(0, len(nets)):
    iter = [prefixes[i], nets[i]]
    import_list.append(iter)

print(import_list)

with open('01_result.csv', 'w', newline = '') as f:
    writer = csv.writer(f)
    writer.writerows(import_list)
    
"""
FILE CONTENT:

Prefix,Description
172.18.0.0/24,atffk_guest
172.18.1.0/24,atffk_wifi
172.18.2.0/26,wired
172.18.2.64/27,acs
"""

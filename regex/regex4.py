import re

output1 = '''Tunnel 1000, encap UDP
  From 1.1.1.2 to 2.2.2.2
  Peer tunnel 2000
  UDP source / dest ports: 6000/5000'''

output2 = '''Session 3000 in tunnel 1000
  Peer session 4000, tunnel 2000
  interface name: l2tpeth0
  offset 0, peer offset 0'''

output3 = '39: virbr0-nic: <BROADCAST,MULTICAST> mtu 1500 qdisc pfifo_fast master virbr0 state DOWN group default qlen 500'
output4 = 'link/ether 86:ed:82:1f:cb:46 brd ff:ff:ff:ff:ff:ff'
output5 = 'inet 192.168.2.27/25 brd 192.168.2.127 scope global br-mgmt'

regc1 = re.compile(r'(?s)Tunnel (\d+).*?From (\S+).*?to (\S+)\s+Peer tunnel (\d+).*?ports: (\d+)/(\d+)')

tunnels = regc1.findall(output1)

for tunnel in tunnels:
    print tunnel

regc2 = re.compile(r'(?s)Session (\d+).*?in tunnel (\d+)\s+Peer session (\d+).*?tunnel (\d+)\s+interface name: (\S+)')

sessions = regc2.findall(output2)

for session in sessions:
    print session

regex_result3 = re.search(r'(\d+): (\S+): \S+ mtu (\d+).*?state (\S+)', output3)

if regex_result3:
    print regex_result3.group(1), regex_result3.group(2), regex_result3.group(3), regex_result3.group(4)

regex_result4 = re.search(r'link/\S+ (\S+)', output4)

if regex_result4:
    print regex_result4.group(1)

regex_result5 = re.search(r'inet (\S+)', output5)

if regex_result5:
    print regex_result5.group(1)

output6 = 'eth3.13@eth3'
regex_result6 = re.search(r'(\S+)\.(\d+)@(\S+)', output6)
if regex_result6:
    print regex_result6.group(1), regex_result6.group(2), regex_result6.group(3)
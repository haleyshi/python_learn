import re

output1 = '''default via 192.168.2.20 dev br-mgmt  proto static\n
unreachable 169.254.169.254  scope host\n
default via 192.168.2.20 dev br-mgmt \n
192.168.0.0/24 dev br-fw-admin  proto kernel  scope link  src 192.168.0.21\n
192.168.2.0/25 dev br-mgmt  proto kernel  scope link  src 192.168.2.25\n
192.168.11.0/25 dev eth3.11  proto kernel  scope link  src 192.168.11.22\n
192.168.12.0/25 dev eth1.12  proto kernel  scope link  src 192.168.12.22\n
192.168.14.0/25 dev bond-migration  proto kernel  scope link  src 192.168.14.22\n
192.168.122.0/24 dev virbr0  proto kernel  scope link  src 192.168.122.1'''

regc_default = re.compile(r'default via \b(.*)\b dev ([^ ]*) ')
regc_other = re.compile(r'(\S+) dev (\S+)  proto \S+  scope \S+  src (\S+)')

def find(output):
    default_routes = regc_default.findall(output)

    print default_routes

    for default_route in default_routes:
        print default_route[0], default_route[1]

    other_routes = regc_other.findall(output)

    print other_routes

find(output1)
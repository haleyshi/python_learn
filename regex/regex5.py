import re

output = '''br-ex     Link encap:Ethernet  HWaddr fe:bf:32:7a:a5:4f
          inet addr:10.33.233.103  Bcast:10.33.233.127  Mask:255.255.255.224
          inet6 addr: fe80::fcbf:32ff:fe7a:a54f/64 Scope:Link
          UP BROADCAST RUNNING MULTICAST  MTU:1500  Metric:1
          RX packets:268902 errors:0 dropped:0 overruns:0 frame:0
          TX packets:129043 errors:0 dropped:0 overruns:0 carrier:0
          collisions:0 txqueuelen:0
          RX bytes:47670656 (47.6 MB)  TX bytes:15698916 (15.6 MB)'''

iface = {}

regex_result = re.search(r'(?s)RX packets:(\d+) errors:(\d+) dropped:(\d+) overruns:(\d+) frame:(\d+)', output)

if regex_result:
    iface["rx_packets"] = regex_result.group(1)
    iface["rx_errors"] = regex_result.group(2)
    iface["rx_dropped"] = regex_result.group(3)

regex_result = re.search(r'(?s)TX packets:(\d+) errors:(\d+) dropped:(\d+) overruns:(\d+) carrier:(\d+)', output)

if regex_result:
    iface["tx_packets"] = regex_result.group(1)
    iface["tx_errors"] = regex_result.group(2)
    iface["tx_dropped"] = regex_result.group(3)

regex_result = re.search(r'(?s)collisions:(\d+) txqueuelen:(\d+)', output)
if regex_result:
    iface["collisions"] = regex_result.group(1)

regex_result = re.search(r'(?s)RX bytes:(\d+).*?TX bytes:(\d+)', output)
if regex_result:
    iface["rx_bytes"] = regex_result.group(1)
    iface["tx_bytes"] = regex_result.group(2)

for key in iface.keys():
    print key, iface[key]
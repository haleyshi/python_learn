import re

output = " cookie=0x0, duration=790607.886s, table=0, n_packets=10203589, n_bytes=1062064984, idle_age=0, hard_age=65534, priority=3,in_port=1,dl_vlan=113 actions=mod_vlan_vid:33,NORMAL"

regex_result = re.search(r'(\S+)dl_vlan=(\d+) (\S+)', output)
if regex_result:
    print regex_result.group(2)
import re

output = 'vethoj70Wv Link encap:Ethernet  HWaddr FE:8E:D8:9B:5A:D8 '

regex_result = re.search(r'(?s)HWaddr FE:(\S+)', output)
if regex_result:
    print regex_result.group(1)
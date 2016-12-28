import re

output = '''bridge name     bridge id               STP enabled     interfaces
virbr0          8000.000000000000       yes      eth0
                                                 eth1'''

bridges = []
tuples = output.split('\n')
del tuples[0]

bridge = None

for tuple in tuples:
    tuple = tuple.strip()
    fields = re.split(r'\s+', tuple)

    if len(fields) == 1:
        if bridge is not None:
            if bridge.has_key("interfaces"):
                interface = {"name": fields[0]}
                bridge["interfaces"].append(interface)
    if len(fields) >= 3:
        bridge = {}
        bridge["name"] = fields[0]
        bridge["id"] = fields[1]

        if len(fields) == 4:
            bridge["interfaces"] = []
            interface = {"name": fields[3]}
            bridge["interfaces"].append(interface)

        bridges.append(bridge)

print bridges


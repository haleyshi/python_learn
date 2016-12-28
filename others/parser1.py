import commands
import re
import json

server_ip = "10.0.91.1"
user_pw = "ccmadm:ccmadmin123"


def getCables():
    cmd = "curl -k -v -X GET -u '%s' -H 'Content-Type: application/json' https://%s/rest/v0/Cables/" % (user_pw, server_ip)

    status, output = commands.getstatusoutput(cmd)

    if status == 0:
        regc = re.compile(r'\S?@odata.id" : "/rest/v0/Cables/(\S+)"')
        cables = regc.findall(output)

        return cables
    else:
        print cmd, status, output
        return None

def getCableEndpoints(cable_id):
    cmd = "curl -k -v -X GET -u '%s' -H 'Content-Type: application/json' https://%s/rest/v0/Cables/%s/CableEndpoints" % (user_pw, server_ip, cable_id)

    status, output = commands.getstatusoutput(cmd)

    if status == 0:
        regc = re.compile(r'\S+/CableEndpoints/(\S+)"')
        endpoints = regc.findall(output)

        return endpoints
    else:
        print cmd, status, output
        return None

def setCableEndpointDetails(cableDetails, cable_id, endpoint_id):
    cmd = "curl -k -v -X GET -u '%s' -H 'Content-Type: application/json' https://%s/rest/v0/Cables/%s/CableEndpoints/%s" % (user_pw, server_ip, cable_id, endpoint_id)

    status, output = commands.getstatusoutput(cmd)

    if status == 0:
        regex_result = re.search(r'\S+EthernetInterfaceID" : "(\S+)"', output)
        if regex_result:
            cableDetails["EthernetInterfaceID"] = regex_result.group(1)
            regex_result = re.search(r'\S+ComputerSystemID" : "(\S+)"', output)
            if regex_result:
                cableDetails["ComputerSystemID"] = regex_result.group(1)
        else:
            regex_result = re.search(r'\S+SwitchID" : "(\S+)"', output)
            if regex_result:
                cableDetails["SwitchID"] = regex_result.group(1)
                regex_result = re.search(r'\S+PortID" : "(\S+)"', output)
                if regex_result:
                    cableDetails["PortID"] = regex_result.group(1)
    else:
        print cmd, status, output

def getCableDetails():
    cables = getCables()
    if cables is None:
        return None

    cableDetails = []

    for cable in cables:
        print cable
        cableDetail = {}
        cableDetail["ID"] = cable
        endpoints = getCableEndpoints(cable)

        if endpoints is not None:
            for endpoint in endpoints:
                setCableEndpointDetails(cableDetail, cable, endpoint)

        cableDetails.append(cableDetail)

    return cableDetails

if __name__ == '__main__':
    print json.dumps(getCableDetails())



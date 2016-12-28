from neutronclient.v2_0 import client as neutronClient
import json

creds = {}
creds['username'] = 'admin'
creds['password'] = 'nova'
creds['tenant_name'] = 'demo'
creds['auth_url'] = 'http://192.168.56.101:5000/v2.0'
keystone_creds = {'username':creds['username'], 'password':creds['password'], 'auth_url':creds['auth_url'], 'tenant_name':creds['tenant_name']}


def listNets():
    try:
        client = neutronClient.Client(**keystone_creds)

        networks = client.list_networks(search_opts={'all': True})

        print json.dumps(networks, sort_keys=True, indent=4, separators=(',', ': '))
    except Exception as e:
        print str(type(e)) + '        ' + str(e)


def listSubNets():
    try:
        client = neutronClient.Client(**keystone_creds)

        subnets = client.list_subnets(search_opts={'all': True})

        print json.dumps(subnets, sort_keys=True, indent=4, separators=(',', ': '))
    except Exception as e:
        print str(type(e)) + '        ' + str(e)


def listPorts():
    try:
        client = neutronClient.Client(**keystone_creds)

        ports = client.list_ports(search_opts={'all': True})

        print json.dumps(ports, sort_keys=True, indent=4, separators=(',', ': '))
    except Exception as e:
        print str(type(e)) + '        ' + str(e)


def listRouters():
    try:
        client = neutronClient.Client(**keystone_creds)

        routers = client.list_routers(search_opts={'all': True})

        print json.dumps(routers, sort_keys=True, indent=4, separators=(',', ': '))
    except Exception as e:
        print str(type(e)) + '        ' + str(e)


def listAgents():
    try:
        client = neutronClient.Client(**keystone_creds)

        agents = client.list_agents(search_opts={'all': True})

        print json.dumps(agents, sort_keys=True, indent=4, separators=(',', ': '))
    except Exception as e:
        print str(type(e)) + '        ' + str(e)


def listSecurityGroups():
    try:
        client = neutronClient.Client(**keystone_creds)

        sec_grps = client.list_security_groups(search_opts={'all': True})

        print json.dumps(sec_grps, sort_keys=True, indent=4, separators=(',', ': '))
    except Exception as e:
        print str(type(e)) + '        ' + str(e)


listNets()
print
listSubNets()
print
listPorts()
print
listRouters()
print
listAgents()
print
listSecurityGroups()

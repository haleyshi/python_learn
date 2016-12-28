from novaclient import client as novaClient
from prettytable import PrettyTable

creds = {}
creds['username'] = 'admin'
creds['password'] = 'nova'
creds['tenant_name'] = 'demo'
creds['auth_url'] = 'http://192.168.56.101:5000/v2.0'
nova_creds = {'username':creds['username'], 'api_key':creds['password'], 'auth_url':creds['auth_url'], 'project_id':creds['tenant_name']}

def listVMs():
    try:
        client = novaClient.Client("2", **nova_creds)
        vms = client.servers.list(search_opts={'all_tenants': 1})

        table = PrettyTable(["ID", "NAME", "STATUS", "HOST_ID", "HOST", "IMAGE_ID", "VOLUMES_ATTACHED", "FLAVOR_ID", "NETWORKS", "AVAILABILITY_ZONE", "INSTANCE_NAME"])
        table.align["NAME"] = "l"  # Left align names
        table.padding_width = 1  # One space between column edges and contents (default)

        for vm in vms:
            if vm.HUMAN_ID:
                name = getattr(vm, vm.NAME_ATTR)
            else:
                name = ""

            if vm.image:
                imageId = vm.image['id']
            else:
                imageId = ""

            table.add_row([vm.id, name, vm.status, vm.hostId, getattr(vm, "OS-EXT-SRV-ATTR:host"), imageId, getattr(vm,"os-extended-volumes:volumes_attached"), vm.flavor['id'], vm.addresses, getattr(vm,"OS-EXT-AZ:availability_zone"), getattr(vm, "OS-EXT-SRV-ATTR:instance_name")])

        print table
    except Exception as e:
        print str(type(e)) + '        ' + str(e)


def listHosts():
    try:
        client = novaClient.Client("2", **nova_creds)
        hosts = client.hypervisors.list()

        table = PrettyTable(["IP", "HOSTNAME", "SERVICE"])
        table.padding_width = 1  # One space between column edges and contents (default)

        for host in hosts:
            table.add_row([host.host_ip, host.hypervisor_hostname, host.service["host"]])

        print table

    except Exception as e:
        print str(type(e)) + '        ' + str(e)


def listImages():
    try:
        client = novaClient.Client("2", **nova_creds)
        images = client.images.list()

        table = PrettyTable(["ID", "NAME"])
        table.align["NAME"] = "l"  # Left align names
        table.padding_width = 1  # One space between column edges and contents (default)

        for image in images:
            table.add_row([image.id, image.name])

        print table

    except Exception as e:
        print str(type(e)) + '        ' + str(e)


def listFlavors():
    try:
        client = novaClient.Client("2", **nova_creds)
        flavors = client.flavors.list()

        table = PrettyTable(["ID", "NAME", "VCPUs", "RAM", "DISK"])
        table.align["NAME"] = "l"  # Left align names
        table.padding_width = 1  # One space between column edges and contents (default)

        for flavor in flavors:
            table.add_row([flavor.id, flavor.name, flavor.vcpus, flavor.ram, flavor.disk])

        print table

    except Exception as e:
        print str(type(e)) + '        ' + str(e)


def createVM(name, image, flavor, network):
    try:
        client = novaClient.Client("2", **nova_creds)
        server = client.servers.create(name=name, flavor=flavor, image=image, nics=[{'net-id': network}])
        print "Create VM: %s" % name
    except Exception as e:
        print str(type(e)) + '        ' + str(e)

listVMs()
print
listHosts()
print
listFlavors()
print
listImages()
print
try:
    client = novaClient.Client("2", **nova_creds)
    flavor = client.flavors.find(name="m1.tiny")
    network = client.networks.find(label="private")
    image = client.images.find(name="cirros-0.3.2-x86_64-uec")
    createVM("test", image.id, flavor.id, network.id)
except Exception as e:
    print str(type(e)) + '        ' + str(e)

print

listVMs()

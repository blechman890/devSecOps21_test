network_device = {'device': {'hostname': 'router1', 'interface': {'eth0': 'up', 'eth1': 'down'}}}
status = network_device['device']['interface'].get('eth0', 'status')
print(status)
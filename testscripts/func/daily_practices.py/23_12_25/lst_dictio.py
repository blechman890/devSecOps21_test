servers = [
    {'name': 'web1', 'cpu': 45, 'memory': 60},
    {'name': 'db01', 'cpu': 85, 'memory': 70},
    {'name': 'app1', 'cpu': 92, 'memory': 88},
    {'name': 'web2', 'cpu': 55, 'memory': 65}
]
dict_srvrs = [server for server in servers if server['cpu'] > 80]
print(f"Servers with high CPU: {dict_srvrs}")
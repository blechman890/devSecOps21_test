services = ['HTTP', 'HTTPS', 'SSH', 'FTP']
ports = [80, 443, 22, 21]
dict_service_to_port = dict(zip(services, ports))
print(f"{dict_service_to_port}")
ports = [22, 80, 443, 8080, 3306, 5432, 8443, 21,25]
filtered_ports = [port for port in ports if port > 1024]
print(f'The requested ports are: {filtered_ports}')
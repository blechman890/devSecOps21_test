ports = [22, 80, 443, 8080, 5432, 8443, 21, 25]
high_ports = [port for port in ports if port > 1024]
print(f"\nPorts above 1024 are: {high_ports}")
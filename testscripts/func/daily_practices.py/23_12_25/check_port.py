def check_port(port, protocol="TCP"):
    return f"Checking {protocol} \nport {port}"
# print(check_port(80))
print(check_port(53, 'UDP'))
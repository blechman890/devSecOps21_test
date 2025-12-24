def update_connection(protocol, port, service):
    protocol, port, service = connection_tuple
    return (protocol, port, service)

"""
connection = ('tcp', 443, 'https')
print(f"Original connection details: {connection}")
# connection[1] = 80
new_connection = ('udp', 80, connection[2])
print(f"\nNew connection details: {new_connection}")
"""
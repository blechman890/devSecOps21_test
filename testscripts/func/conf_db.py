def conf_db(host, *, port=5432, username='admin', timeout=30):
    config = f"Connecting to {host} on port {port} as user {username} with timeout {timeout}s"
    print(f"Database Configuration: {config}")

conf_db('localhost')
conf_db('prod-db-server', port=54320)
conf_db('db-server-2', username='dbadmin', timeout=30)
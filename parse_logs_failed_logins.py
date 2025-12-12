print("\nParse Logs - Failed Logins")
def failed_logins(log_lines):
    failed_attempts = {} # Dictionary to store failed login attempts
    for line in log_lines: # Process each log line.
        if "Failed login" in line:
# Split the line into parts # Example - "2024-06-01 12:00:00 - Failed login for user 'admin' from IP
            parts = line.split()
            # IP is the 3rd element (index 2)
            ip_address = parts [2]
            # Increment counter for IP address. If IP not in dict, start at 0, then add 1.
            if ip_address in failed_attempts:
                failed_attempts[ip_address] += 1
            else:
                failed_attempts[ip_address] = 1
    return failed_attempts
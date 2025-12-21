log_entries = [
    "INFO: System started",
    "ERROR: Connection timeout",
    "WARNING: High memory usage",
    "INFO: User logged in",
    "ERROR: Authentication failed"
]
levels = ['ERROR', 'WARNING']
filtered_logs = [log for log in log_entries if any(level in log for level in levels)]
print(f"Logs: {filtered_logs}")
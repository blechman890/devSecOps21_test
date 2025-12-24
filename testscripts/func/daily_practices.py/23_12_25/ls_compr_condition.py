logs = [
    'INFO: System is up',
    'ERROR: Connection timeout',
    'WARNING: High memory usage',
    'CRITICAL: The dev/ Disk is full',
    'INFO: User ilya is logged-in',
    'CRITICAL: Snapshot failed'
]

filtered_logs = [log for log in logs if 'ERROR' in log or 'CRITICAL' in log]
print(f"Filtered logs: {filtered_logs}")
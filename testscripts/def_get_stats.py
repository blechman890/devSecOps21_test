def get_stats():
    cpu = 45
    memory = 70
    disk = 80
    return cpu, memory, disk
c, m, d = get_stats()
print(f"CPU Usage: {c}%, Memory Usage: {m}%, Disk Usage: {d}%")
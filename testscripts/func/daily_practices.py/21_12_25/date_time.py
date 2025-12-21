from datetime import datetime

def timestamp():
    return datetime.now().strftime("%Y-%m-%d %H:%M:%S")

print(f"Current timestamp: {timestamp()}")
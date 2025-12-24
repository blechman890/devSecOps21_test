def is_valid_ipv4(ip):
    parts = ip.split('.')
    if len(parts) !=4:
        return False
    for part in parts:
        if not part.isdigit() or len(part) == 0:
            return False
    
    num=int(part)

    if num < 0 or num > 255:
        return False
    
    if part != str(num):
        return False
    
    return True
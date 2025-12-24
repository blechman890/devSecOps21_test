def pass_val(password):
    has_min_length = len(password) >= 8; has_digit = any(char.isdigit() for char in password)
    return has_min_length and has_digit
print(f"Password validateion('password'): {pass_val('password')}")
print(f"Password validateion('1password'): {pass_val('1password')}")

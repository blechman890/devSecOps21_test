def pass_val(password):
    has_min_length = len(password) >= 8; has_digit = any(char.isdigit() for char in password)
    return has_min_length and has_digit
print(f"pass_val('pass123'): {pass_val('pass123')}")
print(f"pass_val('password123'): {pass_val('password123')}")

print("\nPassword strength check function")
def is_pass_strong(password):
    if len(password) < 8:
        return False
    print("The password must be at least 8 characters long.")
    
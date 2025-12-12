print("\nPassword strength check function")
def is_pass_strong(password):
    if len(password) < 8: # Minimum length check
        return False
    print("The password must be at least 8 characters long.")
    # Initialize criteria flags
    has_upper = False
    has_lower = False
    has_digit = False
    has_special = False
    # Define special characters
    special_characters = "!@#$%^&*"
    for char in password: # Check each character in the password
        if char.isupper(): # Check for uppercase letters
            has_upper = True
        elif char.islower(): # Check for lowercase letters
            has_lower = True
        elif char.isdigit(): # Check for digits
            has_digit = True
        elif char in special_characters: # Check for special characters
            has_special = True

    # Return True only if all criteria are met
    return has_upper and has_lower and has_digit and has_special


# Test the function with different passwords
print("\nTEST CASES FOR PASSWORD STRENGTH CHECK FUNCTION")
test_passwords = [
    ("weak", False),
    ("P@ssword1!", True), # Has uppercase, lowercase, digit, special char.
    ("password1" , False), # Missing uppercase and special char.
    ("PASSWORD1!", False), # Missing lowercase char.
    ("Password1!", False), # Missing special char.
    ("Pass1!", False), # Less than 8 characters.
    ("Password!", False)  # Missing digit.
]
for pwd, expected in test_passwords:
    result = is_pass_strong(pwd)
    status = "PASS" if result == expected else "FAIL"
    print(f"{status} '{pwd}'; {result} (expected {expected})")

print("\nKEY CONCEPTS:")
print(" - String methods: len(), isupper(), islower(), isdigit()")
print(" - Boolean logic: and, or")
print(" - Loop through string characters")
print(" - Membership testing with 'in'")
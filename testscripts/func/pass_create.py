def pass_create(username, /, password=None, *, min_length=8, req_special_char=True):
    if password == "" or password is None:
        raise ValueError("Password cannot be empty")
    if len(password) < min_length:
        raise ValueError(f"Password must be at least {min_length} characters long")
    if req_special_char:
        special_characters = "!@#$%^&*()-_=+[]{}|;:'\",.<>?/"
        has_special = any(char in special_characters for char in password)
        if not has_special:
            raise ValueError("Password must contain at least one special character")
    # print(f"\nUser '{username}' created. \nPassword creation 'Success'.")
    success_message = f"\nUser '{username}' created successfully with a secure password."
    # print(f"\n {success_message}")

    return {
    "success": True,
    "username": username,
    "message": success_message,
    }
pass_create("ilya", password="P@ssw0rd!")
# pass_create("Ayush", password= "password123!")
# pass_create("Moshe", password="")
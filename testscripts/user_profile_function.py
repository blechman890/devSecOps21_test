import profile


def user_prof(username, age="9mill", location="Cybertron", is_active=True):
    profile = {
        "username": username,
        "age": age,
        "location": location,
        "is_active": is_active
    }
    return profile
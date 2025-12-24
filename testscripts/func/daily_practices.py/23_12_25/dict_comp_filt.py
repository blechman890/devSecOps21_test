failed_logins = {'alice': 2, 'bob': 5, 'charlie': 8, 'diana': 1, 'ilya': 4}
new_filt_logins = {k: v for k, v in failed_logins.items() if v > 3}
print(f"New dict: {new_filt_logins}")
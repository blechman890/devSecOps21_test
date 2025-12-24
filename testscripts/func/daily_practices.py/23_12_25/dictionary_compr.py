user_data = [('ilya','active'), ('moshe','active'), ('charlie', 'deactivated'), ('moti', 'suspended')]
filtered_list = {user: status for user, status in user_data if status =='active'}
print(f"Active users: {filtered_list}")
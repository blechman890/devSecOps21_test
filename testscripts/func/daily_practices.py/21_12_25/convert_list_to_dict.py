user_data = [('alice','active'),('bob','inactive'),('charlie','active'),('dave','suspended')]
active_users = {user: status for user, status in user_data if status == 'active'}
print(f"Active users: {active_users}")
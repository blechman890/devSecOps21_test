login_counts = {"alice": 5, "ilya": 10, "moshe": 2}
for user in login_counts:
    login_counts[user] += 1
login_counts['david'] = 1
print(f'Updated login counts: {login_counts}')
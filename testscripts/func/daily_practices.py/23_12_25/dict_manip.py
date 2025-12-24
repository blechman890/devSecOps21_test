logins = {'alice': 5, 'ilya':10, 'moshe': 15, 'jacob': 13}
for user in logins:
    logins[user] += 1
logins['yaakov'] = 1
print(f"Updated logins: {logins}")
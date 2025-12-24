log_entry = '2025-12-23 14:30:00 ERROR Failed authentication'
# Step 1 is to split the entry into parts
parts = log_entry.split()

# Step 2: Extract the date, time, level and message

date = parts[0]     # 2025-12-23
time = parts[1]     # 14:30:00
level = parts[2]    # "ERROR"        
message = " ".join(parts[3:]) # Take the items and combine(join) them between index 3 up until the last one [3:]
# which means in this case "Failed authentication"

# Step 3: Reconstruct the log entry
formated_log = f"[{level}] {date} {time}: {message}"

# Output the result

print(formated_log)

# print(parts)
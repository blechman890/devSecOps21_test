rules1 = {"rule1": "allow", "rule2": "deny"}
rules2 = {"rule2": "allow", "rule3": "deny"}

# Method 1: update()

merged = rules1.copy()
merged.update(rules2)
print(f"Merged rules: {merged}")

# Method 2: unpacking

merged2= {**rules1, **rules2}
print(f"Merged rules method 2: {merged2}")
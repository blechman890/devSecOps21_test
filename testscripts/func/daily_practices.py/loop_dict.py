for nums in range(1,11):
    if nums % 2 ==0:
        print(nums, end=" ")
print()

servers = { 
    "web1": "1.2.3.4.",
    "prod2": "192.123.12.34",
    "api3": "170.23.45.1"
    }
print(f"Keys: {list(servers.keys())}")
print(f"Values: {list(servers.values())}")
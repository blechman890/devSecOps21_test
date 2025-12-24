all_ports = [22, 80, 443, 1080, 3000, 8080, 8000, 9000, 50000, 60000]
new_list = [p for p in all_ports if 1024 <= p <= 49151 and p % 10 == 0]
# print(new_list)
print(f"Divisible by 10: {new_list}")
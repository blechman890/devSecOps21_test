black_list = ['192.168.1.100', '10.0.0.50', '172.16.0.200']
white_list = ['192.168.1.100', '10.0.0.25', '172.16.0.150']
b_set = set(black_list)
w_set = set(white_list)
print(f"Union set: {b_set & w_set} \nOnly in the B set: {b_set - w_set} \nUniques: {b_set | w_set}")
# print(f"Only in black list: {b_set - w_set}")
# print(f"Uniques : {b_set | w_set}")

def base_exp(num, exp,/): # This (/) means only positional arguments are allowed before the /.
    print(num ** exp)
# base_exp(2, 3) # 2 raised to the power of 3
# base_exp(num=5, exp=4) # This will cause an error because num is a keyword argument before /
# base_exp(exp=2, num=10) # This will also cause an error for the same reason
base_exp(7, exp=3)  # This will also fail because exp=3 is a keyword argument after /
def odd_nums(a,b):
    return[num for num in range(a, b+1) if num %2 !=0] 
print(odd_nums(1, 21))
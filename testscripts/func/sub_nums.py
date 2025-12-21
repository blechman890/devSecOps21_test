# Best func
# Accepts all needed data as parameters
# Does one thing and does it well

something = 5

def sub_nums(a, b):
    return a - b
print("sub_nums {a - b}")
# Not so good func
# def sub_somthing(num):  # Better if something was a parameter
#    print(num - something)
# sub_somthing(12)


# def many_params(a, b, c, /, d, e, f, *, g, h, i):
#    print(a, b, c, d, e, f, g, h, i)

# many_params(a=1, b=2, c=3, 4, 5, 6, g=7, h=8, i=9) # Wrong 

# Params with * and **

def all_pars(a, b, *c, **d):
    print(a, b, c)

all_pars(1, 2, 3, 4, 5, 6, a=3, d=4) # c will be (3, 4, 5, 6). d will be {'a': 3, 'd': 4}

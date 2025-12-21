def add_nums(a,b):  # a, b are parameters
    print(a + b)   # Function body (adds two numbers).

add_nums(3,5)  # 3, 5 are arguments

x, y = 10, 20 # Here I am defining variables. x, y are assigned arguments.
add_nums(x,y) # Here I am passing variables as arguments.

q, v = 7, 14
add_nums(q, v) # q, v are assigned arguments.

# add_nums is a name of OBJECT and the type of this object is FUNCTION.
# That means, I can add the name of a function to a list and then call for it.

lst2 = [6.9, ('a',35, -4), None, add_nums, -99, 'bye']

# calling for the add_nums() by using the lst2: lst2[3](any_two, nums)

d1 = {'add':add_nums, 'sub':'sub'}

def sub_func(x, y):
    return x-y

d1['sub'] = sub_func
# I can also call for the sub_func from dictionary: d1['sub'](any_two, nums)
# In general, I can create different pointers to point at the same function.
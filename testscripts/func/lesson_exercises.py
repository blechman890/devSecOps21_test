# def func_1(num1, num2, /, *other_nums, **args):
#    print(num1,num2, other_nums, args)
# func_1(1,2,3,4,5,'bla','moshe', False, name='Tally')

# def smart_func(**kwargs):
#    print(kwargs)
# smart_func(name='Moshe', last_name='Bush', age=55, hight=190, more=(1,2,3))
t5=[(2,8,6),(4,5,77),(6,6,6),(3,9,-66)]

def triple(triple):
    return triple[2]

sorted(t5, key=triple)


# def pair_eval(pair): # Function that will sort 2 parameters
#    return pair[1] # It will sort based on the SECOND value 
# sorted(t5, key=pair_eval)
# f1 = lambda a, b: a+b
# print(f1(4,5))


# print((lambda x, y: x*y)(4,5)) # Lambda is an edhoc function that will do what is needed and then disappear.

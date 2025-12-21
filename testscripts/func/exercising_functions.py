# def say_hello():
#    print("Hello World")

# print("\nCalling: say_hello()")
# say_hello()
# print()

# def greet(name):
#    print(f"Hello {name}")
# greet('Ilya')

# def add(a, b):
#    result = a + b
#    return result
# result = add(5, 6)
# print(f"\nResult: {result}")

# def add_user(username, email):
#    return f"\nUser: {username}, \nEmail: {email}"
# print(f"{add_user('Ilya', 'ilya@test.com')}")

# def employee_card(username, role=None, active=True):
#    return f"\nEmployee: {username}, \nRole: {role}, \nActive: {active}"
# print(f"{employee_card('Sys Admin')}")

# def book_flight(pass_name, destination, date, seat_class='economy'):
#    return f"\nName{pass_name} \nTo {destination} \nOn {date} \nClass {seat_class}"
# print(f"{book_flight('Ilya', 'Paris', 'Today','business')}")

# def add_nums(a, b, c=10):
#    return a+b+c
# result = add_nums(3, 5)
# result = add_nums(a=4, b=5)
# result = add_nums(4, b=7)
# result3 = add_nums(a=4, 9) # This is wrong
# result = add_nums(3, 4, 5)


# def many_params(a, b, c, /, d, e, f, *, g, h, i):
#    print(a, b, c, d, e, f, g, h, i)
# many_params(a=1, b=2, c=3, d=4, e=5, f=6, g=7, h=8, i=9) # Wrong
# many_params(1, 2, 3, 4, 5, 6, 7, 8, 9) # Wrong

# many_params(1, 2, 3, d=4, e=5, f=6, g=7, h=8, i=9) # OK

# def all_pars(a, b, *c):
#    print(a,b,c)
# all_pars(3,4)
# all_pars(3,4,5)
# all_pars(3,4,5,6,7,8,9)

# def add_all(*nums):
#    sum=0
#    for num in nums:
#        sum += num
#    return sum
# print(add_all(1,2,3,4,5,6,7,8,9)) # OK
# print(add_all(1,2,3,4,5,6,7,8,a=9)) # NOT OK because it accepts ONLY POSITIONAL.

# def show_all(a, b, **args):
#    print(a,b,args)
# show_all(3,4, name='Ilya', last_name='Blechman', age=42)

# def show_max(a,b,*ars,**fields):
#    print(a,b,ars,fields)
# show_max(2,3,4,5,name='Ilya',last_name='Blechman', age=42)
list = [1,2,3,4,5,6,7,8,9] # This is list

# Instead of doing the above, we can create am empty list and use a loop command (for)
# to append to it what we need. 
list = []
for i in range(10):
    list.append(i*3)
print(list)

# We can simlify it even further by creating an expression that will create a list
# list2=[i for i in range(10)] # The first i is the one that creates the basis of the list
list3=[i*3 for i in range(10)] # We have added the *3 so that the range numbers will multiply by 3.
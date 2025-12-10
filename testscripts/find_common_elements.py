print('\nExercise 17: ')
list1 = input(print('Enter numbers for list1 separated by spaces: ')).split()
list2 = input(print("Enter numbers for list2 separated by spaces: ")).split()
common_elements = []
for element in list1:
    if element in list2:
        common_elements.append(element)
print(common_elements)  # Output: [4, 5]
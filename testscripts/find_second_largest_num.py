print('\nExercise 20: ')
numbers = [45, 23, 67, 89, 12, 90, 34]
first_largest = 0
second_largest = 0
for num in numbers:
    if num > first_largest:
        second_largest = first_largest
        first_largest = num
    elif num > second_largest and num < first_largest:
        second_largest = num
print("The second largest number is:", second_largest)


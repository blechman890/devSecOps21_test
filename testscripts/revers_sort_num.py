print('\nExerscise 21: ')
numbers = [45, 23, 67, 89, 12, 90, 34]
unique_numbers = list(set(numbers))
unique_numbers.sort(reverse=True)
print(f"Second largest number:{unique_numbers[1]}")
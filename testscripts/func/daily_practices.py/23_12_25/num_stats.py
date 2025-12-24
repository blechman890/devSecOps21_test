def analyze_nums(numbers):
    for num in numbers:
        total = sum(numbers)
        average = total // len(numbers)
        return(total, average, min(numbers), max(numbers))

data = [7, 25, 44, 6]
result = analyze_nums(data)
print(f'Sum: {result[0]}, \nAVG: {result[1]}, \nSmallest: {result[2]}, \nLargest: {result[3]}')
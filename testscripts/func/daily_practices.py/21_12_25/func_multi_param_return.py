def stats(numbers):
    total = sum(numbers)
    avg = total // len(numbers)
    return(total, avg, min(numbers), max(numbers))

data = [3, 55, -7, 0, 8]
result = stats(data)
print(f"\nSum: {result[0]}, \nAvg: {result[1]}, \nMin: {result[2]}, \nMax: {result[3]}")
"""
def calculate_risk_score(*risk_values):
    if len(risk_values) == 0:
        return 0
    avg = sum(risk_values) / len(risk_values)
    return avg
average_risk = calculate_risk_score(-30, 50, 70)
print(f"The average score of risk is: {average_risk}")
"""

def calc_risk_avg(*args):
    if not args:
        return 0
    total = 0 # the sum of all numbers
    count = 0 # how many numbers were in args
    for number in args:
        total += number # add each number to total
        count += 1      # Increment count
    avg = total / count
    return avg
average_risk = calc_risk_avg(30, 50, 70)
print("Average risk:", average_risk)
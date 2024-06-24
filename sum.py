def sum_of_list(numbers):
    total = 0
    for number in numbers:
        total += number
    return total
numbers = [1, 2, 3, 4, 5]
print("Sum of numbers:", sum_of_list(numbers))

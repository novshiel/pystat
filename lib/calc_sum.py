# Although there is a sum function in Python, this is an exercise
# to manually show how to calculate a sum given a list of numbers.

def calc_sum(numbers):
    sum = 0

    for num in numbers:
        sum += num

    return sum

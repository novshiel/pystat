def get_numbers_from_user():
    input_string = input('Enter a series of numbers separated by a space: ')
    num_strings = input_string.split()

    nums = []

    for num_str in num_strings:
        nums.append(float(num_str))

    return nums

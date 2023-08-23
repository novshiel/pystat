from lib.add_two import add_two
from lib.calc_sum import calc_sum
from lib.get_numbers_from_user import get_numbers_from_user
from lib.calc_mean import calc_mean

nums = get_numbers_from_user()
# print(nums)

# Test add_two function.
# Expected output: 5
# print(add_two(2, 3))

# numbers = [1, 2, 3, 4, 5]
# print(numbers)

print('Sum of numbers: ', calc_sum(nums))
print('Mean of numbers: ', calc_mean(nums))
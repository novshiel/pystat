from inspect import currentframe
from lib.add_two import add_two

def test_add_two_positive_numbers():
    test_name = currentframe().f_code.co_name
    result = add_two(2, 3)
    if result == 5:
        print(test_name + ": passed")
    else:
        print(test_name + ": failed")

def test_add_two_negative_numbers():
    test_name = currentframe().f_code.co_name
    result = add_two(-2, -3)
    if result == -5:
        print(test_name + ": passed")
    else:
        print(test_name + ": failed")

def test_add_two():
    test_add_two_positive_numbers()
    test_add_two_negative_numbers()

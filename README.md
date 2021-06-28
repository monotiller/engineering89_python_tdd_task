# Test Driven Development Task
Task requirements:
- create a test to check is the number divisible/remainder 0 if True pass the test if False fail
- create a class and method to write code to pass the test
- create a test case to calculate % and code to pass the test
- create a test to check if the given values are positive 
- create a method in the class to pass the test

## Tests
- `calc_test.py` - This is where the tests are stored
- `complicated_calc.py` this is where the calculator is stored
### `test_divisible`
Tests if the modulous of the two numbers is 0. The calculator returns a `True` or `False` statement depending on the answer. Here, we're passing in `2` and `10` and we are expecting it to `False` because  the answer is 3

### `test_modulous`
Tests the modulous of two numbers and returns that value. We are passing in `2` and `2` and we are expecting `0`.

### `test_positive`
Test if the values passed in are positive. The calculator returns `True` if they are positive and `False` if they are not. Since 0 is neither positive or negative, the calculator will only count values 1 and above as positive
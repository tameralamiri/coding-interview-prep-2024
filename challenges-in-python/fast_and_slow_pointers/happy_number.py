# Solving the "Happy Number" Challenge
# Challenge Description:
# A "happy number" is defined as a number which eventually reaches 1 
# when replaced by the sum of the square of each digit. 
# If this process results in an endless cycle of numbers which does not include 1, 
# then the number is not happy.

# Approach:
# Use the Fast and Slow pointer technique to determine whether the cycle ends at 1 
# (happy number) or enters a loop other than 1 (not a happy number).

# Algorithm:
# 1. Initialize slow and fast pointers to the number n.
# 2. Loop until slow and fast pointers meet.
# 3. In each iteration, do the following:
#     a. Set slow to the sum of the square of each digit in slow.
#     b. Set fast to the sum of the square of each digit in fast.
#     c. Set fast to the sum of the square of each digit in fast again.
# 4. If slow is equal to 1, then the number is happy.
# 5. Otherwise, the number is not happy.

# Implementation:
def find_square_sum(num: int) -> int:
    _sum = 0
    while num > 0:
        digit = num % 10 # get the last digit
        _sum += digit * digit # add square of the digit to the sum
        num //= 10 # move to the next digit
    return _sum

def is_happy_number(num: int) -> bool:
    slow, fast = num, num
    while True:
        slow = find_square_sum(slow) # move one step
        fast = find_square_sum(find_square_sum(fast)) # move two steps
        if slow == fast: # found the cycle
            break
    return slow == 1 # Check if the cycle is stuck on the number '1'

assert(is_happy_number(23))
assert(is_happy_number(12))
assert(is_happy_number(7))
assert not (is_happy_number(4))
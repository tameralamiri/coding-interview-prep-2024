# Map(function, iterable) Function:
# The function is applied to each item of the iterable, one at a time, in order.
# The result is a map object, which is an iterator that yields the results of applying the function to each item of the iterable.
# Since the result is an iterator, you often need to convert it to a list or another iterable type to see the results or iterate over them.

# Example 1: Using map() with a list
def square(x):
    return x**2

numbers = [1, 2, 3, 4, 5]
squared = map(square, numbers)
print(list(squared)) # Output: [1, 4, 9, 16, 25]

# Example 2: Using map() with a lambda function
numbers = [1, 2, 3, 4, 5]
squared = map(lambda x: x**2, numbers)
print(list(squared)) # Output: [1, 4, 9, 16, 25]

# Example 3: Using map() with multiple iterables
def add(x, y):
    return x + y

numbers1 = [1, 2, 3]
numbers2 = [4, 5, 6]
added = map(add, numbers1, numbers2)
print(list(added)) # Output: [5, 7, 9]
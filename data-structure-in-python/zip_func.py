# Zip():
# zip() takes one or more iterables as input.
# It combines the corresponding elements from these iterables into tuples based on their index/order.
# zip() operates up to the length of the shortest iterable if the input iterables are of different lengths.
# The result is a zip object, which is an iterator of tuples.

# Example 1: Using zip() with two lists
numbers = [1, 2, 3]
letters = ['a', 'b', 'c']
zipped = zip(numbers, letters)
print(list(zipped))

# Unzipping a Sequence using zip( *zipped_sequence ), where * is the unpacking operator:

# Example 2: Unzipping a Sequence
pairs = [(1, 'a'), (2, 'b'), (3, 'c')]
numbers, letters = zip(*pairs)
print(numbers) # Output: (1, 2, 3)
print(letters) # Output: (a, b, c)
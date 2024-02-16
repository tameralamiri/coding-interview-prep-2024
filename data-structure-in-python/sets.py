# Set() Function:
# It is a built-in data type in Python. they are mutable, iterable.
# Sets cannot have duplicates, and they are unordered, which means they cannot be indexed.
# They are mostly used for mathematical set operations like union, intersection, difference, and complement.

# Creating a set:
# 1. Using set() function.
even_numbers = set([2, 4, 6, 8, 10])
# 2. Using curly braces {}.
odd_numbers = {1, 3, 5, 7, 9}

# Set methods:
# 1. add(): It adds an element to the set.
even_numbers.add(12)
# 2. update(): It adds multiple elements to the set.
even_numbers.update([14, 16, 18, 20])
# 3. remove(): It removes the specified element from the set. raise an error if the element is not present.
even_numbers.remove(20)
# 4. discard(): It removes the specified element from the set. does not raise an error if the element is not present.
even_numbers.discard(18)
# 5. pop(): It removes an arbitrary element from the set, and returns the element removed.
even_number = even_numbers.pop()
# 2. clear(): It removes all the elements from the set.
even_numbers.clear()
# 3. copy(): It returns a copy of the set.
copy_odd_numbers = odd_numbers.copy()

# Sets Operations:
# 1. Union: It returns a set containing all the elements of both the sets.
numbers = odd_numbers.union(even_numbers)
# 2. Intersection: It returns a set containing the common elements of both the sets. 
common_numbers = numbers.intersection(even_numbers) # & operator can also be used.
common_numbers = numbers & even_numbers
# 3. Difference: It returns a set containing elements in the first set but not in the second.
difference_numbers = numbers.difference(even_numbers)
difference_numbers = numbers - even_numbers
# 4. Symmetric Difference: It returns a set containing elements in either of the sets but not in both.
xor_numbers = numbers.symmetric_difference(even_numbers)
xor_numbers = odd_numbers ^ even_numbers

# 5. Subset: It returns True if all elements of the set are present in another set.
is_subset = odd_numbers.issubset(numbers)

# 6. Superset: It returns True if all elements of another set are present in the set.
is_superset = numbers.issuperset(odd_numbers)

# 7. Disjoint: It returns True if two sets have no common elements.
is_disjoint = odd_numbers.isdisjoint(even_numbers)

# 8. Length: It returns the length of the set.
length = len(odd_numbers)

# 9. Maximum: It returns the maximum element of the set.
maximum = max(odd_numbers)

# 10. Minimum: It returns the minimum element of the set.
minimum = min(odd_numbers)

# 11. Sum: It returns the sum of elements of the set.
sum_of_numbers = sum(odd_numbers)


# 13. Sort: It returns a new sorted list from elements of the set.
sorted_numbers_list = sorted(odd_numbers)

# 14 all(): It returns True if all elements of the set are true.
all_numbers = all(odd_numbers)

# 15. any(): It returns True if any element of the set is true.
any_numbers = any(odd_numbers)

# 16. enumerate(): It returns an enumerate object of the set.
enum_numbers = enumerate(odd_numbers)


# Set Comprehension Syntax:
# {expression for item in iterable}

# Set Comprehension Example:
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
squared_numbers = {number ** 2 for number in numbers}
print(squared_numbers) # Output: {64, 1, 4, 36, 100, 9, 16, 49, 81, 25}

# Set Comprehension with Condition:
even_numbers = {number for number in numbers if number % 2 == 0}
print(even_numbers) # Output: {2, 4, 6, 8, 10}

# Set Comprehension with Nested Loop:
nested_numbers = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
flattened_numbers = {number for row in nested_numbers for number in row}
print(flattened_numbers) # Output: {1, 2, 3, 4, 5, 6, 7, 8, 9}

# Set Comprehension with Dictionary:
squared_numbers = {number: number ** 2 for number in numbers}
print(squared_numbers) # Output: {1: 1, 2: 4, 3: 9, 4: 16, 5: 25, 6: 36, 7: 49, 8: 64, 9: 81, 10: 100}



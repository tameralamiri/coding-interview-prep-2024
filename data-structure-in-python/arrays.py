# Arrays, Lists:
# Arrays in python are represented by the list data type. which is slow
# There's Array module in python which is faster than list but it's not commonly used. and supports only numeric values.
# List is a collection of items. It is a mutable data type. It can store elements of different data types.
my_list = [1, 2, 3, 4, 5]
my_list_mixed = [1, "Hello", 3.4, True]

# Lists Methods, Operations:
#################
# 1. Accessing Elements:
print(my_list[0]) # 1, Access elements using index, Index starts from 0.
print(my_list[-1]) # 5, # Accessing elements using negative index, Negative index starts from -1.

# 2. Slicing:
# Slicing is used to access a range of elements.
# Syntax: list[start:stop:step]
# start: starting index of the slice.
# stop: ending index of the slice, the element at this index is not included.
# step: step size of the slice.
print(my_list[1:3]) # [2, 3]
print(my_list[1:]) # [2, 3, 4, 5]

# 3. Modifying Elements:
my_list[0] = 10 # [10, 2, 3, 4, 5],  Modifying elements using index.
my_list[1:3] = [20, 30] # [10, 20, 30, 4, 5], Modifying elements using slicing.
my_list.append(6) # [10, 20, 30, 4, 5, 6], Adding elements using append() method, It takes an element as an argument, and adds it to the end of the list.
my_list.extend([7, 8, 9]) # [10, 20, 30, 4, 5, 6, 7, 8, 9], Adding elements using extend(iter) method, It takes an iterable as an argument.
my_list.insert(1, 15) # [10, 15, 20, 30, 4, 5, 6, 7, 8, 9], Adding elements using insert(index, value) method, It takes an index and an element as arguments.
my_list.remove(20) # [10, 15, 30, 4, 5, 6, 7, 8, 9], Removing elements using remove(value) method, in case of duplicate values, it removes the first occurrence.
my_list.pop(1) # [10, 30, 4, 5, 6, 7, 8, 9], Removing elements using pop(index) method, It takes an index as an argument, if no index is provided, it removes the last element.
del my_list[1] # [10, 4, 5, 6, 7, 8, 9], Removing elements using del statement, It takes an index as an argument.
my_list.clear() # [], Removing all elements using clear() method.

# 4. Concatenating Lists:
list_one = [1, 2, 3]
list_two = [4, 5, 6]
concatenated_list = list_one + list_two # [1, 2, 3, 4, 5, 6], Using + operator.
list_one.extend(list_two) # [1, 2, 3, 4, 5, 6], Using extend() method.

# 5. Repeating Lists:
repeated_list = list_one * 2 # [1, 2, 3, 4, 5, 6, 1, 2, 3, 4, 5, 6], Using * operator.
empty_list = [] * 3 # [], Using * operator with an empty list.

# 6. List Comprehension:
# List comprehension is a concise way to create lists.
# Syntax: [expression for item in iterable]
squared_numbers = [i**2 for i in range(1, 6)] # [1, 4, 9, 16, 25]
even_numbers = [i for i in range(1, 11) if i % 2 == 0] # [2, 4, 6, 8, 10]


# 7. sort() and sorted():
numbers = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5]
sorted_numbers = sorted(numbers) # [1, 1, 2, 3, 3, 4, 5, 5, 5, 6, 9], Using sorted() function, It returns a new sorted list.
numbers.sort() # [1, 1, 2, 3, 3, 4, 5, 5, 5, 6, 9], Using sort() method, It sorts the list in place.

# 8. Reversing a List:
reversed_numbers = list(reversed(numbers)) # [9, 6, 5, 5, 5, 4, 3, 3, 2, 1, 1], Using reversed() function, It returns a new reversed list.
numbers.reverse() # [9, 6, 5, 5, 5, 4, 3, 3, 2, 1, 1], Using reverse() method, It reverses the list in place.
reversed_numbers = numbers[::-1] # [9, 6, 5, 5, 5, 4, 3, 3, 2, 1, 1], Using slicing, It returns a new reversed list.

# 9. Searching for an Element:
# Using in and not in operators:
print(3 in numbers) # True
print(10 not in numbers) # True

print(numbers.index(5)) # 2, It returns the index of the first occurrence of the element. If the element is not found, it raises a ValueError.
print(numbers.count(5)) # 3, It returns the number of occurrences of the element. If the element is not found, it returns 0.

# 10. Copying a List:
numbers_copy = numbers.copy() # [9, 6, 5, 5, 5, 4, 3, 3, 2, 1, 1], Using copy() method. shallow copy, same inner list.
numbers_copy = list(numbers) # [9, 6, 5, 5, 5, 4, 3, 3, 2, 1, 1], Using list() function. 
numbers_copy = numbers[:] # [9, 6, 5, 5, 5, 4, 3, 3, 2, 1, 1], Using slicing:


# Lists Traversal:
#################
# 1. For Loop:
my_list = [1, 2, 3, 4, 5]
for item in my_list:
    print(item)

for i in range(len(my_list)):
    print(my_list[i])

for i, value in enumerate(my_list):
    print(f"Index: {i}, Value: {value}")

# 2. List Comprehension:
squared_numbers = [item**2 for item in my_list]

# 3. While Loop:
i = 0
while i < len(my_list):
    print(my_list[i])
    i += 1

# 4. Using map*() function:
# map(fun, iter)
def squared_numbers(item):
    return item**2
my_list = [1, 2, 3, 4, 5]
squared_list = list(map(squared_numbers, my_list))

# 5. Using filter*() function:
# filter(fun, iter)
# fun : It is a function to which map passes each element of given iterable, It returns a boolean value.
# iter : It is a iterable which is to be filtered.
def is_even(item):
    return item % 2 == 0
even_numbers = list(filter(is_even, my_list))

# 6. Using iter() and next():
my_list = iter([1, 2, 3, 4, 5])
while True:
    try:
        print(next(my_list))
    except StopIteration:
        break

# 7. Using zip() for Parallel Traversal:
list_one = [1, 2, 3]
list_two = [4, 5, 6]
for item1, item2 in zip(list_one, list_two):
    print(item1, item2)

# 8. Recursive Traversal:
def traverse_list(my_list):
    if not my_list:
        return
    print(my_list[0])
    traverse_list(my_list[1:])
traverse_list([1, 2, 3, 4, 5])





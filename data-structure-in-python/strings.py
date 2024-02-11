# Strings:
# Strings are immutable: You can't change a string after it's created.
# Escape Characters: \n, \t, \r, \', \", \\, \b, \f, \ooo, \xhh, use \ to escape a character.
###################
# Single line  string:
single_quote_string = 'Hello, World!'
double_quote_string = "Hello, World!"

# Multi lines string:
multi_lines_string = """ This is a 
Multi-lines
string."""

# Convert to string:
num_to_string = str(1234)

# Formatted string:
name="Darth Vader"
formatted_string = f"Hi {name}, how are you"

# Raw String: used to allow backslash
raw_string = r'Hi\n Hello'


# String Operations:
###################
# Concatenation: + operator to join strings.
string_one = "Hello"
string_two = "World"
concatenated_string = string_one + ", " + string_two

# Repetition: * operator to repeat strings.
repeated_string = "echo " * 5

# Indexing: Access a character by its position, e.g., my_string[1].
charecter = concatenated_string[7]

# Slicing: Extract a substring, e.g., my_string[1:5].
substring = concatenated_string[0:5]

# Membership: Checking if a substring exists within a string using `in`, and return boolean
contains = "World" in concatenated_string # True
contains = "world" in concatenated_string # False

# Length: len() returns the number of characters in a string.
length = len(concatenated_string)

# String Methods:
###################
# 1. String Testing Methods: These methods return `True` or `False` based on the content of the string.
example_one = "A string to test 1234"
example_two = "AStringToTest1234"
example_three = "ABC"
example_four = "444"
is_alphanumeric = example_one.isalnum() # False, Checks if all characters are alphanumeric.
is_alphanumeric = example_two.isalnum() # True
is_alpha = example_one.isalpha() # False, Checks if all characters are alphabetic.
is_digit = example_one.isdigit() # False, Checks if all characters are digits.
is_lower = example_one.islower() # False, Checks if all characters are lowercase.
is_upper = example_one.isupper() # False, Checks if all characters are uppercase.
is_space = example_one.isspace() # False, Checks if all characters are whitespace.
is_title = example_one.istitle() # False, Checks if the string is titled (first character in each word is uppercase).
starts_with = example_one.startswith("A") # True, Checks if the string starts with a specific substring.
ends_with = example_one.endswith("4") # True, Checks if the string ends with a specific substring.

# 2. Searching, Counting and replacing Methods:
example_two = "AStringToTest1234"
substring_first_index = example_two.find("Test") # 8, Finds the first occurrence of a substring and returns its index. Returns -1 if not found.
substring_first_index = example_two.index("Test") # 8, Same as find, but raises a ValueError if not found.
substring_first_index = example_two.rfind("Test") # 8, Finds the last occurrence of a substring and returns its index. Returns -1 if not found.
substring_first_index = example_two.rindex("Test") # 8, Same as rfind, but raises a ValueError if not found.
substring_first_index = example_two.count("T") # 2, Counts the number of occurrences of a substring.
new_string = example_two.replace("Test", "Replace") # Replaces occurrences of a substring.

# 3. Splitting and Joining Methods:
example_three = "A String To Test 1234"
split_string = example_three.split(" ") # Splits a string into a list of substrings based on a separator.
join_string = " ".join(split_string) # Joins a list of substrings into a single string using a separator.
partition_string = example_three.partition("To") # Splits the string at the first occurrence of the separator into a tuple (before, separator, after).
rpartition_string = example_three.rpartition("To") # Splits the string at the last occurrence of the separator into a tuple (before, separator, after).

# 4. Stripping Methods:
example_four = "   A String To Test 1234   "
stripped_string = example_four.strip() # `.strip(chars)` Removes leading and trailing characters (whitespace by default or specified characters).
stripped_left_string = example_four.lstrip() # `.lstrip(chars)` Removes leading characters on the left side.
stripped_right_string = example_four.rstrip() # `.lstrip(chars)` Removes trailing characters on the right side.


# 5. Text alignment Methods:
example_five = "A String To Test 1234"
centered_string = example_five.center(40, "#") # Centers the string, padding it with the specified fill character from both sides(space by default).
left_justified_string = example_five.ljust(40, "#") # Left-justifies the string, padding it with the specified fill character from the right(space by default).
right_justified_string = example_five.rjust(40, "#") # Right-justifies the string, padding it with the specified fill character from the left(space by default).

# 6. Case Methods:
zfilled_string = example_four.zfill(30) # Pads the string with zeros from the left to make it at least 30 characters long.
capitalized_string = example_five.capitalize() # Capitalizes the first character of the string.
titlecased_string = example_five.title() # Capitalizes the first character of each word in the string.
upper_case_string = example_five.upper() # Converts the string to uppercase.
lower_case_string = example_five.lower() # Converts the string to lowercase.
swapped_case_string = example_four.swapcase() # Swaps the case of each character in the string.

# 7. Encoding and Decoding Methods:
example_six = "A String To Test 1234"
encoded_string = example_six.encode("utf-8") # Encodes the string using the specified encoding.
decoded_string = encoded_string.decode("utf-8") # Decodes the string using the specified encoding.

# 8. Formatting Methods:
formatted_string = "Hello, {} {}".format("World", "!")
formatted_string = "Hello, {:d}".format(1234)



# String Traversal:
###################

# 1. Basic For Loop:
for ch in concatenated_string:
    print(ch)

# Using range:
for i in range(len(concatenated_string)):
    print(concatenated_string[i])

# Iterating in Chunks:
chunk_size = 3
for i in range(0, len(concatenated_string), chunk_size):
    print(concatenated_string[i:i+chunk_size])

# Using enumerate:
for i, ch in enumerate(concatenated_string):
    print(f"Index: {i}, Character: {ch}")

# 2. While Loop:
i = 0
while i < len(concatenated_string):
    print(concatenated_string[i])
    i += 1

# 3. List Comprehension:
characters = [ch for ch in concatenated_string]
print(characters) # ['H', 'e', 'l', 'l', 'o', ',', ' ', 'W', 'o', 'r', 'l', 'd', '!']

# 4. Map Function: the map function applies a function to each item in an input list.
# map(fun, iter)
# fun : It is a function to which map passes each element of given iterable.
# iter : It is a iterable which is to be mapped.
characters = list(map(str, concatenated_string)) 
print(characters) # ['H', 'e', 'l', 'l', 'o', ',', ' ', 'W', 'o', 'r', 'l', 'd', '!']

# 5. Iterating Backwards:
# Using reversed():
for ch in reversed(concatenated_string):
    print(ch)

# Using slice notation:
for ch in concatenated_string[::-1]:
    print(ch)

# Iterating in Reverse Order:
for i in range(len(concatenated_string)-1, -1, -1):
    print(concatenated_string[i])

# 6. Iterating in Parallel:
# Using zip(): Zip function takes two or more iterables and returns an iterator that generates tuples of items from the iterables.
string_one = "Hello"
string_two = "World"
for ch1, ch2 in zip(string_one, string_two):
    print(ch1, ch2)

# 7. Using iter() and next():
# iter() returns an iterator object.
# next() retrieves the next item from the iterator.
my_string = iter("Hello")
while True:
    try:
        print(next(my_string))
    except StopIteration:
        break

# 8. Recursive Traversal:
def traverse(string):
    if len(string) == 0:
        return
    print(string[0])
    traverse(string[1:]) # Recursive call
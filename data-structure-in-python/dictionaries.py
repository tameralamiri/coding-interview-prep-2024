# Dictionaries:
# 1. A dictionary is a built-in data type that store collections of key-value pair. unordered, mutable and indexed. 
# 2. Keys must be unique and immutable. such as strings, numbers, or tuples.
# 3. Dictionaries are the representations of hash tables


# Creating a dictionary:
# 1. Using curly braces {}.
person = {
    "name": "John",
    "age": 30,
    "city": "New York"
}
print(person)
# 2. Using dict() function:
person = dict(name="John", age=30, city="New York")
print(person)

# Accessing elements:
# 1. Using square brackets [], returns an error if the key does not exist.
print(person["name"])
# 2. Using get() method, returns None if the key does not exist.
print(person.get("age"))

# Changing elements:
# 1. Using square brackets [].
person["age"] = 40
print(person)
# 2. Using update() method, to add a new key-value pair or update an existing one.
person.update({"age": 50})
print(person)

# 3. Using pop() method, to remove a key-value pair by key. or returns an error if the key does not exist.
person_age = person.pop("age")

# 4. using del keyword, to remove a key-value pair by key.
del person["age"]


# Looping through a dictionary:
# 1. Loop through keys:
for key in person:
    print(key)

# 2. Loop through values:   
for value in person.values():
    print(value)

# 3. Loop through both keys and values:
for key, value in person.items():
    print(key, value)

# Check if a key exists:
if "name" in person:
    print("Yes, 'name' is one of the keys in the person dictionary")

# Check the length of a dictionary:
print(len(person))

# Renaming a key:
person["first_name"] = person.pop("name") # pop() method returns the value of the key that is removed.
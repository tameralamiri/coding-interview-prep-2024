# OOP (Object Oriented Programming) in Python:
# 1. Class and Object
# 2. Inheritance
# 3. Encapsulation
# 4. Polymorphism

# Class and Object:
# 1. A class is a blueprint for creating objects.
# 2. An object is an instance of a class.
# 3. A class is defined using the class keyword.
# 4. An object is created using the constructor of the class.
# 5. The constructor is a special method that is automatically called when an object is created.
# 6. The constructor method is called __init__.
# 7. The self parameter is a reference to the current instance of the class, and is used to access variables that belongs to the class.
# 8. The self parameter is not passed in when the object is created.


# Example:
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def greet(self):
        print(f"Hello, my name is {self.name} and I am {self.age} years old.")

darth = Person("Darth Vader", 50)
print(darth.name)

# Inheritance:
# 1. Inheritance is a mechanism in which one class acquires the properties and behavior of another class.
# 2. The class that is inherited from is called the parent class.
# 3. The class that inherits is called the child class.
# 4. The child class can override the methods of the parent class.
# 5. The child class can also add new methods and properties.
# 6. In Python, inheritance is defined by putting the parent class in parentheses after the child class name.

# Example:
class Student(Person):
    def __init__(self, name, age, student_id):
        super().__init__(name, age)
        self.student_id = student_id

    def study(self):
        print(f"{self.name} is studying.")

luke = Student("Luke Skywalker", 20, "123")

luke.greet() # Accessing the parent class method:
luke.study() # Accessing the child class method:

# Encapsulation:
# 1. Encapsulation is the process of restricting access to certain parts of an object.
# 2. Encapsulation is achieved by using private and protected access modifiers.
# 3. Private members are denoted by a double underscore prefix.
# 4. Protected members are denoted by a single underscore prefix.
# 5. Private members can only be accessed within the class.
# 6. Protected members can be accessed within the class and its subclasses.

# Example:
class Car:
    def __init__(self):
        self.__speed = 0
        self._color = "Red"

    def accelerate(self):
        self.__speed += 10
        print(f"The car is accelerating at {self.__speed} km/h.")

    def brake(self):
        self.__speed -= 10
        print(f"The car is braking at {self.__speed} km/h.")

    def _private_method(self):
        print("This is a private method.") 


ferrari = Car()
print(ferrari.__speed) # This will raise an error, # Accessing the private member:
print(ferrari._color) # This will not raise an error, but it is not recommended to access protected members directly.
print(ferrari._private_method()) # This will not raise an error, but it is not recommended to access private methods directly.

# Polymorphism:
# 1. Polymorphism is the ability of an object to take on many forms.
# 2. Polymorphism is achieved by using method overriding and method overloading.
# 3. Method overriding is the process of redefining a method in the child class.
# 4. Method overloading is the process of defining multiple methods with the same name but different parameters.

# Example:
class Animal:
    def speak(self):
        print("The animal makes a sound.")

class Dog(Animal):
    def speak(self): # Method overriding
        print("The dog barks.")


animal = Animal()
animal.speak() # The animal makes a sound.
dog = Dog()
dog.speak() # The dog barks.


# Method overloading:
# 1. Method overloading is not supported in Python.
# 2. However, you can achieve method overloading by using the *args and **kwargs parameters.
# 3. The *args parameter is used to pass a variable number of non-keyword arguments to a function.
# 4. The **kwargs parameter is used to pass a variable number of keyword arguments to a function.
# Example:
class Calculator:
    def add(self, *args):
        return sum(args)
    
    # **kwargs
    def sub(self, **kwargs):
        return kwargs['a'] - kwargs['b']
    
# example:
calculator = Calculator()
print(calculator.add(2, 3)) # 5
print(calculator.add(2, 3, 4)) # 9
print(calculator.sub(a=2, b=3)) # 5


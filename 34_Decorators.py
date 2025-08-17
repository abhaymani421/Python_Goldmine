"""
Decorators in Python
--------------------

A decorator is a special tool in Python that lets you add extra features 
to a function (or class) without changing its original code.

Think of a decorator like gift wrapping:
- You already have a gift (the function).
- You wrap it (apply the decorator).
- Now, when you give the gift (call the function), it looks nicer or 
  has some added effect.

How it works:
-------------
1. A decorator is itself a function that takes another function as input.
2. It usually defines an inner function (wrapper) that adds new behavior.
3. It returns this wrapper, replacing the original function.
4. The '@decorator_name' syntax is a shortcut to apply it.
"""

def my_decorator(func): # basically func is the gift and we decorate it with the wrapper
    def wrapper():
        print("Something extra before the function runs")
        func()
        print("Something extra after the function runs")
    return wrapper

@my_decorator   # applying the decorator
def say_hello(): # the function on which the decorator was applied 
    print("Hello!")
# the above three line are actually equivalent of this-->(say_hello = my_decorator(say_hello))
say_hello()

#Inbuilt Decorators-->
#@staticmethod-->
'''The @staticmethod decorator is used to define a method that doesn't operate on an instance
of the class (i.e., it doesn't use self). Static methods are called on the class itself, 
not on an instance of the class.'''
class MathOperations:
    @staticmethod
    def add(x, y):
        return x + y

# Using the static method
res = MathOperations.add(5, 3)
print(res)


#CLASSMETHOD-->
class Student:
    school_name = "IIT Jodhpur"   # class variable

    def __init__(self, name):
        self.name = name

    @classmethod
    def from_string(cls, student_str): # this does not belong to any instance but to the whole class
        # cls(...) creates a new object of this class
        name = student_str.title()
        return cls(name)   # this uses cls instead of hardcoding Student()

# Usage
s1 = Student.from_string("abhaymani") # this creates a new object where name = "abhaymani" and assigns it to s1
print(s1.name)         # Abhaymani
print(s1.school_name)  # IIT Jodhpur

#CHAINING DECORATORS-->
def decor1(func): 
    def inner(): 
        x = func() 
        return x * x 
    return inner 

def decor(func): 
    def inner(): 
        x = func() 
        return 2 * x 
    return inner 
#while chaining decorators remember this that the decorator nearest to the function runs first.

@decor1
@decor
def num(): 
    return 10

@decor
@decor1
def num2():
    return 10
  
print(num()) 
print(num2())
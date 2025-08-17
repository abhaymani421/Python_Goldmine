#what are nested functions -->
#when we define a function inside another function then the inner one is called nested function or simple inner function
# Why use it?

# Encapsulation / Protection → The inner function is hidden from the outside world. 
# It can only be used inside the outer function.

# Code Organization → Helps group related logic together.

# Access to Outer Variables → Inner function can use variables from the outer function (this is called a closure).

#EXAMPLE -->
def calculator(number):
    def square(): #nested function
        return number * number
    
    def cube(): #nested function
        return number * number * number
    
    print("Square:", square())
    print("Cube:", cube())

calculator(3)

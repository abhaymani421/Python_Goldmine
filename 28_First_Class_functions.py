def example():
    """
    First-Class Functions in Python:

    In Python, functions are treated as "first-class citizens."
    This means functions can be:
      1. Assigned to variables.
      2. Passed as arguments to other functions.
      3. Returned from other functions.
      4. Stored in data structures (like lists, dicts, etc.).

    Because of this property, Python supports functional programming
    features such as higher-order functions, decorators, and callbacks.
    """
    pass

#Assigning functions to variables-->
def greeting_to(name) : 
    print(f"Hello {name}")

f = greeting_to # assigning the function to the variable
f("Abhay") #calling the function using that variable

#Passing function as arguments -->
def eligibility(age):
    if age>=18:
        return "YES"
    return "NO"

def can_I_vote(func,name,age):
    print(f"{func(age)}, {name}!")

can_I_vote(eligibility,"Abhay",22)
    
#Returning functions from other functions-->
def fun1(msg):
    def fun2():
        return f"Message: {msg}"
    return fun2

# Getting the inner function
func = fun1("Hello, World!")
print(func())

#Storing functions in data structures -->

def add(x,y):
    return x+y  
def sub(x,y):
    return x-y 

func_dict = {
    "addition" : add,
    "subtract" : sub
}

print(func_dict["addition"](3,4))
print(func_dict["subtract"](12,8))

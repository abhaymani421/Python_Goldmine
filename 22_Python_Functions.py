#python function are block of code use to specify a task
# they can be reused and also increase readibility, and this we do not have to write the same code again and again
#if we want the same functionality
#def kewword--> it is used to create a userdefined function
#Syntax-->
'''
def function_name(parameters):

    # function body
'''
def intro() : 
    print("hey, i am abhay!")

intro() # calling the function

def area_of_square(side) : 
    return side*side #returns the value to the place from where the function was called
side = int(input("enter side of the square to find its area : "))
print("The area of the Square is : ",area_of_square(side))

#writing functions with type hints in python
#type hints in python just improve the code readibility by mentioning the expected variable data type of the parameters
#and the return type too. they do not enforce any data type at runtime since python is a dynamically typed language
def area_of_rectangle(l : int, b : int)->int : #type hints are utilised here
    return l*b
length = int(input("enter length of the rectangle : ")) 
breadth = int(input("enter breadth of the reactangle : "))
print("The area of the rectangle is :",area_of_rectangle(length,breadth))

#Type of functional arguments -->
# Default argument 
# Keyword arguments (named arguments)
# Positional arguments
# Arbitrary arguments (*args and **kwargs)

#DEFAULT ARGUMENTS (if a value for a particular argument is not provided then it takes the default value)

def did_you_vote(voted = False) : 
    if voted==True : 
        print("I have voted")
    else : 
        print("I Haven't")

did_you_vote(True) # since the user provided true that he did vote the message that printed was "i have voted"
did_you_vote()# since the user provided nothing, it took false as default argument and printed "I haven't"

#KEYWORD ARGUMENTS 
# if the user already specifies the argument names with their respective values then there is no need to pass the arguments
#in the correct order. this is the idea behind keyword arguments .

def My_name(firstName,LastName) : 
    print(f"My name is {firstName} {LastName}")

My_name(LastName="Singh",firstName="Abhaymani") # the order of passing values doesnt matter here since we already assigned them

#POSITIONAL ARGUMENTS : 
#these are what are used in most of the cases , like mentioned above in area of square, area of rectangle

#Arbitary Arguments : 
# In Python, sometimes you don’t know how many arguments a function will receive. 
# Instead of fixing the number of arguments, you can use *args and **kwargs to handle a variable number of inputs.

#*arg-->
# Collects extra positional arguments (non-keyword) into a tuple.
# You can pass any number of values, and they’ll be packed inside args.
def find_sum(*args) : 
    sum = 0 
    for i in args : 
        sum+=i 
    return sum 

print("Sum of 1+2+3+...7 :",find_sum(1,2,3,4,5,6,7))
print("Sum of 1+2+3+4....12:",find_sum(1,2,3,4,5,6,7,8,9,10,11,12))

#*kwargs takes keyword arguments and packs them in the form of a dictionary -->
def My_info(**kwargs) : 
    print(kwargs)
    for key,value in kwargs.items() : 
        print(f"{key} : {value}")

My_info(name = "Abhay", age = "22", hobby = "coding")

#a good practice is to write about the function in short in the form of a doctstring at the top of the function body
'''
In Python, global variables are declared outside any function and can be accessed anywhere 
in the program, including inside functions. On the other hand, local variables are created 
within a function and are only accessible during that function’s execution. This means local 
variables exist only inside the function where they are defined and cannot be used outside it
'''

def greetings() : 
    msg = "Hey, How are you" #this is a local variable
    print(msg)

greetings()
#print(msg) # this gives name error as msg is a local variable and cannot be accessed outside the function

message = "This is a global greeting"

def global_gretting() : 
    print(message) # since message was a global variable , it can be accessed from the inside

global_gretting()

#WHAT HAPPENS WHEN THE LOCAL VARIABLE AND GLOBAL VARIABLE DEFINED HAVE THE SAME NAME?
'''
If a variable is defined both globally and locally with the same name, 
the local variable shadows the global variable inside the function. 
Changes to the local variable do not affect the global variable unless you explicitly
declare the variable as global. 
'''

def inside_outside() : 
    s = "Hello from inside the function"
    print(s) # uses the local s , the global s does not get affeceted

s = "Hello from outside the function"
inside_outside()
print(s) #prints the global s , no changes due the function

#WHAT IF WE TRY TO MODIFY THE GLOBAL VARIABLE INSIDE THE FUNCTION?
'''
Attempt to change the global variable inside a function without explicitly declaring it global
isnide the function will cause errors
Example-->
def fun():
    s += 'GFG'    # this gives error
    print("Inside Function", s)

s = "I love Geeksforgeeks"
fun()
'''
#CORRECT WAY TO MODIFY GLOBAL VARIABLES INSIDE THE FUNCTION
def modify():
    global age
    age = 23
   
age = 22 
print(f"My age is {age}") 
modify()
print(f"My age is {age}") # age gets modified from inside the function and takes the value of 23
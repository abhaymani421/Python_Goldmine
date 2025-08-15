"""
In Python, variables store references to objects rather than the actual objects themselves.
Assigning `x = 5` creates an integer object with value 5 and makes `x` reference it. Assigning
`y = x` creates another reference to the same object (shared reference). Reassigning `x` or `y`
creates new objects and updates the references, without affecting other variables referencing
the original object. When no references remain, the object is eligible for garbage collection.

Variables can be deleted using the `del` keyword, which removes them from the namespace and
frees memory. Accessing a deleted variable raises a `NameError`.

Swapping variables can be done without a temporary variable using tuple unpacking:
`a, b = b, a`. Variables can store results of operations, such as `length = len(word)`.
Variable scope determines where they can be accessed: local variables exist only within a
function or block and are destroyed when it ends, while global variables exist outside functions,
are accessible throughout the program, and can be modified inside functions using the `global`
keyword.
"""
#swapping without a temporaray variable
a = 3 
b = 5  
print(a,b)
a,b = b,a
print(a,b)
#with a temporary variable
temp  = a 
a = b
b = temp 
print(a,b)

#counting characters in a string
word = "python"
length = len(word)
print("length of the word : ",length) 

# Scope of a Variable
# In Python, the scope of a variable defines where it can be accessed in the program. There are two main types of scope: local and global.

# Local Variables:
# Defined within a function or block, accessible only inside that scope.
# Destroyed once the function/block ends.
# Temporary, used for short-term data.
    
# Global Variables:
# Defined outside functions, accessible throughout the program.
# To modify within a function, use the global keyword.
# Persist in memory for the program’s duration, useful for shared data.

# Using an undefined variable raises a NameError. Always initialize variables before use.
def create_global():
    global my_var
    my_var = "Hello from inside the function"

# Call the function so the global variable is created
create_global()

# Now we can use it anywhere in this file
print(my_var)  

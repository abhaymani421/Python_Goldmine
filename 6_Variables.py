# In Python, variables are used to store data that can be referenced and 
# manipulated during program execution. 
# A variable is essentially a name that is assigned to a value. Unlike many other programming 
# languages, Python variables do not require explicit declaration of type. 
# The type of the variable is inferred based on the value assigned.
#Variables act as placeholders for data. 
# They allow us to store and reuse values in our program.
x = 5 # variable of type integer and we are assigning values using = operator
name = "abhay"#variable of type string

# Dynamic Typing
# Python variables are dynamically typed, 
# meaning the same variable can hold different types of values during execution.
x = 10 
x = "Now a string"

#Assigning the Same Value
a=b=c=100 
print(a,b,c)
#Assigning different Values
a,b,c = 2,2.5,"abhay"
print(a,b,c)

#type casting a variable -->
# Casting variables
s = "10"  # Initially a string
n = int(s)  # Cast string to integer
cnt = 5
f = float(cnt)  # Cast integer to float
age = 25
s2 = str(age)  # Cast integer to string

# Display results
print(n)  
print(f)  
print(s2)
# in Python, Ternary operators also known as conditional expressions are operators that 
# evaluate something based on a condition being true or false. 
# It was added to Python in version 2.5. 

# It simply allows testing a condition in a single line 
# replacing the multiline if-else making the code compact.

# Syntax :  [on_true] if [expression] else [on_false] 

a,b = 10,20

min = a if a<b else b
print(min)

a, b, c = 10, 20, 30

# Choose smallest among a, b, c (nested ternary)
smallest = a if a < b and a < c else (b if b < c else c)
print(smallest)  # 10

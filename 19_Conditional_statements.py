# Conditional statements in Python are used to execute certain blocks of code based on specific 
# conditions. These statements help control the flow of a program, making it behave differently 
# in different situations.

age = int(input("enter you age : "))
if age<=12:
    print("free travel, no ticket fare")
else :  
    print("ticket fare appliable, paid travel")

print("eligible to vote" if age>=18 else "not eligible") # we used a ternary operator here

#elif statement-->
if age<=12 : 
    print("child")
elif age<=19 : 
    print("teenager")
elif age<=30 : 
    print("young adult")
elif age<60 : 
    print("adult")
else : 
    print("senior citizen")

#ternary conditional statement
verdict = "minor" if age<18 else "adult"
print("verdict :",verdict)

#Match case statement in python
# Sure! The match-case statement in Python is essentially Python’s way of doing what other 
# languages call a switch-case, but it’s more powerful because it supports pattern matching.
item = (0, 5, 10)

match item:
    # Match tuple starting with 0, capture the rest
    case (0, *rest):
        print(f"Tuple starts with 0, rest = {rest}")
    
    # Match exact values
    case 1 | 2: # | acts as or in pattern matching in match case statements
        print("Exact match: 1 or 2")
    
    # Match any other tuple of length 3
    case (x, y, z):
        print(f"Other tuple with 3 elements: ({x}, {y}, {z})")
    
    # Default case
    case _:
        print(f"Fallback: {item}")

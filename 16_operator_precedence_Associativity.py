# Operator Precedence in Python
# This is used in an expression with more than one operator with different precedence to 
# determine which operation to perform first.

# Operator Associativity in Python
# If an expression contains two or more operators with the same precedence then Operator 
# Associativity is used to determine. It can either be Left to Right or from Right to Left.

#examples-->
print(100 / 10 * 10)
print(5 - 2 + 3)
print(5 - (2 + 3))
print(2 ** 3 ** 2)

# Precedence	Operators	Description	Associativity
# 1

# ()	
# Parentheses

# Left to right

# 2

# x[index], x[index:index]	
# Subscription, slicing

# Left to right

# 3

# await x	
# Await expression

# N/A

# 4

# **	
# Exponentiation

# Right to left

# 5

# +x, -x, ~x	
# Positive, negative, bitwise NOT

# Right to left

# 6

# *, @, /, //, %	
# Multiplication, matrix, division, floor division, remainder

# Left to right

# 7

# +, -	
# Addition and subtraction

# Left to right

# 8

# <<, >>	
# Shifts

# Left to right

# 9

# &	
# Bitwise AND

# Left to right

# 10

# ^	
# Bitwise XOR

# Left to right

# 11

# |	
# Bitwise OR

# Left to right

# 12

# in, not in, is, is not, <, <=, >, >=, !=, ==	
# Comparisons, membership tests, identity tests

# Left to Right

# 13

# not x	
# Boolean NOT

# Right to left

# 14

# and	
# Boolean AND

# Left to right

# 15

# or	
# Boolean OR

# Left to right

# 16

# if-else	
# Conditional expression

# Right to left

# 17

# lambda	
# Lambda expression

# N/A

# 18

# :=	
# Assignment expression (walrus operator)

# Right to left
a = 10
b = 20
c = a
d = 19 
e = 19 
# 'is' checks wether the two variables are actually refrencing the same object, not just that they have the same value.
print(a is not b)
print(a is c)
print(d is e)#What’s happening here is a quirk of Python’s object model called integer interning (or caching).
# Python optimizes small integers by keeping them in memory for reuse.

# In CPython, integers from -5 to 256 are interned (pre-created and reused).

# This means when you write 19 anywhere in your code, Python doesn't create a new object—it reuses the same object.

f = 25700000000000 
g = 25700000000001
print(f is g)
print(id(f)) #id() → lets you see the actual object identity number.
print(id(g))


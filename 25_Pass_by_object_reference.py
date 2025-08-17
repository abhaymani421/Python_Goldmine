#In python there is nothing like pass by reference or pass by value like it occurs in the traditinal sense in C and C++
#Instead python has pass by object refrence 
#So here is general thumb rule in case of python-->
# In Python, everything is an object, and variables are just references (names) pointing to those objects.

# So when you pass something into a function:
# Python passes the reference to the object (not a copy of the object).
# BUT, whether the object itself can be changed depends on if it’s mutable or immutable.

# Mutable vs Immutable

# Mutable objects (can be changed): lists, dictionaries, sets, etc.
# Immutable objects (cannot be changed): integers, floats, strings, tuples, etc.

#Example of Mutable object-->
def Info(lst_arg):
    lst_arg[0] = "Gaurav"

lst = ["Abhay",22,"IITJ"]
print("before passing into the function :",lst)
Info(lst)
print("After passing to the function :",lst) # the original list does get updated

#Example of Immutable object-->
def swap(x,y):
    temp = x
    x=y 
    y = temp

x,y = 2,3
print("before swapping :","x :",x,"y :",y)
swap(x,y)
print("After swapping :","x :",x,"y :",y)
#from the resule it can be seen that swap does not happend because the local variable of the functions got swapped and not the outer ones
# as soon as we reassigned the local variables, since they are immutable they created a new object and started pointing to it



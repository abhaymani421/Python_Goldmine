"""
Mutable vs Immutable Data Types in Python
------------------------------------------

Immutable Data Types:
    - Once created, their value cannot be changed (modified in-place).
    - Any operation that seems to "change" them actually creates a new object in memory.
    - Examples:
        int, float, complex
        bool
        str
        tuple
        frozenset
        bytes

Mutable Data Types:
    - Can be changed in-place without creating a new object.
    - Operations on them modify the original object in memory.
    - Examples:
        list
        dict
        set
        bytearray
        user-defined classes (unless explicitly made immutable)

Theory:
    - "Immutability" means the internal state of an object cannot be altered after creation.
    - For immutable objects, variable reassignment points the variable name to a new object.
    - For mutable objects, in-place changes affect the same object referenced by other variables.
"""

#integer, float, complex data types-->
a = 5 
print(type(a)) 
b = 6.0
print(type(b))
c = 5+7j
print(type(c))

#string datatype -->
s = "Welcome to the world of data types"
print(type(s))
#0-based indexing
print(s[1])
print(s[11])
print(s[-1]) # last character of the string

#list data types -->
a = []
a = [1,"Abhay",True]
print(a[0])
print(a[1])
print(a[2])
a[1] = "gaurav" #list is mutable
print(a[-2]) #using negative indexing
print(a[-3])
print(a)
a.append(5)
a.remove(1) # remove first occurnence of that element from the list
print(a)
#Tuple data Type-->
a = () #empty tuple 
a = (1,2,3)
print(a[0]) 
print(a[1])
print(a[2])
# we can use negative indexing too as we used in list data type
b = 1,2,3,4,5 # called tuple packing, b is a tuple
print(b)
#a[1] = 4 this gives error since tuples are immutable

#Boolean data type-->
print(type(True))
print(type(False))

#Set data type in python-->
#set cannot contain duplicate entries
# initializing empty set
# all the entries of the set must be elements of immutable datatypes. so we cannot have list dict etc in the set
s1 = set()
# sets are unordered data types unlike list they do not have the concept of indexing
s1 = set("GeeksForGeeks")
print("Set with the use of String: ", s1)

s2 = set(["Geeks", "For", "Geeks"])
print("Set with the use of List: ", s2)

s3 = {1,2,3,"abhay",4.5}
print(type(s3),s3)

# for accesing set items we have to loop over them since indexing is out of options-->
for i in s3 : 
    print(i)


#Dictionary Data types-->
d = {1:'Abhay',2 : 'Alwar',3 : 'IITJ'} #key-value pair
d1 = dict([(1,"abhay"),(2,"IITJ")])
d2 = dict([[1,"abhay"],[2,"IITJ"]])
print(d1)
print(d2)

#Accesing an element using key-->
d = {'name' : 'Abhaymani', 'college' : 'IIT Jodhpur','age' : 22}
print(d.get('age'))
print(d['name'])
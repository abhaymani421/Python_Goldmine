from functools import reduce
import operator
import functools
from itertools import accumulate
from operator import add
'''
The reduce() function in Python applies a given function cumulatively to all items in an 
iterable, reducing it to a single final value.

It’s a method of the functools module, so we need to import it before use
'''

#basic use -->
def add(x,y) : 
    return x+y

lst = [1,2,3,4,5,6,7,8]
res = reduce(add,lst)
print(res)

#with lambda function -->

lst = [1,2,3,4,5]
res = reduce(lambda x,y : x+y, lst)
print(res)
a = [1, 3, 5, 6, 2]
print(functools.reduce(operator.add, a)) # Sum of list
print(functools.reduce(operator.mul, a)) # Product of list
print(functools.reduce(operator.add, ["Python", "For", "The","Win"])) #string concatenation

a = [1, 2, 3]
res = reduce(lambda x, y: x + y, a, 10) # we used a intial value here to sum the list, so basically this results in 10+1+2+3
print(res)

#Accumulate function --> useful to find the prefix sum list of a list
lst1 = [1,2,3,4,5,6]
res = accumulate(lst1,add)
print(list(res)) # accumulate return an iterator so we have to typecast it into an object
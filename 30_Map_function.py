'''
map() function in Python is used to apply a specific function to each element of an iterable 
(like a list, tuple, or set) and returns a map object (which is an iterator).
'''

def square(val) :
    return val**2
lst = [1,2,3,4,5]
res = map(square,lst) 
print(list(res)) #map is a object so we have to type cast it into a list 

#Converting a list of string number to list of integers
lst = ['1','2','3','4']
res = map(int,lst)
print(list(res))

#map with lambda function-->
lst = [1,2,3,4,5]
res = map(lambda x : x**3,lst)
print(list(res))

#map with mulltiple iterables -->
lst1 = [1,2,3,4,5]
lst2 = [1,2,3,4,5]
def added(x,y):
    return x+y 
res = map(added,lst1,lst2)
print(list(res)) # takes one element from lst1 and other from lst2 and adds them and does the same for each index

#Converting strings to Upper case

fruits = ['Apple','banana','cherry']

res = map(str.upper,fruits)

#removing trailing and leading whitespaces
print(list(res))
fruits = ['  Apple   ','  banana  ','  cherry  ']
print(fruits)

for i,j in enumerate(fruits) : 
    fruits[i] = j.strip()  # reomve white space from the extreme end

print(fruits)
#Short way of doing the same thing using map-->
fruits = ['  Apple   ','  banana  ','  cherry  ']
print(fruits)
print(list(map(str.strip,fruits)))

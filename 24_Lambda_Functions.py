'''
lambda functions, also called anonymous functions(they dont have a name) are one liner functions 
provided by python for short use
'''
add = lambda a,b : a+b #a and b are the arguments and after colon we have the return value
print(add(5,7)) 

greet = lambda : "Hello how are you"
print(greet())

cube = lambda x:x**3
print(cube(4))

#Checking wether a number is positive , negative or 0 using lambda functions 
checker = lambda x : "Positive" if x>0 else "Negative" if x<0 else "Zero"

print(checker(6))
print(checker(-7))
print(checker(0))

#Lambda function with list comprehension(is covered in detail in later files)
li = [lambda arg=x: arg * 10 for x in range(1, 5)]
for i in li:
    print(i())
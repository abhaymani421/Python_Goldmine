# Python's input() function is used to take user input. 
# By default, it returns the user input in form of a string. 
name = input("what is your name : ")
print("Hello,",name,"! how are you doing.")

s = "bob" 
print("Hello",s)
city = "alwar"
dob = "23rdJun"
print(s,city,dob) #printing multiple outputs

#taking multiple inputs-->
x,y,z = input("Enter three values space seperated : ").split() # taking three inputs at a time
print(x,y,z)
# we know that python by default takes input as a string , but we can change the data type of input-->
number = int(input("enter a integer : ")) # this is basically typecasting
print(number)
print(type(number)) # to check the type of the input
#similarly we can do the same for float and other data types lets have a look-->
a = "Hello World"
b = 10
c = 11.22
d = ("Geeks", "for", "Geeks")
e = ["Geeks", "for", "Geeks"]
f = {"Geeks": 1, "for":2, "Geeks":3}


print(type(a))
print(type(b))
print(type(c))
print(type(d))
print(type(e))
print(type(f))
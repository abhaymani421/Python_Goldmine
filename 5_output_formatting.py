#f string-->
name = "abhay"
college = "IITJ"
age = 22
print(f'My name is {name}, I completed my graduation at the age of {age} from the college of {college}')

#format method-->
Amount = 150.68695
print("Amount : ${:.2f}".format(Amount)) #{} this is a place holder for original variable and :.2f instructs to round of the variable to two decimal places

#using sep and end parameter -->
# end Parameter with '@'
print("Python", end='@') #prints the end parameter instead of going to the next line
print("GeeksforGeeks")

# Seprating with Comma
print('G', 'F', 'G', sep='')

# for formatting a date
print('09', '12', '2016', sep='-')

# another example
print('Abhay', 'geeksforgeeks', sep='@')

#Using % Operator-->
# %d –integer
# %f – float
# %s – string
# %x –hexadecimal
# %o – octal
age = 22 
name = "abhay"
print("My name is %s and my age is %d" % (name, age))
print("My name is %s" %name)

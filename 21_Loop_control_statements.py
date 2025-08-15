# Loop control statements change execution from their normal sequence.
# break statement --> makes the loop exit prematurely
for i in range(10) :
    if(i==6):
        break # exits the range for loop prematurely on i=6 and does not conver the full loop
    else:
        print(i,end=" ")
print()

#continue statement 
#it skips the current iteration and continues with the next one
for i in range(10) : 
    if i%2==0:
        continue 
    else :
        print(i) # prints all the odd integers between 0 and 10 (10 not included)

#Pass statement--> it is a null operation , it does nothing and thus sometimes act as a placehoder for future code

for i in range(20) : 
    if(i%2==0) : 
        pass
        # can figure this code in future. till that time pass is a placeholder.
    else : 
        print(i,end = " ")    
print()
#else statement with for loops 
# The else block just after for/while is executed only when the loop is NOT terminated by a break statement.
lst = ['abhay','gaurav','atharva','garvit']
for i in lst : 
    print(i)
else : # since there was no break statement in the for loop therefore this else will get executed
    print("they are friends")

#Using enumerate with for loop -->
#enumerate function helps to keep track of the index of each item in the iterable
for i,j in enumerate(lst) : 
    # i stores the index , j stores the actual values at those indexes
    print(f"at index {i} we have :",j)

#Nested loops 
lst = [[1,2,3],[4,5,6],[6,7,8]] # nested list
for i in lst : 
    for j in i : #The inner loop is executed for each value of i in outer loop.
        print(j,end=', ')
    print()
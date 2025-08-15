#for Loop :
for i in range(10) : # 10 is not inclusive and starts from 0  
    print(i)
print("----------")
for i in range(1,6) : # again 6 is not inclusive and 1 is 
    print(i)
print("----------")
for i in range(0,10,2): # 2 is the stepsize
    print(i,end=" ") 
print() 
print("----------")
for i in range(10,1,-1) : # -1 is the step size and 1 is not included
    print(i,end=" ")
print()
print("----------")
for i in range(10,1,-2) : # -2 is the step size and 1 is not included
    print(i,end=" ")
print()
print("----------")
s = "MyNameIsAbhay"
for i in s : 
    print(i,end=" ")
print()
print("----------")
#While loop-->

#the while loop continues to execute as long as the condition is true
count = 0 
while(count<5):
    print(count)
    count+=1 ; 


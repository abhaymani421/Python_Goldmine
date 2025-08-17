# we have already gone through the basics of args and kwargs in functions , here we will look
#at the various ways to use them

def func(arg1,*args):
    print("arg1 :",arg1)
    for i in args : 
        print(i,end=" ")

func(1,2,3,4,5,6,7,8)
print()
print("-----------------")

def func1(*args,**kwargs):
    for i in args : 
        print(i,end=" ")
    print()
    for i,j in kwargs.items():
        print("%s <--> %s" %(i,j))

func1(1,2,3,4,A1="Abhay",A2=22,A3="IITJ",A4="GRADUATED")

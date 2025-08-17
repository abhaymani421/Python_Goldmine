"""
    Recursion is a programming technique where a function calls itself 
    directly or indirectly to solve a problem by breaking it down into 
    smaller subproblems. 

    Key aspects:
    - A base case: defines when the recursion should stop.
    - A recursive case: the function calls itself with modified arguments 
      to move towards the base case.
"""
#recursive code to find nth fibonacchi sequence 
def fib(n) :
    if n==0 or n==1 :#base case
        return n
    return fib(n-1)+fib(n-2)

print(fib(7)) # 0 , 1 , 2 , 3 , 5 , 8 , 13

#recursive code to find factorial of a number
def Factorial(n) : 
    if n<=1 : #base case
        return 1
    return n*Factorial(n-1)
n = int(input("Enter a number to find its factorial : "))
print("The factorial of n is :",Factorial(n))
'''
🔹 1. Tail Recursion

A recursion is called tail recursion if the recursive call is the last thing the function does.

Nothing is left to do after the recursive call returns.

Python does not optimize tail recursion (unlike some languages like Scheme or Haskell), so very deep tail recursion can still cause a RecursionError.

✅ Example (Tail Recursion):

def tail_factorial(n, acc=1):
    """
    Tail recursion example:
    The recursive call is the last statement in the function.
    """
    if n == 0:
        return acc
    return tail_factorial(n - 1, n * acc)  # last action is recursion


Here, after calling tail_factorial, nothing else is left to compute → hence tail recursion.

🔹 2. Non-Tail Recursion

A recursion is non-tail recursion if some computation is still pending after the recursive call.

The function has to “remember” previous states until recursion finishes, so it uses more stack memory.

✅ Example (Non-Tail Recursion):

def factorial(n):
    """
    Non-tail recursion example:
    Multiplication happens after the recursive call returns.
    """
    if n == 0:
        return 1
    return n * factorial(n - 1)  # recursive call is NOT last


Here, after the recursive call, Python still needs to multiply n * result, so it is non-tail recursion.

🔑 Difference in One Line:

Tail recursion: recursive call is the last step → no extra work after return.

Non-tail recursion: recursive call is followed by extra computation.
'''
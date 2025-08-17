def fun1(): # outer function
    a = 45
    
    def fun2(): # inner function
        nonlocal a # without using nonlocal keyword we cannot modufy the outer variable 'a' , and we get a error.
        a+=2
        print(a)
    
    fun2()
    print(a)

fun1()

#Closure-->
def fun1(a):
    """
    Closure in Python:
    ------------------
    A closure is a function (inner function) that remembers the variables
    from the scope in which it was created, even after the outer function
    has finished executing.

    In this example:
    - `fun1` is the outer function that takes a parameter `a`.
    - `fun2` is the inner function that uses `a`.
    - When `fun1` returns `fun2` (without calling it), the returned
      function `closure_func` still remembers the value of `a`.
    - So, even though `fun1` has already finished, `fun2` can still access `a`.

    This is called a **closure**.
    """

    def fun2():
        print(a)
    return fun2


closure_func = fun1("Hello, Closure!")
closure_func()  # Output: Hello, Closure!

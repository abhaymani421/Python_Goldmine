"""
    The filter() function in Python is used to filter elements of an iterable
    (like a list, tuple, or string) based on a condition (a function that returns
    True or False). 
    
    - It takes two arguments:
        1. A function (that checks each element).
        2. An iterable (like a list).
    
    - It returns an iterator containing only those elements for which
      the function returns True.

    Example:
    --------
    numbers = [1, 2, 3, 4, 5, 6]

    # Keep only even numbers
    evens = filter(lambda x: x % 2 == 0, numbers)
    print(list(evens))   # Output: [2, 4, 6]
    """
numbers = [1, 2, 3, 4, 5, 6]

# Keep only even numbers
evens = filter(lambda x: x % 2 == 0, numbers)
print(list(evens))   # Output: [2, 4, 6]

#Using map and filter functions-->
a = [1,2,3,4,5,6,7,8]

odds = list(filter(lambda x : x%2!=0 ,a))

#double the odds->

double_odds = list(map(lambda x : x*2,odds))
print(odds)
print(double_odds)

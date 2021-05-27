'''
#   In Python, we can pass a variable number of arguments to a function using special symbols.
    There are two special symbols:
    1.)*args (Non-Keyword Arguments)
    2.)**kwargs (Keyword Arguments)
    *args and **kwargs allow you to pass multiple arguments or keyword arguments to a function.
    Consider the following example.
'''


def super_function(*args, **kwargs):
    print(args)
    print(kwargs)
    total = 0
    for items in kwargs.values():
        total += items
    return sum(args) + total


print(super_function(1, 2, 3, 4, 5, num1=10, num2=20))

'''
There is a hierarchical order for declaring arguments and that is 
    :parameter, *args, default_parameter, **kwargs.
'''


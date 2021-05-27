'''
#   Scope - It generally refers to what variables do i have access to.
    A variable is only available from inside the region it is created. This is called scope.
#   Local Scope - A variable created inside a function belongs to the local scope of that function,
    and can only be used inside that function.
'''


def my_func():
    x = 200
    print(x)


my_func()

'''
#   Function Inside Function - As explained in the example above, the variable x is not available outside the 
    function, but it is available for any function inside the function:
'''


def my_func():
    x = 300

    def my_innerFunc():
        print(x)

    my_innerFunc()


my_func()

'''
#   Global Scope - A variable created in the main body of the Python code is a global variable and belongs to 
    the global scope. Global variables are available from within any scope, global and local.
'''

x = 20


def my_func1():
    print(x)


my_func1()

print(x)

'''
#   Naming Variables - If you operate with the same variable name inside and outside of a function, 
    Python will treat them as two separate variables, one available in the global scope (outside the function) 
    and one available in the local scope (inside the function).
'''

x = 300


def myfunc():
    x = 200
    print(x)


myfunc()

print(x)

'''
#   Global Keyword - If you need to create a global variable, but are stuck in the local scope, you can use the g
    lobal keyword. The global keyword makes the variable global.
'''


def myfunc():
    global x
    x = 300


myfunc()

print(x)

'''
#   Scope Checking Rules - 1. Start with local scope.
                           2. Parent local scope?
                           3. Global scope?
                           4. Build in python function? 
'''

def my_func():

    def my_innerFunc():
        return sum

    my_innerFunc()


print(my_func())
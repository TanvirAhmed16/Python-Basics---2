'''
#   Global Scope - A variable created in the main body of the Python code is a global variable and belongs to
    the global scope. Global variables are available from within any scope, global and local.
'''

# total = 10
#
# def count():
#     total += 1
#     return total
#
# print(count()) # In this condition the program won't run as total is not declared inside the function.
# So, for handling this error we need to declare that variable inside the function.


total = 0


def count(total):
    # total = 0
    total += 1
    return total


# count()
# count()
# print(count())  # Here we need to count 3 times but this won't count 3 times as every time the
# count function is called, total is set to 0. So we can do this.
print(count(count(count(total))))

# The best way is to use the global variable using global keyword inside the function.

total = 0


def count():
    global total
    total += 1
    return total


count()
count()
count()
print(count())

''' 
THough it is helpful in some situation, but as a good programmer we need to avoid writing this kind of 
program where everything becomes so complicated.
'''

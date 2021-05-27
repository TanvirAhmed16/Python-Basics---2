'''
#   Clean Code - In simple words Clean code is code that is easy to understand and easy to change.
    It basically maintained by the experienced programmer while they code.
'''

# Suppose we need to make a program that check a number whether it is even or not.

def is_even(num):
    if num % 2 == 0:
        return True
    elif num % 2 != 0:
        return False
print(is_even(50))

# We can make this function more clean.
def is_even(num):
    if num % 2 == 0:
        return True
    # As first condition is false, so it doesn't need to check the second condition.
    #elif num % 2 != 0:
        #return False
    else:
        return False
print(is_even(5))

# More Cleaner

def is_even(num):
    if num % 2 == 0:
        return True
    return False
print(is_even(50))

# More Cleaner
# As it is returning a boolean value, so we can evaluate it as an expression.
def is_even(num):
    return num % 2 == 0

print(is_even(51))
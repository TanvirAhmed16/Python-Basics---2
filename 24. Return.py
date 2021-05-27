'''
# We need to remember very well that
    A function should do specific operations very well.
    A function should return something corresponding to the specified operations.
    As soon as a function return anything, it exits the function.
'''


def sum(num1, num2):
    num1 + num2  # It won't return anything unless we use return keyword.
    #return num1 + num2


#total = sum(10, 5)  # We can also store sunction in a variable.
print(sum(10, 5))

def sum1(num1, num2):
    return num1 + num2


total = sum1(10, 5)  # We can also store function in a variable.
print(sum1(10, total))

# We can also create nested function.
def add(num1, num2):
    def another_function(n1, n2):
        return n1 + n2
    # If we call this function in this situation then it won't return anything as 1st function doesn't return
    # anything.
    return another_function(num1, num2)

print(add(25, 35))

# No operation is executed inside a function after return.
def say_hi():
    return 'Hiiiiiii'
    print('Hello')

print(say_hi())






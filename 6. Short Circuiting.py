'''
By short circuiting we mean the stoppage of execution of boolean operation if the truth value of
expression has been determined already. The evaluation of expression takes place from left to right.
In python, short circuiting is supported by various boolean operators and functions.
'''
'''
and: For an and expression, Python uses a short circuit technique to check if the first statement
is false then the whole statement must be false, so it returns that value. Only if the first value is
true, it checks the second statement and returns the value.
'''
is_friend = True
is_user = True
if is_friend and is_user: # Here both conditions will be checked by the interpreter.
    print("Friends Forever.")
else:
    print("Be My Friend.")

is_friend = False
is_user = True
if is_friend and is_user:
    '''Here both conditions won't be checked by the interpreter as is_friend is false, 
    so there is no way for the both conditions will be true. That's why interpreter won't 
    check the is_user condition.
    '''
    print("Friends Forever.")
else:
    print("Be My Friend.")

'''
or: When the Python interpreter scans or expression, it takes first statement and checks to see if it is true. 
If the first statement is true, then Python returns that object’s value without checking the second statement. 
The program does not bother with the second statement. 
If the first value is false, only then Python checks the second value and then result is based on second half.
'''
is_friend = True
is_user = True
if is_friend or is_user: # Here only is_friend condition will be checked by the interpreter.
    print("Friends Forever.")
else:
    print("Be My Friend.")

is_friend = False
is_user = True
if is_friend or is_user: # Here 2nd condition will be checked by the interpreter.
    print("Friends Forever.")
else:
    print("Be My Friend.")

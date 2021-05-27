'''
In Python, While Loops is used to execute a block of statements repeatedly until a given condition is
satisfied.And when the condition becomes false, the line immediately after the loop in the program is executed.
While loop falls under the category of indefinite iteration.
Indefinite iteration means that the number of times the loop is executed isn’t specified explicitly in advance.

Syntax:
while expression:
    statement(s)
'''

i = 0
while i < 10:
    print(i)
    break  # If we don't use break here then it will be an Infinite loop. So we need to be careful.
while i < 20:
    print(i)
    i = i + 1  # or i +=1
    # break -If we use this break here then else won't be executed. So else is a special case below.
else:
    print('Done with loops.')

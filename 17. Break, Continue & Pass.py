'''
# Break statement - The break statement is used to terminate the loop or statement in which it is present.
After that, the control will pass to the statements that are present after the break statement, if available.
If the break statement is present in the nested loop, then it terminates only those loops which contains
break statement.
'''

for letters in "Python":
    print(letters)
    if letters == "h":
        break

i = 5
while i > 0:
    print(f"Current value is :", {i})
    i -= 1
    if i == 2:
        break

'''
Continue Statement - The continue statement in Python returns the control to the beginning of the while loop. 
The continue statement rejects all the remaining statements in the current iteration of the loop and moves 
the control back to the top of the loop.
The continue statement can be used in both while and for loops.
'''
for letters in "Python":
    print(letters)
    if letters == "h":
        continue

i = 5
while i > 0:
    print(f"Current value is :", {i})
    i -= 1
    if i == 2:
        continue

# Python program to
# demonstrate continue
# statement

# loop from 1 to 10
for i in range(1, 11):

    # If i is equals to 6,
    # continue to next iteration
    # without printing
    if i == 6:
        continue
    else:
        # otherwise print the value
        # of i
        print(i)

'''
Pass statement - As the name suggests pass statement simply does nothing. The pass statement in Python is used 
when a statement is required syntactically but you do not want any command or code to execute. 
The pass statement is a null operation; nothing happens when it executes. The pass is also useful in 
places where your code will eventually go, but has not been written yet (e.g., in stubs for example):
'''
for letters in 'Python':
    if letters == 't':
        pass
        print("This is pass block")
    print(letters)
# Another example
my_list = [1, 2, 3]
for item in my_list:
    # Thinking about it...
    pass  # If we don't use pass here then program will show error as for loop won't be complete.
i = 0
while i < len(my_list):
    print(my_list[i])
    i += 1

'''
# When to use for loop and when to use while loop????
    In general for simple loops or iterating over iterable objects for loops are great. On the other hand
    While you are not sure of how many times you want to loop over, then based on the condition it is better
    to use while loop.
    But we need to remember when we are using while loop we need to be careful of not making a loop infinite.
'''


my_list = [1, 2, 3]

for i in my_list:
    print(i)

i = 0
while i < len(my_list):
    print(my_list[i])
    i += 1

# One of the useful ways of using while loop is like below...

while True:
    response = input("Say something:")
    if response == "Bye":
        break

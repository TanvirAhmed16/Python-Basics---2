'''
A lot of times when dealing with iterators, we also get a need to keep a count of iterations.
Python eases the programmers’ task by providing a built-in function enumerate() for this task.
Enumerate() method adds a counter to an iterable and returns it in a form of enumerate object.
This enumerate object can then be used directly in for loops or be converted into a list of
tuples using list() method.
'''
for char in enumerate('Heellooo'):
    print(char)
for i, char in enumerate('Heellooo'):
    print(i, char)
# List
for i, char in enumerate([1, 2, 3]):
    print(i, char)
# Set
for i, char in enumerate({1, 2, 3}):
    print(i, char)
# Tuple
for i, char in enumerate((1, 2, 3)):
    print(i, char)

# Let's do an exercise. We need to find the index of 50 of a range 0-100.

for i, char in enumerate (list(range(100))):
    print(i,char)
    if char == 50:
        print(f'Index of {char} is: {i}')
print('Happy Coding...:-)')

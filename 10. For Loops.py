'''
Loops are generally used to do same work multiple times.
'''

for letters in "Tan":
    print(letters)
# Applying on List
friends = ['Tanvir', 'Rohit', 'Parosh']
for names in friends:
    print(names)
for values in [1, 2, 3]:
    print(values)
# Applying on Sets. We can also print in same line.
for values in {1, 2, 3}:
    print(values)
# Applying in Tuple
for values in (1, 2, 3):
    print(values)
    print(values) # Printing values 2 times

# Making Loops nested. (Nested loops means loop inside a loop.)
for values in [1, 2, 3]:
    for characters in ['a', 'b', 'c']:
        print(values, characters)
print("Happy Coding.")
'''
# We need to find the duplicate value item in the list given below and we can't use set.
'''

some_list = ['a', 'b', 'c', 'b', 'd', 'm', 'n', 'n']
count = 0
for item in some_list:
    if item == 'a':
        count += 1
if count > 1:
    print(f'a has duplicates.')
else:
    print(f'a is unique.')

count = 0
for item in some_list:
    if item == 'b':
        count += 1
if count > 1:
    print(f'b has duplicates.')
else:
    print(f'b is unique.')

count = 0
for item in some_list:
    if item == 'c':
        count += 1
if count > 1:
    print(f'c has duplicates.')
else:
    print(f'c is unique.')

count = 0
for item in some_list:
    if item == 'd':
        count += 1
if count > 1:
    print(f'd has duplicates.')
else:
    print(f'd is unique.')

count = 0
for item in some_list:
    if item == 'm':
        count += 1
if count > 1:
    print(f'm has duplicates.')
else:
    print(f'm is unique.')

count = 0
for item in some_list:
    if item == 'n':
        count += 1
if count > 1:
    print(f'n has duplicates.')
else:
    print(f'n is unique.')

'''
# One of the optimal solution is 
some_list = ['a', 'b', 'c', 'b', 'd', 'm', 'n', 'n']

duplicates = []
for value in some_list:
    if some_list.count(value) > 1:
        if value not in duplicates:
            duplicates.append(value)

print(duplicates)
'''
some_list = ['a', 'b', 'c', 'b', 'd', 'm', 'n', 'n']

duplicates = []
for item in some_list:
    some_list.count(item)
    if some_list.count(item) > 1:
        # print(f'{item} has duplicates value.')
        if item not in duplicates:
            duplicates.append(item)
print(duplicates)
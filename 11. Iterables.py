'''
Iterables - String, List, Set, Tuple, Dictionary.
Iterate -  One by One check items in the collection.
'''
user = {
    'name': 'Tan',
    'age': 25,
    'can_swim': True
}
for item in user:
    print(item)
'''
Dictionary uses 3 methods for accessing its values.
'''
for item in user.items():
    print(item)
# As .items() returns tuples. So we can separate them using tuple unpacking.
for item in user.items():
    keys, values = item
    print(keys, values)  # or
for keys, values in user.items():
    print(keys, values)

for item in user.values():
    print(item)

for item in user.keys():
    print(item)
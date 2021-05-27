# Count items and Find sum of a list items.

my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

counter = 0
print(f'I have', len(my_list), 'items in my list.')
for item in my_list:
    counter = counter + item
print(f'Total sum of the items is', counter)
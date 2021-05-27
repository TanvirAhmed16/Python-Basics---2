'''
# We need to find the highest even number from a given list.
'''


def highest_even(li):
    print(li)
    new_li = []
    for item in li:
        if item % 2 == 0:
            new_li.append(item)
    return max(new_li)


print(highest_even([1, 3, 4, 5, 6]))

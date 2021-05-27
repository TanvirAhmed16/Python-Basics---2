"""
Any object can be tested for truth value, for use in an if or while condition
or as operand of the Boolean operations.
it just refers to values which are evaluated to True or False.

For instance, to see if a list is not empty, instead of checking like this:

"""
my_list = [1, 2, 3]

if len(my_list) != 0:
   print("Not empty!")
# You can simply do this:

my_list = []

if my_list:
   print("Not empty!")
else:
    print(f'It\'s an empty list.')

"""
All values are considered "truthy" except for the following, which are "falsy":

None
False
0
0.0
0j
Decimal(0)
Fraction(0, 1)
[] - an empty list
{} - an empty dict
() - an empty tuple
'' - an empty str
b'' - an empty bytes
set() - an empty set
an empty range, like range(0)
objects for which
obj.__bool__() returns False
obj.__len__() returns 0
A "truthy" value will satisfy the check performed by if or while statements. 
We use "truthy" and "falsy" to differentiate from the bool values True and False.
"""

user_name = "Tanvir"
password = 123

if user_name and password:
    print("You are allowed to continue to this account.")
else:
    print("You need to have valid user_name and password.")

print("Happy Coding... :-)")
'''
#   Python Docstrings - Python documentation strings (or docstrings) provide a convenient way of associating
    documentation with Python modules, functions, classes, and methods.
#   It’s specified in source code that is used, like a comment, to document a specific segment of code.
    Unlike conventional source code comments, the docstring should describe what the function does, not how.

#   Declaring Docstrings: The docstrings are declared using ”’triple single quotes”’ or “””triple double
    quotes””” just below the class, method or function declaration. All functions should have a docstring.

#   Accessing Docstrings: The docstrings can be accessed using the __doc__ method of the object
    or using the help function.
'''


def test(a):
    '''
    This function test and prints param a.
    :param a:
    :return:
    '''

    print(a)


# We can access this function in many ways.
test('!!!')
help(test)
print(test.__doc__)

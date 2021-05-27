'''
# Nonlocal Keyword - It basically refers to the parent local scope of a function.
'''


def outer():
    x = 'local'

    def inner():
        nonlocal x  # This nonlocal keyword says whatever are in the parent or outer function, i want to grab those.
        # So, this refers to the parent local x.
        x = 'nonlocal'  # Here the x is replaced to 'nonlocal' from 'local'
        print('Inner', x)

    inner()
    print('Outer', x)


outer()


# If we comment out this nonlocal keyword then this will happen.

def outer():
    x = 'local'

    def inner():
        # nonlocal x  # This nonlocal keyword says whatever are in the parent or outer function, i want to grab those.
        # So, this refers to the parent local x.
        x = 'nonlocal'  # Here the x is replaced to 'nonlocal' from 'local'
        print('Inner', x)

    inner()
    print('Outer', x)


outer()
y = 'hello'
print(y)
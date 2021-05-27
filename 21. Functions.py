'''
A function is a block of code which only runs when it is called. You can pass data, known as parameters,
into a function. A function can return data as a result.
In Python a function is defined using the def keyword:
'''


def say_hello():
    print('Hellllloooooooo')

for len in 'Hi':
    say_hello()

picture = [
    [0, 0, 0, 1, 0, 0, 0],
    [0, 0, 1, 1, 1, 0, 0],
    [0, 1, 1, 1, 1, 1, 0],
    [1, 1, 1, 1, 1, 1, 1],
    [0, 0, 0, 1, 0, 0, 0],
    [0, 0, 0, 1, 0, 0, 0]
]
def draw_tree():
    for row in picture:
        for pixel in row:
            if pixel == 0:
                print(' ', end='')
            else:
                print('*', end='')
        print('')
i = 0
while i < 3:
    draw_tree()
    i += 1
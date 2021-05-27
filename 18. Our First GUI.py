'''Exercise!
# Display the image below to the right hand side where the 0 is going to be ' ',
# and the 1 is going to be '*'. This will reveal an image!
'''
picture = [
    [0, 0, 0, 1, 0, 0, 0],
    [0, 0, 1, 1, 1, 0, 0],
    [0, 1, 1, 1, 1, 1, 0],
    [1, 1, 1, 1, 1, 1, 1],
    [0, 0, 0, 1, 0, 0, 0],
    [0, 0, 0, 1, 0, 0, 0]
]

for item in picture[0]:
    if item == 0:
        print(' ', end='')
    else:
        print('*', end='')
print('')
for item in picture[1]:
    if item == 0:
        print(' ', end='')
    else:
        print('*', end='')
print('')
for item in picture[2]:
    if item == 0:
        print(' ', end='')
    else:
        print('*', end='')
print('')
for item in picture[3]:
    if item == 0:
        print(' ', end='')
    else:
        print('*', end='')
print('')
for item in picture[4]:
    if item == 0:
        print(' ', end='')
    else:
        print('*', end='')
print('')
for item in picture[5]:
    if item == 0:
        print(' ', end='')
    else:
        print('*', end='')
print('')

# Short Code
for row in picture:
    for pixel in row:
        if pixel == 0:
            print(' ', end='')
        else:
            print('*', end='')
    print('')
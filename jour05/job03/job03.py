def draw_hollow_triangle(height):

    print(' ' * (height - 1) + '/\\')

    for i in range(1, height - 1):
        spaces = ' ' * (height - i - 1)
        middle_spaces = ' ' * (2 * i - 1)
        print(spaces + '/' + middle_spaces + '\\')

    if height > 1:
        print('/' + '_' * (2 * height - 3) + '\\')

draw_hollow_triangle(5)

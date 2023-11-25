def draw_diagonal_carpet(n):
    print(' ' + '-' * (n + 2) + '+')

    for i in range(n):
        print('|' + ' ' * (n - i) + '#' * (i + 1) + ' |')
        print('+' + '-' * (n + 2) + '+')

draw_diagonal_carpet(10)

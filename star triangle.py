for i in range(1, n + 1):
    print('*' * i)

for i in range(n):
    print(' ' * (n - i - 1), end='')
    print('*' * (2 * i + 1))

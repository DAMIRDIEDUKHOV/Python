height = int(input("Enter the height of the Christmas tree: "))

for i in range(height):
    print(' ' * (height - i - 1) + '*' * (2 * i + 1))
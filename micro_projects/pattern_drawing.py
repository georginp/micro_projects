def right_angled_trianlge():
    rows = int(input("Please enter number of rows: "))
    for num in range(rows + 1):
        print("*" * num)


def square_with_hollow_center():
    size_square = int(input("Please enter size of the square: "))
    for i in range(size_square):
        for j in range(size_square):
            if (i == 0 or i == size_square - 1 or j == 0 or j == size_square - 1):
                print('*', end='')
            else:
                print(' ', end='')
        print()


def diamond_pattern():
    number_rows = int(input("Please enter height for the diamond: "))
    for i in range(1, number_rows + 1):
        i = i - (number_rows//2 + 1)
        if i < 0:
            i = -i
        print(" " * i + "*" * (number_rows - i*2) + " "*i)

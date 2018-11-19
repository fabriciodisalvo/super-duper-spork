from checker import sudoku_check


def sudoku_display(sudoku_map):
    print(" -" * 12)
    for y in range(9):
        print("|", end=" ")
        for i in range(3):
            print(sudoku_map[y * 9 + 0 + i * 3],
                  sudoku_map[y * 9 + 1 + i * 3],
                  sudoku_map[y * 9 + 2 + i * 3], "|", end=" ")
        print()
        if (y + 1) % 3 == 0:
            print(" -" * 12)


def input_check(sudoku_map):
    if len(sudoku_map) != 81:
        print(' Sudoku provided is not 81 numbers long...')
    elif sudoku_map.count(0) != 0:
        print(' Sudoku provided contains zeros...')
    else:
        return True


def main():
    sudoku_map = [1, 2, 3, 4, 5, 6, 7, 8, 8,
                  7, 8, 9, 1, 2, 3, 4, 5, 6,
                  4, 5, 6, 7, 8, 9, 1, 2, 3,
                  3, 1, 2, 8, 4, 5, 9, 6, 7,
                  6, 9, 7, 3, 1, 2, 8, 4, 5,
                  8, 4, 5, 6, 9, 7, 3, 1, 2,
                  2, 3, 1, 5, 7, 4, 6, 9, 8,
                  9, 6, 8, 2, 3, 1, 5, 7, 4,
                  5, 7, 4, 9, 6, 8, 2, 3, 1]
    if input_check(sudoku_map):
        print('\n Sudoku provided: ')
        sudoku_display(sudoku_map)
        print()
        if sudoku_check(sudoku_map):
            pass
        else:
            print(' Keep trying')
            # Placeholder for solver method


if __name__ == "__main__":
    main()

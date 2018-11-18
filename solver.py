
def sodoku_display(sudoku_map):
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


def group_validate(group_to_check):
    if sum(group_to_check) != 45:
        return False
    for i in group_to_check:
        if group_to_check.count(i) != 1:
            return False
    return True


def sudoku_check(sudoku_map):
    if len(sudoku_map) == 81:

        sodoku_display(sudoku_map)

        for i in range(9):
            line_to_check = sudoku_map[(i * 9 + 0):(i * 9 + 9)]
            if group_validate(line_to_check):
                print('Line {} : {} : Group is OK.'.format(i + 1, line_to_check))

        for y in range(9):
            column_to_check = [sudoku_map[num] for num in range(81) if num % 9 == y]
            if group_validate(column_to_check):
                print('Column {} : {} : Group is OK.'.format(y + 1, column_to_check))

    else:
        print(' len is not ok')


def main():
    sudoku_map = [1, 2, 3, 4, 5, 6, 7, 8, 9,
                  7, 8, 9, 1, 2, 3, 4, 5, 6,
                  4, 5, 6, 7, 8, 9, 1, 2, 3,
                  3, 1, 2, 8, 4, 5, 9, 6, 7,
                  6, 9, 7, 3, 1, 2, 8, 4, 5,
                  8, 4, 5, 6, 9, 7, 3, 1, 2,
                  2, 3, 1, 5, 7, 4, 6, 9, 8,
                  9, 6, 8, 2, 3, 1, 5, 7, 4,
                  5, 7, 4, 9, 6, 8, 2, 3, 1]
    sudoku_check(sudoku_map)


if __name__ == "__main__":
    main()

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


def group_validate(group_to_check):
    if sum(group_to_check) != 45:
        return False
    for i in group_to_check:
        if group_to_check.count(i) != 1:
            return False
    return True


def sudoku_solver(sudoku_map):
    print(' Sudoku provided: ')
    sudoku_display(sudoku_map)
    print(' Sudoku solved: ')
    sudoku_display(sudoku_map)
    return sudoku_map


def sudoku_check(sudoku_map):
    if len(sudoku_map) != 81:
        print(' Sudoku provided is not 81 numbers long...')
    elif sudoku_map.count(0) != 0:
        print(' Sudoku provided contains zeros...')
    else:
        sudoku_map_solved = sudoku_solver(sudoku_map)
#       Perform validation line by line:
        for i in range(9):
            line_to_check = sudoku_map_solved[(i * 9 + 0):(i * 9 + 9)]
            if group_validate(line_to_check):
                print('Line   {} : {} : Group is OK.'.format(i + 1, line_to_check))
#       Perform validation column by column:
        for y in range(9):
            column_to_check = [sudoku_map[num] for num in range(81) if num % 9 == y]
            if group_validate(column_to_check):
                print('Column {} : {} : Group is OK.'.format(y + 1, column_to_check))
#       Perform validation square by square:
        square_number = 0
        for z in range(0, 9, 3):
            for w in range(0, 9, 3):
                square_number += 1
                square_to_check = sudoku_map[((z + 0) * 9 + w):((z + 0) * 9 + w + 3)] + sudoku_map[((z + 1) * 9 + w):((z + 1) * 9 + w + 3)] + sudoku_map[((z + 2) * 9 + w):((z + 2) * 9 + w + 3)]
                if group_validate(square_to_check):
                    print('Square {} : {} : Group is OK.'.format(square_number, square_to_check))

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

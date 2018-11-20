from checker import sudoku_check
from solver import sudoku_solver
from display import sudoku_display


def input_check(sudoku_map):
    if len(sudoku_map) != 81:
        print(' Sudoku provided is not 81 positions long...')
    elif sudoku_map.count(0) != 0:
        print(' Sudoku provided contains zeros...')
    else:
        return True


def main():
    sudoku_map = [1, 2, 3, 'X', 5, 6, 7, 8, 9,
                  7, 8, 9, 1, 2, 3, 4, 5, 'X',
                  4, 5, 6, 7, 8, 9, 1, 2, 3,
                  3, 1, 2, 8, 4, 'X', 9, 6, 7,
                  6, 9, 7, 3, 1, 2, 8, 4, 5,
                  8, 'X', 5, 6, 9, 7, 3, 1, 2,
                  2, 3, 1, 5, 7, 4, 6, 9, 8,
                  9, 6, 8, 2, 3, 1, 5, 7, 4,
                  5, 7, 4, 9, 6, 8, 'X', 3, 1]
    if input_check(sudoku_map):
        print('\n Sudoku provided: ')
        sudoku_display(sudoku_map)
        print()
        if sudoku_check(sudoku_map):
            print()
            print(' Sudoku solved: ')
            sudoku_display(sudoku_test_map)
        else:
            sudoku_solver(sudoku_map)


if __name__ == "__main__":
    main()

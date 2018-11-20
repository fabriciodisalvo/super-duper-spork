from checker import group_validate
from checker import sudoku_check
from display import sudoku_display


def sudoku_solver(sudoku_map):
    possible_guesses = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    squares = [[0, 1, 2, 9, 10, 11, 18, 19, 20],
               [3, 4, 5, 12, 13, 14, 21, 22, 23],
               [6, 7, 8, 15, 16, 17, 24, 25, 26],
               [27, 28, 29, 36, 37, 38, 45, 46, 47],
               [30, 31, 32, 39, 40, 41, 48, 49, 50],
               [33, 34, 35, 42, 43, 44, 51, 52, 53],
               [54, 55, 56, 63, 64, 65, 72, 73, 74],
               [57, 58, 59, 66, 67, 68, 75, 76, 77],
               [60, 61, 62, 69, 70, 71, 78, 79, 80]]
    sudoku_test_map = sudoku_map
    try:
        last_changed_position = sudoku_map.index('X')
        for i in possible_guesses:
            sudoku_test_map[last_changed_position] = i
            line_location = (last_changed_position // 9) * 9
            line_to_check = sudoku_test_map[line_location:line_location + 9]
            if group_validate(line_to_check):
                column_location = last_changed_position % 9
                column_to_check = [sudoku_test_map[num]
                                   for num in range(81) if num % 9 == column_location]
                if group_validate(column_to_check):
                    for s in squares:
                        if last_changed_position in s:
                            square_to_check = [sudoku_test_map[x] for x in s]
                            if group_validate(square_to_check):
                                sudoku_solver(sudoku_test_map)
    except ValueError:
        sudoku_check(sudoku_test_map)
        print()
        print(' Sudoku solved: ')
        sudoku_display(sudoku_test_map)
        return sudoku_test_map

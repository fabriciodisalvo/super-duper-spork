from solver import sudoku_solver
from display import sudoku_display


sudoku_map_list = {
    'completed': [1, 2, 3, 4, 5, 6, 7, 8, 9,
                  7, 8, 9, 1, 2, 3, 4, 5, 6,
                  4, 5, 6, 7, 8, 9, 1, 2, 3,
                  3, 1, 2, 8, 4, 5, 9, 6, 7,
                  6, 9, 7, 3, 1, 2, 8, 4, 5,
                  8, 4, 5, 6, 9, 7, 3, 1, 2,
                  2, 3, 1, 5, 7, 4, 6, 9, 8,
                  9, 6, 8, 2, 3, 1, 5, 7, 4,
                  5, 7, 4, 9, 6, 8, 2, 3, 1],
    'dispersed': [1, 2, 3, 'X', 5, 6, 7, 8, 9,
                  7, 8, 9, 1, 2, 3, 4, 5, 'X',
                  4, 5, 6, 7, 8, 9, 1, 2, 3,
                  3, 1, 2, 8, 4, 'X', 9, 6, 7,
                  6, 9, 7, 3, 1, 2, 8, 4, 5,
                  8, 'X', 5, 6, 9, 7, 3, 1, 2,
                  2, 3, 1, 5, 7, 4, 6, 9, 8,
                  9, 6, 8, 2, 3, 1, 5, 7, 4,
                  5, 7, 4, 9, 6, 8, 'X', 3, 1],
    'two_group': [1, 2, 3, 4, 5, 6, 7, 8, 9,
                  7, 8, 'X', 1, 2, 3, 'X', 5, 6,
                  4, 5, 6, 7, 8, 9, 1, 2, 3,
                  3, 1, 2, 8, 4, 5, 9, 6, 7,
                  6, 9, 'X', 3, 1, 2, 8, 4, 5,
                  8, 4, 5, 6, 9, 7, 3, 1, 2,
                  2, 3, 1, 5, 7, 4, 6, 9, 8,
                  9, 6, 8, 2, 3, 1, 5, 7, 4,
                  5, 7, 4, 9, 6, 8, 2, 3, 1]
}

for sudoku in sudoku_map_list.keys():
    print()
    print(' Sudoku provided: ')
    print(' Type: {}'.format(sudoku))
    sudoku_display(sudoku_map_list[sudoku])
    sudoku_solver(sudoku_map_list[sudoku])

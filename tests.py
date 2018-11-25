from sudoku_class import Sudoku
from solver_class import Solver


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
                  5, 7, 4, 9, 6, 8, 2, 3, 1],
    'half_miss': ['X', 2, 'X', 4, 'X', 6, 7, 'X', 9,
                  7, 8, 'X', 1, 'X', 3, 'X', 5, 6,
                  4, 5, 6, 7, 8, 9, 1, 2, 3,
                  3, 1, 2, 'X', 4, 5, 'X', 6, 7,
                  6, 9, 'X', 3, 1, 2, 8, 4, 5,
                  8, 4, 5, 6, 9, 7, 3, 1, 2,
                  2, 3, 1, 'X', 7, 'X', 'X', 9, 8,
                  9, 6, 'X', 'X', 'X', 1, 'X', 7, 4,
                  5, 7, 'X', 9, 6, 'X', 2, 3, 1],
    'real_test': ['X', 'X', 'X', 'X', 'X', 4, 'X', 9, 'X',
                  8, 'X', 2, 9, 7, 'X', 'X', 'X', 'X',
                  9, 'X', 1, 2, 'X', 'X', 3, 'X', 'X',
                  'X', 'X', 'X', 'X', 4, 9, 1, 5, 7,
                  'X', 1, 3, 'X', 5, 'X', 9, 2, 'X',
                  5, 7, 9, 1, 2, 'X', 'X', 'X', 'X',
                  'X', 'X', 7, 'X', 'X', 2, 6, 'X', 3,
                  'X', 'X', 'X', 'X', 3, 8, 2, 'X', 5,
                  'X', 2, 'X', 5, 'X', 'X', 'X', 'X', 'X']
}

# for i in sudoku_map_list.keys():
#     this_sudoku = Sudoku(sudoku_map_list[i])
#     print()
#     print(' Sudoku provided: ')
#     this_sudoku.display()
#     sudoku_solved = Solver.solve(Solver, this_sudoku)


this_sudoku = Sudoku(sudoku_map_list['real_test'])
print()
print(' Provided:')
this_sudoku.display()
print()
sudoku_solved = Solver()
sudoku_solved.solve_test_02(this_sudoku)

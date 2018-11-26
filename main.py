from sudoku_class import Sudoku
from solver_class import Solver


def main():
    sudoku_map = ['X', 'X', 'X', 'X', 'X', 4, 'X', 9, 'X',
                  8, 'X', 2, 9, 7, 'X', 'X', 'X', 'X',
                  9, 'X', 1, 2, 'X', 'X', 3, 'X', 'X',
                  'X', 'X', 'X', 'X', 4, 9, 1, 5, 7,
                  'X', 1, 3, 'X', 5, 'X', 9, 2, 'X',
                  5, 7, 9, 1, 2, 'X', 'X', 'X', 'X',
                  'X', 'X', 7, 'X', 'X', 2, 6, 'X', 3,
                  'X', 'X', 'X', 'X', 3, 8, 2, 'X', 5,
                  'X', 2, 'X', 5, 'X', 'X', 'X', 'X', 'X']
    this_sudoku = Sudoku(sudoku_map)
    print()
    print(' Sudoku provided: ')
    this_sudoku.display()
    print()
    sudoku_solved = Solver()
    sudoku_solved.solve(this_sudoku.sudoku_map)


if __name__ == "__main__":
    main()

from sudoku_class import Sudoku
from solver_class import Solver


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
    this_sudoku = Sudoku(sudoku_map)
    print()
    print(' Sudoku provided: ')
    this_sudoku.display()
    sudoku_solved = Solver.solve(Solver, this_sudoku)
    return sudoku_solved


if __name__ == "__main__":
    main()

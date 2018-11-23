class Sudoku:
    def display(self):
        sudoku_map = self.sudoku_map
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

    def __init__(self, sudoku_map):
        if len(sudoku_map) != 81:
            print(' Sudoku provided is not 81 positions long...')
        elif sudoku_map.count(0) != 0:
            print(' Sudoku provided contains zeros...')
        else:
            self.sudoku_map = sudoku_map
            self.sudoku_map_in_progress = sudoku_map

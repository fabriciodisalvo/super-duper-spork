class Sudoku:
    def display(self):
        sudoku_map = self.sudoku_map
        display_version_map = [x if x != 0 else ' ' for x in sudoku_map]
        print(" -" * 12)
        for y in range(9):
            print("|", end=" ")
            for i in range(3):
                print(display_version_map[y * 9 + 0 + i * 3],
                      display_version_map[y * 9 + 1 + i * 3],
                      display_version_map[y * 9 + 2 + i * 3], "|", end=" ")
            print()
            if (y + 1) % 3 == 0:
                print(" -" * 12)

    def __init__(self, sudoku_map):
        if len(sudoku_map) != 81:
            print(' Sudoku provided is not 81 positions long...')
        # ADD MORE INPUT VALIDATION RULES !
        else:
            self.sudoku_map = sudoku_map

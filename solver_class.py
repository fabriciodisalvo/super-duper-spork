from sudoku_class import Sudoku


class Solver:
    def __init__(self):
        self.path_list = []

    def find_related_groups(self, location):
        current_line_to_check = list(range(((location // 9) * 9), ((location // 9) * 9 + 9)))
        squares = [[0, 1, 2, 9, 10, 11, 18, 19, 20],
                   [3, 4, 5, 12, 13, 14, 21, 22, 23],
                   [6, 7, 8, 15, 16, 17, 24, 25, 26],
                   [27, 28, 29, 36, 37, 38, 45, 46, 47],
                   [30, 31, 32, 39, 40, 41, 48, 49, 50],
                   [33, 34, 35, 42, 43, 44, 51, 52, 53],
                   [54, 55, 56, 63, 64, 65, 72, 73, 74],
                   [57, 58, 59, 66, 67, 68, 75, 76, 77],
                   [60, 61, 62, 69, 70, 71, 78, 79, 80]]
        for square in squares:
            if location in square:
                current_square_to_check = square
        current_column_to_check = [num for num in range(81) if num % 9 == location % 9]
        all_relatives = current_line_to_check
        for x in current_column_to_check:
            if x not in all_relatives:
                all_relatives.append(x)
        for y in current_square_to_check:
            if y not in all_relatives:
                all_relatives.append(y)
        all_relatives.remove(location)
        return(all_relatives)

    def solve_version_01(self, sudoku_input_map):
        sudoku_map = sudoku_input_map
        possible_guesses = [1, 2, 3, 4, 5, 6, 7, 8, 9]
        try:
            last_changed_position = sudoku_map.index(0)
            all_relatives = self.find_related_groups(last_changed_position)
            all_relative_values = [sudoku_map[x] for x in all_relatives]
            possible_guesses_for_this_location = [x for x in possible_guesses if x not in all_relative_values]
            if len(possible_guesses_for_this_location) > 0:
                for x in possible_guesses_for_this_location:
                    self.path_list.append(last_changed_position + 1)
                    print(' Position : {}'.format(last_changed_position))  # remove after testing
                    print(' Possible values : {}'.format(possible_guesses_for_this_location))  # remove after testing
                    print(' Setting {} in position {}'.format(x, last_changed_position))  # remove after testing
                    print()
                    sudoku_map[last_changed_position] = x
                    if self.solve_version_01(sudoku_map):
                        return True
                print(' Position : {}'.format(last_changed_position))  # remove after testing
                print(' Exhausted all choices for this position. Backtracking...')  # remove after testing
                sudoku_map[last_changed_position] = 0  # LATEST TESTING
                print()
            else:
                print(' Position : {}'.format(last_changed_position))  # remove after testing
                print(' No valid options for this position, backtracking...')  # remove after testing
                sudoku_map[last_changed_position] = 0  # LATEST TESTING
                print()
        except ValueError:
            print()
            print(' Solved:')
            solved_sudoku = Sudoku(sudoku_map)
            solved_sudoku.display()
            print()
            print(' Path walked : {}'.format(self.path_list))
            print(' Path lenght : {}'.format(len(self.path_list)))
            print()
            return True

    def solve_version_02(self, sudoku_input_map):
        return

    def solve(self, sudoku_input_map):
        self.solve_version_01(sudoku_input_map)

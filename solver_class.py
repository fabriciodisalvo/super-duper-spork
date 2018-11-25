from sudoku_class import Sudoku


class Solver:

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

    def group_validate(self, group_to_check):
        try:
            if sum(group_to_check) != 45:
                return False
        except TypeError:
            pass
        # if 'X' in group_to_check:
        #     return False
        for i in group_to_check:
            if i == 'X':
                return False
            if group_to_check.count(i) != 1:
                return False
        return True

    def solve_test_02(self, sudoku_input_map):
        sudoku_map = sudoku_input_map
        print('NEW INSTANCE ', '_' * 25)
        print(sudoku_map)
        print()
        possible_guesses = [1, 2, 3, 4, 5, 6, 7, 8, 9]
        try:
            last_changed_position = sudoku_map.index('X')
            all_relatives = self.find_related_groups(last_changed_position)
            all_relative_values = [sudoku_map[x] for x in all_relatives]
            possible_guesses_for_this_location = [x for x in possible_guesses if x not in all_relative_values]
            if len(possible_guesses_for_this_location) > 0:
                for x in possible_guesses_for_this_location:
                    print('Position : {}'.format(last_changed_position))  # remove after testing
                    print('Relatives : {}'.format(all_relatives))  # remove after testing
                    print('Relative values : {}'.format(all_relative_values))  # remove after testing
                    print('Possible values : {}'.format(possible_guesses_for_this_location))  # remove after testing
                    print('Setting {} in position {}'.format(x, last_changed_position))  # remove after testing
                    print()
                    sudoku_map[last_changed_position] = x
                    self.solve_test_02(sudoku_map)
                print('Position : {}'.format(last_changed_position))  # remove after testing
                print('No more choices for this position.')  # remove after testing
                sudoku_map[last_changed_position] = 'X'  # LATEST TESTING
                print()
            else:
                print('Position : {}'.format(last_changed_position))  # remove after testing
                print('No choices, backtracking...')  # remove after testing
                sudoku_map[last_changed_position] = 'X'  # LATEST TESTING
                print()
        except ValueError:
            print()
            print(' Solved:')
            solved_sudoku = Sudoku(sudoku_input_map)
            solved_sudoku.display()
            return(solved_sudoku)

    def solve_test_01(self, sudoku_input):
        sudoku_map = sudoku_input.sudoku_map
        possible_guesses = [1, 2, 3, 4, 5, 6, 7, 8, 9]
        important_neighbours = {}
        positions = range(len(sudoku_map))
        for position in positions:
            partial_list = []
            print("Position {}.".format(position))
            list_neighbor = []
            for specific_place_in_list in range(((position // 9) * 9), ((position // 9) * 9 + 9)):
                if (specific_place_in_list != position) & (sudoku_map[specific_place_in_list] != 'X'):
                    list_neighbor.append(sudoku_map[specific_place_in_list])
            print(list_neighbor)
            column_neighbor = []
            column_to_check = [num for num in range(81) if num % 9 == position % 9]
            for specific_place_in_column in column_to_check:
                if (specific_place_in_column != position) & (sudoku_map[specific_place_in_column] != 'X'):
                    column_neighbor.append(sudoku_map[specific_place_in_column])
            print(column_neighbor)
            square_neighbor = []
            for s in squares:
                if position in s:
                    square_to_check = s
            for specific_place_in_square in square_to_check:
                if (specific_place_in_square != position) & (sudoku_map[specific_place_in_square] != 'X'):
                    square_neighbor.append(sudoku_map[specific_place_in_square])
            print(square_neighbor)
            partial_list.append(list_neighbor)
            partial_list.append(column_neighbor)
            partial_list.append(square_neighbor)
            important_neighbours[position] = [partial_list]
        important_neighbours_number = {}
        for x in important_neighbours.keys():
            second_partial_list = []
            for y in important_neighbours[x]:
                for z in y:
                    for zz in z:
                        if zz not in second_partial_list:
                            second_partial_list.append(zz)
            important_neighbours_number[x] = second_partial_list
            print('Position {} : {} friends.'.format(x, len(second_partial_list)))
            print(second_partial_list)
        for xx in important_neighbours.keys():
            more_neighbors_amount = 0
            if sudoku_map[xx] == 'X':
                if len(important_neighbours_number[xx]) > more_neighbors_amount:
                    more_neighbors = xx
                    more_neighbors_amount = len(important_neighbours_number[xx])
        print('The position with more neighbors is {} with {} friends'.format(more_neighbors, len(important_neighbours_number[more_neighbors])))
        # THIS IS JUST TO KNOW IF IT GETS HERE...
        print("Got to the end...")

    def solve_first_try(self, sudoku_input):
        sudoku_map_in_progress = sudoku_input.sudoku_map_in_progress
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
        try:
            last_changed_position = sudoku_map_in_progress.index('X')
            for i in possible_guesses:
                sudoku_map_in_progress[last_changed_position] = i
                # sudoku_input.display()
                line_location = (last_changed_position // 9) * 9
                line_to_check = sudoku_map_in_progress[line_location:line_location + 9]
                column_location = last_changed_position % 9
                column_to_check = [sudoku_map_in_progress[num] for num in range(81) if num % 9 == column_location]
                for s in squares:
                    if last_changed_position in s:
                        square_to_check = [sudoku_map_in_progress[x] for x in s]
                if self.group_validate(self, line_to_check):
                    if self.group_validate(self, column_to_check):
                        if self.group_validate(self, square_to_check):
                            next_sudoku = Sudoku(sudoku_map_in_progress)
                            self.solve(self, next_sudoku)
                            break
        except ValueError:
            print()
            print(' Checking for errors... ')
            if self.check:
                print()
                print(' Sudoku solved.')
                print()
                sudoku_input.display()
                return sudoku_input
            else:
                print()
                print(' Something went wrong. ')
                print()

    def check(self, sudoku_map_solved):
        error_log = 0
        # Perform validation line by line:
        for i in range(9):
            line_to_check = sudoku_map_solved[(i * 9 + 0):(i * 9 + 9)]
            if self.group_validate(self, line_to_check):
                pass
                print('Line   {} : {} : Group is OK.'.format(i + 1, line_to_check))
            else:
                error_log += 1
                print('Line   {} : {} : NEEDS REVIEW.'.format(i + 1, line_to_check))
        # Perform validation column by column:
        for y in range(9):
            column_to_check = [sudoku_map_solved[num] for num in range(81) if num % 9 == y]
            if self.group_validate(self, column_to_check):
                pass
                print('Column {} : {} : Group is OK.'.format(y + 1, column_to_check))
            else:
                error_log += 1
                print('Column {} : {} : NEEDS REVIEW.'.format(y + 1, column_to_check))
        # Perform validation square by square:
        square_number = 0
        for z in range(0, 9, 3):
            for w in range(0, 9, 3):
                square_number += 1
                square_to_check = sudoku_map_solved[((z + 0) * 9 + w):((z + 0) * 9 + w + 3)] + sudoku_map_solved[((z + 1) * 9 + w):((z + 1) * 9 + w + 3)] + sudoku_map_solved[((z + 2) * 9 + w):((z + 2) * 9 + w + 3)]
                if self.group_validate(self, square_to_check):
                    pass
                    print('Square {} : {} : Group is OK.'.format(square_number, square_to_check))
                else:
                    error_log += 1
                    print('Square {} : {} : NEEDS REVIEW.'.format(square_number, square_to_check))
        if error_log > 0:
            return False
        else:
            return True

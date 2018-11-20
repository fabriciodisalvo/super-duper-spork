def group_validate(group_to_check):
    try:
        if sum(group_to_check) != 45:
            return False
    except TypeError:
        pass
    if 'X' in group_to_check:
        return False
    for i in group_to_check:
        if group_to_check.count(i) != 1:
            return False
    return True


def sudoku_check(sudoku_map_solved):
    error_log = 0
#       Perform validation line by line:
    for i in range(9):
        line_to_check = sudoku_map_solved[(i * 9 + 0):(i * 9 + 9)]
        if group_validate(line_to_check):
            pass
            #print('Line   {} : {} : Group is OK.'.format(i + 1, line_to_check))
        else:
            error_log += 1
            print('Line   {} : {} : NEEDS REVIEW.'.format(i + 1, line_to_check))
#       Perform validation column by column:
    for y in range(9):
        column_to_check = [sudoku_map_solved[num] for num in range(81) if num % 9 == y]
        if group_validate(column_to_check):
            pass
            #print('Column {} : {} : Group is OK.'.format(y + 1, column_to_check))
        else:
            error_log += 1
            print('Column {} : {} : NEEDS REVIEW.'.format(y + 1, column_to_check))
#       Perform validation square by square:
    square_number = 0
    for z in range(0, 9, 3):
        for w in range(0, 9, 3):
            square_number += 1
            square_to_check = sudoku_map_solved[((z + 0) * 9 + w):((z + 0) * 9 + w + 3)] + sudoku_map_solved[((z + 1) * 9 + w):((z + 1) * 9 + w + 3)] + sudoku_map_solved[((z + 2) * 9 + w):((z + 2) * 9 + w + 3)]
            if group_validate(square_to_check):
                pass
                #print('Square {} : {} : Group is OK.'.format(square_number, square_to_check))
            else:
                error_log += 1
                print('Square {} : {} : NEEDS REVIEW.'.format(square_number, square_to_check))
    if error_log > 0:
        return False
    else:
        return True


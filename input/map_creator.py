workfile = 'C:/Users/fdisarb/Documents/GitHub/sudoku_test_solver/0.txt'
file_opened = open(workfile, 'r')
output_dictionary = {}
index = 0

for line in file_opened:
    index += 1
    this_index = str(index)
    if len(this_index) == 1:
        this_index = '0000' + str(this_index)
    elif len(this_index) == 2:
        this_index = '000' + str(this_index)
    elif len(this_index) == 3:
        this_index = '00' + str(this_index)
    elif len(this_index) == 4:
        this_index = '0' + str(this_index)
    sudoku_map_to_import = [int(x) for x in line if x != '\n']
    output_dictionary['LVL0_' + this_index] = sudoku_map_to_import

print(output_dictionary)
file_opened.close()

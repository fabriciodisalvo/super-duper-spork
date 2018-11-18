
def sodoku_display(sudoku_map):
    print("|", end=" ")
    for i in range(3):
        print(sudoku_map[0 + i * 3], sudoku_map[1 + i * 3],
              sudoku_map[2 + i * 3], "|", end=" ")
    print()


def sudoku_check(sudoku_map):
    if len(sudoku_map) == 81:
        sodoku_display(sudoku_map)
    else:
        print(' len is not ok')


def main():
    sudoku_map = [1, 2, 3, 4, 5, 6, 7, 8, 9, 7, 8, 9, 1, 2, 3, 4, 5, 6, 4, 5, 6, 7, 8, 9, 1, 2, 3, 3, 1, 2, 8, 4, 5, 9, 6, 7, 6, 9,
                  7, 3, 1, 2, 8, 4, 5, 8, 4, 5, 6, 9, 7, 3, 1, 2, 2, 3, 1, 5, 7, 4, 6, 9, 8, 9, 6, 8, 2, 3, 1, 5, 7, 4, 5, 7, 4, 9, 6, 8, 2, 3, 1]
    sudoku_check(sudoku_map)


if __name__ == "__main__":
    main()

#!/usr/bin/env python3
import sys
import copy
import numpy as np
# TODO not a pretty solution; lots of code duplication; could definitely be
# improved; also, quite slow


def valid_limits(index, max_index):
    limits = [index - 1, index + 2]
    if limits[0] < 0:
        limits[0] = 0
    elif limits[1] > max_index:
        limits[1] = max_index
    return limits


def count_filled_seats(i, j, seating):
    count_filled_seats = 0
    max_row = len(seating)
    max_col = len(seating[0])
    row_limits = valid_limits(i, max_row)
    col_limits = valid_limits(j, max_col)

    for row_index in range(*row_limits):
        for col_index in range(*col_limits):
            if (row_index, col_index) == (i, j):
                continue
            elif seating[row_index][col_index] == '#':
                count_filled_seats += 1
    return count_filled_seats


def count_filled_seats_v2(i, j, seating):
    count_filled_seats = 0
    max_row = len(seating)
    max_col = len(seating[0])
    cases = [(i, range(j + 1, max_col)), 
             (range(i - 1, -1, -1), range(j + 1, max_col)),
             (range(i - 1, -1, -1), j),
             (range(i - 1, -1, -1), range(j - 1, -1, -1)),
             (i, range(j - 1, -1, -1)),
             (range(i + 1, max_row), range(j - 1, -1, -1)),
             (range(i + 1, max_row), j),
             (range(i + 1, max_row), range(j + 1, max_col))]

    for row, col in cases:
        if not isinstance(row, range) or not isinstance(col, range):
            seats = seating[row, col]
        else:
            row_slice, col_slice = ([], [])
            [(row_slice.append(x), col_slice.append(y)) for x, y in \
             zip(row, col)]
            seats = seating[row_slice, col_slice]
        for seat in seats:
            if seat == '#':
                count_filled_seats += 1
                break
            elif seat == 'L':
                break

    return count_filled_seats


def apply_rules(seating):
    new_seating = copy.deepcopy(seating)
    for i, row in enumerate(seating):
        for j, seat in enumerate(row):
            if seat == '.':
                continue
            else:
                adjacent_filled = count_filled_seats(i, j, seating)
                if adjacent_filled == 0 and seat == 'L':
                    new_seating[i][j] = '#'
                elif adjacent_filled >= 4 and seat == '#':
                    new_seating[i][j] = 'L'
    return new_seating


def apply_rules_v2(seating):
    new_seating = copy.deepcopy(seating)
    for i, row in enumerate(seating):
        for j, seat in enumerate(row):
            if seat == '.':
                continue
            else:
                adjacent_filled = count_filled_seats_v2(i, j, seating)
                if adjacent_filled == 0 and seat == 'L':
                    new_seating[i][j] = '#'
                elif adjacent_filled >= 5 and seat == '#':
                    new_seating[i][j] = 'L'
    return new_seating


def find_final_seating(seating):
    prev_seating = seating
    while True:
        new_seating = apply_rules(prev_seating)
        if np.array_equal(new_seating, prev_seating):
            break
        prev_seating = new_seating
    return new_seating


def find_final_seating_v2(seating):
    prev_seating = seating
    while True:
        new_seating = apply_rules_v2(prev_seating)
        if np.array_equal(new_seating, prev_seating):
            break
        prev_seating = new_seating
    return new_seating


def count_final_filled(initial_seating):
    count_final_filled = 0
    final_seating = find_final_seating(initial_seating)
    for row in final_seating:
        for seat in row:
            if seat == '#':
                count_final_filled += 1
    return count_final_filled


def count_final_filled_v2(initial_seating):
    final_seating = find_final_seating_v2(initial_seating)
    return np.sum(final_seating == '#')


def main(input_file='input.txt'):
    with open(input_file) as input:
        initial_seating = [line.strip() for line in input.readlines()]
        initial_seating = [[seat for seat in row] for row in  initial_seating]
        initial_seating = np.array(initial_seating)
    print('Final occupied seats (part 1): ',
          count_final_filled(initial_seating))
    print('Final occupied seats (part 2): ',
          count_final_filled_v2(initial_seating))

if __name__ == '__main__':
    if len(sys.argv) > 1:
        main(input_file=sys.argv[1])
    else:
        main()

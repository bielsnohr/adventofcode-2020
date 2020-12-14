import pytest
import numpy as np
from seating_system import apply_rules, count_filled_seats, find_final_seating
from seating_system import count_final_filled
#from seating_system import (apply_rules_v2, count_filled_seats_v2,
#                            find_final_seating_v2, count_final_filled_v2)
from seating_system import count_filled_seats_v2, count_final_filled_v2
from seating_system import find_final_seating_v2

blank = ['L.LL.LL.LL',
         'LLLLLLL.LL',
         'L.L.L..L..',
         'LLLL.LL.LL',
         'L.LL.LL.LL',
         'L.LLLLL.LL',
         '..L.L.....',
         'LLLLLLLLLL',
         'L.LLLLLL.L',
         'L.LLLLL.LL']
blank = [[char for char in row] for row in blank]
blank_v2 = np.array(blank)

iter1 = ['#.##.##.##',
         '#######.##',
         '#.#.#..#..',
         '####.##.##',
         '#.##.##.##',
         '#.#####.##',
         '..#.#.....',
         '##########',
         '#.######.#',
         '#.#####.##']
iter1 = [ [char for char in row] for row in iter1]

iter2 = ['#.LL.L#.##',
         '#LLLLLL.L#',
         'L.L.L..L..',
         '#LLL.LL.L#',
         '#.LL.LL.LL',
         '#.LLLL#.##',
         '..L.L.....',
         '#LLLLLLLL#',
         '#.LLLLLL.L',
         '#.#LLLL.##']
iter2 = [ [char for char in row] for row in iter2]

iter3 = ['#.##.L#.##',
         '#L###LL.L#',
         'L.#.#..#..',
         '#L##.##.L#',
         '#.##.LL.LL',
         '#.###L#.##',
         '..#.#.....',
         '#L######L#',
         '#.LL###L.L',
         '#.#L###.##']
iter3 = [ [char for char in row] for row in iter3]

final = ['#.#L.L#.##',
         '#LLL#LL.L#',
         'L.#.L..#..',
         '#L##.##.L#',
         '#.#L.LL.LL',
         '#.#L#L#.##',
         '..L.L.....',
         '#L#L##L#L#',
         '#.LLLLLL.L',
         '#.#L#L#.##']
final = [[char for char in row] for row in final]
last_row_index = len(final[0]) - 1
last_index = len(final) - 1

# Data for part 2
eight_occupied = ['.......#.',
                  '...#.....',
                  '.#.......',
                  '.........',
                  '..#L....#',
                  '....#....',
                  '.........',
                  '#........',
                  '...#.....']
eight_occupied = np.array([[char for char in row] for row in eight_occupied])

unocc_blocking = ['.............',
                  '.L.L.#.#.#.#.',
                  '.............']
unocc_blocking = np.array([[char for char in row] for row in unocc_blocking])

no_occupied = ['.##.##.',
               '#.#.#.#',
               '##...##',
               '...L...',
               '##...##',
               '#.#.#.#',
               '.##.##.']
no_occupied = np.array([ [char for char in row] for row in no_occupied])


@pytest.mark.parametrize("i, j, seating, adjacent_filled", [
    (0, 0, blank, 0), (0, 0, iter1, 2), (0, last_row_index, iter2, 2), 
    (last_index, 0, iter3, 1), (last_index, last_row_index, iter3, 1),
    (2, 3, iter3, 7)
])
def test_count_filled_seats(i, j, seating, adjacent_filled):
    assert count_filled_seats(i, j, seating) == adjacent_filled

@pytest.mark.parametrize("i, j, seating, adjacent_filled", [
    (4, 3, eight_occupied, 8), (1, 1, unocc_blocking, 0), 
    (3, 3, no_occupied, 0), (0, 0, no_occupied, 2) 
])
def test_count_filled_seats_v2(i, j, seating, adjacent_filled):
    assert count_filled_seats_v2(i, j, seating) == adjacent_filled


@pytest.mark.parametrize("seats_before, seats_after", [
    (blank, iter1), (iter1, iter2),
    (iter2, iter3)
])
def test_apply_rules(seats_before, seats_after):
    assert apply_rules(seats_before) == seats_after


def test_find_final_seating():
    assert find_final_seating(blank) == final


#def test_find_final_seating_v2():
#    assert find_final_seating_v2(blank) == final_v2


def test_count_final_filled():
    assert count_final_filled(blank) == 37


def test_count_final_filled_v2():
    assert count_final_filled_v2(blank_v2) == 26

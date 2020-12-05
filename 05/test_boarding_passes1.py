import pytest
from boarding_passes1 import (calculate_seat_id, calculate_row,
                              calculate_column, binary_search, find_open_seat)


@pytest.mark.parametrize("boarding_pass, expected_seat_id",
                          [('FBFBBFFRLR', 357), ('BFFFBBFRRR', 567),
                           ('FFFBBBFRRR', 119), ('BBFFBBFRLL', 820)])
def test_calculate_seat_id(boarding_pass, expected_seat_id):
    assert calculate_seat_id(boarding_pass) == expected_seat_id


@pytest.mark.parametrize("row_segment, expected_row",
                          [('FBFBBFF', 44), ('BFFFBBF', 70),
                           ('FFFBBBF', 14), ('BBFFBBF', 102)])
def test_calculate_row(row_segment, expected_row):
    assert calculate_row(row_segment) == expected_row


@pytest.mark.parametrize("column_segment, expected_column",
                          [('RLR', 5), ('RRR', 7),
                           ('RLL', 4)])
def test_calculate_column(column_segment, expected_column):
    assert calculate_column(column_segment) == expected_column

@pytest.mark.parametrize("instructions, range, expected",
                          [('0101100', [0, 127], 44), 
                           ('1000110', [0, 127], 70),
                           ('101', [0, 7], 5)])
def test_binary_search(instructions, range, expected):
    assert binary_search(instructions, range) == expected

def test_find_open_seat():
    seat_ids = [10, 4, 9, 5, 7, 6]
    assert find_open_seat(seat_ids) == 8

#!/usr/bin/env python3
import sys
import re

def binary_search(instructions, range):
    for i in instructions:
        change = (range[1] - range[0]) // 2 + 1
        if i == '0':
            range[1] -= change
        elif i == '1':
            range[0] += change

    if range[0] != range[1]:
        raise ValueError
    return range[0]


def calculate_row(row_segment):
    row_segment = row_segment.upper().replace('F', '0').replace('B', '1')
    return binary_search(row_segment, [0, 127])



def calculate_column(column_segment):
    column_segment = column_segment.upper().replace('L', '0').replace('R', '1')
    return binary_search(column_segment, [0, 7])


boarding_pass_format = re.compile(r'^([FB]{7})([LR]{3})$')


def calculate_seat_id(boarding_pass):
    boarding_pass_valid = boarding_pass_format.match(boarding_pass)
    if boarding_pass_valid:
        row_segment, column_segment = boarding_pass_valid.groups()
        seat_id = calculate_row(row_segment) * 8 + \
                calculate_column(column_segment)
    else:
        seat_id = None

    return seat_id

def find_open_seat(seat_ids):
    seat_ids = sorted(seat_ids)
    open_seat = None
    for i in range(1, len(seat_ids)):
        if seat_ids[i] - seat_ids[i - 1] == 2:
            open_seat = seat_ids[i] - 1

    return open_seat


def main(input_file='input1.txt'):
    seat_ids = []
    with open(input_file) as input:
        for boarding_pass in input:
            seat_ids.append(calculate_seat_id(boarding_pass))

    print("Maximum seat id: ", max(seat_ids))
    print("Open seat: ", find_open_seat(seat_ids))


if __name__ == '__main__':
    if len(sys.argv) > 1:
        main(input_file=sys.argv[1])
    else:
        main()

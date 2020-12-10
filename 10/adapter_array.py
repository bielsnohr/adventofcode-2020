#!/usr/bin/env python3
import sys
import numpy


def calculate_joltage_diffs(adapter_list):
    adapter_chain = numpy.array(sorted([0] + adapter_list))
    joltage_diffs = numpy.diff(adapter_chain)
    return (joltage_diffs == 1).sum() * ((joltage_diffs == 3).sum() + 1)


def main(input_file='input.txt'):
    with open(input_file) as input:
        adapter_list = [int(line.strip()) for line in input.readlines()]
    print('Joltage diffs multiplied (part 1): ',
          calculate_joltage_diffs(adapter_list))
    # print('Encryption weakness sum (part 2): ',
    #       find_contiguous_sum(invalid_number, number_list))


if __name__ == '__main__':
    if len(sys.argv) > 1:
        main(input_file=sys.argv[1])
    else:
        main()

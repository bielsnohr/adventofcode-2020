#!/usr/bin/env python3
import sys
import numpy


def index_chop(i):
    if i < 0:
        index_chop = 0
    else:
        index_chop = i
    return index_chop


def modified_fibonacci(index, store):
    if index in store:
        mult_factor = store[index]
    else:
        lower = index_chop(index - 3)
        mult_factor = sum([store[j] for j in range(lower, index)])
        # TODO modifying input is not good practice
        store[index] = mult_factor
    return mult_factor


# TODO not pretty, definitely could be improved
def calculate_adapter_arrangements(adapter_list):
    adapter_list.sort()
    final_adapter = [adapter_list[-1] + 3]
    adapter_chain = numpy.array([0] + adapter_list + final_adapter)
    joltage_diffs = numpy.diff(adapter_chain)
    mult_factors = []
    store = {0:1, 1:1, 2:2, 3:4}
    count_ones = 0
    was_one = False
    for diff in joltage_diffs:
        if diff == 1:
            count_ones += 1
            was_one = True
            mult_factor = modified_fibonacci(count_ones, store)
        else:
            if was_one:
                mult_factors.append(mult_factor)
                was_one = False
                count_ones = 0
    return numpy.prod(mult_factors)


def calculate_joltage_diffs(adapter_list):
    adapter_chain = numpy.array(sorted([0] + adapter_list))
    joltage_diffs = numpy.diff(adapter_chain)
    return (joltage_diffs == 1).sum() * ((joltage_diffs == 3).sum() + 1)


def main(input_file='input.txt'):
    with open(input_file) as input:
        adapter_list = [int(line.strip()) for line in input.readlines()]
    print('Joltage diffs multiplied (part 1): ',
          calculate_joltage_diffs(adapter_list))
    print('Adapter arrangements (part 2): ',
          calculate_adapter_arrangements(adapter_list))


if __name__ == '__main__':
    if len(sys.argv) > 1:
        main(input_file=sys.argv[1])
    else:
        main()

#!/usr/bin/env python3
import sys


def is_valid_sum(number, number_list):
    is_valid_sum = False
    for i, value1 in enumerate(number_list):
        for value2 in number_list[i+1:]:
            if value1 + value2 == number:
                is_valid_sum = True
                break
        if is_valid_sum:
            break
    return is_valid_sum


def find_invalid_number(number_list, len_preamble):
    for i in range(len_preamble, len(number_list)):
        number = number_list[i]
        preamble_start = i - len_preamble
        if not is_valid_sum(number, number_list[preamble_start:i]):
            break
    return number


def find_contiguous_sum(number, number_list):
    found_sum = False
    for i, element1 in enumerate(number_list):
        start = i + 1
        sum_list = [element1]
        for element2 in number_list[start:]:
            sum_list.append(element2)
            total = sum(sum_list)
            if total == number:
                found_sum = True
                break
            elif total > number:
                break
        if found_sum:
            break
    return min(sum_list) + max(sum_list)


def main(input_file='input.txt'):
    with open(input_file) as input:
        number_list = [int(line.strip()) for line in input.readlines()]
    invalid_number = find_invalid_number(number_list, 25)
    print('Invalid number (part 1): ', invalid_number)
    print('Encryption weakness sum (part 2): ',
          find_contiguous_sum(invalid_number, number_list))


if __name__ == '__main__':
    if len(sys.argv) > 1:
        main(input_file=sys.argv[1])
    else:
        main()

#!/usr/bin/env python3
import sys


def execute_boot_code(boot_code):
    index = 0
    visited = []
    accumulator = 0

    while True:
        command, arg = boot_code[index].split()
        visited.append(index)
        if command == 'nop':
            index += 1
        elif command == 'acc':
            accumulator += int(arg)
            index += 1
        elif command == 'jmp':
            index += int(arg)
        else:
            raise ValueError('Invalid command in boot code')

        if index in visited:
            break

    return accumulator


def fix_boot_code(boot_code):
    index = 0
    visited = []
    accumulator = 0

    while True:
        command, arg = boot_code[index].split()
        visited.append(index)
        if command == 'nop':
            index += 1
        elif command == 'acc':
            accumulator += int(arg)
            index += 1
        elif command == 'jmp':
            index += int(arg)
        else:
            raise ValueError('Invalid command in boot code')

        if index == len(boot_code):
            break
        elif index in visited:
            # TODO present
            pass

    return accumulator


def main(input_file='input.txt'):
    with open(input_file) as input:
        boot_code = [line.strip() for line in input.readlines()]
        print('Accumulator value (part 1): ', execute_boot_code(boot_code))


if __name__ == '__main__':
    if len(sys.argv) > 1:
        main(input_file=sys.argv[1])
    else:
        main()

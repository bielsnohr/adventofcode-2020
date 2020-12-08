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


def does_boot_code_complete(boot_code):
    index = 0
    visited = []
    accumulator = 0
    code_completes = False

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
        if index == len(boot_code):
            code_completes = True
            break

    return (code_completes, accumulator)


# TODO incorrect logic: fixing the last instruction that sends you to a
# previously visited instruction does not necessarily get you out of the
# infinite loop. The easy correct is to brute for every possible swap from
# 'jmp' <-> 'nop' (but only doing one at a time)
def fix_boot_code(boot_code):
    swap_comms = {'nop': 'jmp', 'jmp': 'nop'}

    for index, instruction in enumerate(boot_code):
        command, arg = instruction.split()
        if command in swap_comms.keys():
            command = swap_comms[command]
        boot_code[index] = ' '.join([command, arg])
        code_completes, accumulator = does_boot_code_complete(boot_code)
        if code_completes:
            break
        else:
            boot_code[index] = instruction

    return accumulator


def main(input_file='input.txt'):
    with open(input_file) as input:
        boot_code = [line.strip() for line in input.readlines()]
        print('Accumulator value (part 1): ', execute_boot_code(boot_code))
        print('Accumulator value (part 2): ', fix_boot_code(boot_code))


if __name__ == '__main__':
    if len(sys.argv) > 1:
        main(input_file=sys.argv[1])
    else:
        main()

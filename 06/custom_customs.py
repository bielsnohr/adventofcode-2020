#!/usr/bin/env python3
import sys
#import re

def count_yes_in_group(group_answers):
    yes_set = set()
    for answer in group_answers:
        yes_set = yes_set | set(answer)
    return len(yes_set)


def collect_total_yes_count(input_file):
    group_answers = []
    count_yes = 0
    with open(input_file) as input:
        while True:
            line = input.readline()
            if line == '' or line == '\n':
                count_yes += count_yes_in_group(group_answers)
                group_answers = []
                if line == '':
                    break
            else:
                group_answers.append(line.strip())

    return count_yes


def main(input_file='input.txt'):
    print(collect_total_yes_count(input_file))

if __name__ == '__main__':
    if len(sys.argv) > 1:
        main(input_file=sys.argv[1])
    else:
        main()

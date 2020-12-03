#!/usr/bin/env python3

import re

pwd_entry_parser = re.compile(r'^(\d+)-(\d+)\s+(\w):\s+(\w+)')
count_valid_pwds = 0

with open('input1.txt') as input:
    for line in input:
        index_1, index_2, letter, pwd = \
                pwd_entry_parser.match(line).groups()
        index_1, index_2 = (int(x) - 1 for x in (index_1, index_2))
        pwd_substring = pwd[index_1] + pwd[index_2]
        if pwd_substring.count(letter) == 1:
            print(True)
            count_valid_pwds += 1
        else:
            print(False)

print("Number of valid passwords: ", count_valid_pwds)

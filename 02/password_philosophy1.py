#!/usr/bin/env python3

import re

pwd_entry_parser = re.compile(r'^(\d+)-(\d+)\s+(\w):\s+(\w+)')
count_valid_pwds = 0

with open('input1.txt') as input:
    for line in input:
        lower, upper, letter, pwd = pwd_entry_parser.match(line).groups()
        if int(lower) <= pwd.count(letter) <= int(upper):
            count_valid_pwds += 1

print("Number of valid passwords: ", count_valid_pwds)

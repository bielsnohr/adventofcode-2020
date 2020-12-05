#!/usr/bin/env python3


def is_valid_passport(passport):
    required_fields = {'ecl', 'pid', 'eyr', 'hcl', 'byr', 'iyr', 'hgt'}
    optional_fields = {'cid'}
    all_fields = required_fields.union(optional_fields)
    fields = set(passport.keys())

#    if len(fields) > len(required_fields) + len(optional_fields):
#        return False
#    elif len(fields) < len(required_fields):
#        return False
    if fields == required_fields or fields == all_fields:
        return True
    else:
        return False


count_valid_passports = 0
with open('input1.txt') as input:

    current_passport = {}
    while True:
        line = input.readline()
        if line == '' or line == '\n':
            if is_valid_passport(current_passport):
                count_valid_passports += 1
            current_passport = {}
            if line == '':
                break
        else:
            entries = line.split()
            for entry in entries:
                key, value = entry.split(':')
                current_passport[key] = value

    print(count_valid_passports)

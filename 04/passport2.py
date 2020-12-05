#!/usr/bin/env python3

import re


# TODO the is_valie_****_year() functions are repetitive and could be combined
# probably
# TODO Add type hints and documentation
def is_valid_birth_year(year_str):
    try:
        birth_year = int(year_str)
    except ValueError:
        return False

    if 1920 <= birth_year <= 2002:
        return True
    else:
        return False


# TODO Add type hints and documentation
def is_valid_issue_year(year_str):
    try:
        issue_year = int(year_str)
    except ValueError:
        return False

    if 2010 <= issue_year <= 2020:
        return True
    else:
        return False


# TODO Add type hints and documentation
def is_valid_expiration_year(year_str):
    try:
        expiration_year = int(year_str)
    except ValueError:
        return False

    if 2020 <= expiration_year <= 2030:
        return True
    else:
        return False


height_format = re.compile(r'^(\d+)(cm|in)')


def is_valid_height(height_str):
    is_valid_height = False
    height_match = height_format.match(height_str)
    if height_match:
        height, unit = height_match.groups()
        try:
            height = int(height)
        except ValueError:
            pass
        else:
            if unit == 'cm':
                if 150 <= height <= 193:
                    is_valid_height = True
            elif unit == 'in':
                if 59 <= height <= 76:
                    is_valid_height = True

    return is_valid_height


hair_format = re.compile(r'^#[0-9a-f]{6}')


def is_valid_hair_color(hair_str):
    if hair_format.match(hair_str):
        return True
    else:
        return False


eye_colors = ['amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth']


def is_valid_eye_color(eye_str):
    if eye_str in eye_colors:
        return True
    else:
        return False


pid_format = re.compile(r'^[0-9]{9}$')


def is_valid_pid(pid_str):
    if pid_format.match(pid_str):
        return True
    else:
        return False


data_field_checks = {'ecl': is_valid_eye_color, 'pid': is_valid_pid,
                     'eyr': is_valid_expiration_year,
                     'hcl': is_valid_hair_color, 'byr': is_valid_birth_year,
                     'iyr': is_valid_issue_year, 'hgt': is_valid_height,
                     'cid': lambda x: True}


def is_valid_passport_data(passport):
    is_valid_passport_data = False

    for field, value in passport.items():
        if data_field_checks[field](value):
            is_valid_passport_data = True
        else:
            is_valid_passport_data = False
            break

    return is_valid_passport_data


def is_valid_passport(passport):
    required_fields = {'ecl', 'pid', 'eyr', 'hcl', 'byr', 'iyr', 'hgt'}
    optional_fields = {'cid'}
    all_fields = required_fields.union(optional_fields)
    fields = set(passport.keys())

    if fields == required_fields or fields == all_fields:
        return is_valid_passport_data(passport)
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

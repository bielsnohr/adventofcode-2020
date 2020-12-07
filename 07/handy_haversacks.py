#!/usr/bin/env python3
import sys
import re


def count_internal_bags(colour, rules):
    bag_count = 0
    if rules[colour] == {}:
        bag_count = 0
    else:
        for sub_colour, count in rules[colour].items():
            bag_count += count * (1 + count_internal_bags(sub_colour, rules))
    return bag_count


# TODO this could be optimised through some "dynamic" programming by storing
# the colours which we know have gold underneath them, such that when we search
# these colours sitting under other colours, we can immediately return true
def search_for_gold(colour, rules):
    contains_gold = False
    sub_colours = rules[colour].keys()
    if 'shiny gold' in sub_colours:
        contains_gold = True
    else:
        for sub_colour in sub_colours:
            contains_gold = search_for_gold(sub_colour, rules)
            if contains_gold:
                break
    return contains_gold


def count_valid_colours(rules):
    colour_count = 0
    for colour in rules:
        colour_count += search_for_gold(colour, rules) and 1 or 0
    return colour_count


bag_colours_numbers = re.compile(r'(\d*)\s*(\w+\s+\w+)\s+bag[s]?')


def collect_bag_rules(input_file):
    rules = {}
    with open(input_file) as input:
        for line in input:
            rule_contents = bag_colours_numbers.findall(line)
            if len(rule_contents) < 2:
                continue
            else:
                colour = rule_contents[0][1]
                rules[colour] = {col: int(num) for num, col in
                                 rule_contents[1:] if col != 'no other'}

    return rules


def main(input_file='input.txt'):
    rules = collect_bag_rules(input_file)
    print('Number of colours that contain shiny gold: ',
          count_valid_colours(rules))
    print('Number of bags within shiny gold: ',
          count_internal_bags('shiny gold', rules))


if __name__ == '__main__':
    if len(sys.argv) > 1:
        main(input_file=sys.argv[1])
    else:
        main()

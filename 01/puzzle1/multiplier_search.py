#!/usr/bin/env python3

with open('input') as input:
    input_list = [int(x) for x in input.readlines()]
    for i, first in enumerate(input_list):
        for second in input_list[(i + 1):]:
            if first + second == 2020:
                print(first * second)



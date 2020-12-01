#!/usr/bin/env python3

with open('input') as input:
    input_list = [int(x) for x in input.readlines()]
    for i, first in enumerate(input_list):
        for j, second in enumerate(input_list[(i + 1):]):
            for third in input_list[(i + j + 2):]:
                if first + second + third == 2020:
                    print(first, second, third)
                    print(first * second * third)


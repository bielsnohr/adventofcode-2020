import pytest
from handy_haversacks import (search_for_gold, count_valid_colours,
                              collect_bag_rules, count_internal_bags)


@pytest.fixture
def rules():
    return {'light red': {'bright white': 1, 'muted yellow': 2},
            'dark orange': {'bright white': 3, 'muted yellow': 4},
            'bright white': {'shiny gold': 1},
            'muted yellow': {'shiny gold': 2, 'faded blue': 9},
            'shiny gold':  {'dark olive': 1, 'vibrant plum': 2},
            'dark olive': {'faded blue': 3, 'dotted black': 4},
            'vibrant plum': {'faded blue': 5, 'dotted black': 6},
            'faded blue': {},
            'dotted black': {}}


@pytest.mark.parametrize("colour, contains_gold", [
    ('bright white', True), ('muted yellow', True),
    ('dark orange', True), ('light red', True),
    ('dark olive', False), ('vibrant plum', False),
    ('shiny gold', False), ('faded blue', False)
])
def test_search_for_gold(rules, colour, contains_gold):
    assert search_for_gold(colour, rules) == contains_gold


def test_count_valid_colours(rules):
    assert count_valid_colours(rules) == 4


def test_collect_bag_rules(rules):
    assert collect_bag_rules('test_input.txt') == rules


@pytest.mark.parametrize("input_file, bag_count", [
    ('test_input.txt', 32), ('test_input2.txt', 126)
])
def test_count_internal_bags(input_file, bag_count):
    rules = collect_bag_rules(input_file)
    assert count_internal_bags('shiny gold', rules) == bag_count

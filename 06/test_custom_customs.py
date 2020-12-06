import pytest
from custom_customs import count_yes_in_group, collect_total_yes_count
from custom_customs import count_intersect_yes_in_group 
from custom_customs import collect_intersect_yes_count


@pytest.mark.parametrize("group_answers, expected_yes_count",[
    (['abcx', 'abcy', 'abcz'], 6), (['ab', 'ac'], 3), 
    (['a', 'a', 'a', 'a'], 1)
])
def test_count_yes_in_group(group_answers, expected_yes_count):
    assert count_yes_in_group(group_answers) == expected_yes_count


@pytest.mark.parametrize("group_answers, expected_yes_count",[
    (['abcx', 'abcy', 'abcz'], 3), (['ab', 'ac'], 1), 
    (['a', 'a', 'a', 'a'], 1)
])
def test_count_intersect_yes_in_group(group_answers, expected_yes_count):
    assert count_intersect_yes_in_group(group_answers) == expected_yes_count


def test_collect_total_yes_count():
    assert collect_total_yes_count(input_file='test_input.txt') == 11


def test_collect_intersect_yes_count():
    assert collect_intersect_yes_count(input_file='test_input.txt') == 6

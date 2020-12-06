import pytest
from custom_customs import count_yes_in_group, collect_total_yes_count


@pytest.mark.parametrize("group_answers, expected_yes_count",[
    (['abcx', 'abcy', 'abcz'], 6), (['ab', 'ac'], 3), 
    (['a', 'a', 'a', 'a'], 1)
])
def test_count_yes_in_group(group_answers, expected_yes_count):
    assert count_yes_in_group(group_answers) == expected_yes_count


def test_collect_total_yes_count():
    assert collect_total_yes_count(input_file='test_input.txt') == 11

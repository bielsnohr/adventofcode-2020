import pytest
from encoding_error import (is_valid_sum, find_invalid_number,
                            find_contiguous_sum)


test_number_list = [x for x in range(1, 26)]


@pytest.fixture
def test2_number_list():
    return [35, 20, 15, 25, 47, 40, 62, 55, 65, 95, 102, 117, 150, 182, 127,
            219, 299, 277, 309, 576]


@pytest.mark.parametrize("number, number_list, is_valid", [
    (26, test_number_list, True), (49, test_number_list, True),
    (100, test_number_list, False), (50, test_number_list, False)
])
def test_is_valid_sum(number, number_list, is_valid):
    assert is_valid_sum(number, number_list) == is_valid


def test_find_invalid_number(test2_number_list):
    assert find_invalid_number(test2_number_list, 5) == 127


def test_find_contiguous_sum(test2_number_list):
    assert find_contiguous_sum(127, test2_number_list) == 62

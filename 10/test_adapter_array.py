import pytest
from adapter_array import calculate_joltage_diffs, calculate_adapter_arrangements
from adapter_array import modified_fibonacci


adapter_input1 = [16, 10, 15, 5, 1, 11, 7, 19, 6, 12, 4]

adapter_input2 = [28, 33, 18, 42, 31, 14, 46, 20, 48, 47, 24, 23, 49, 45, 19,
                  38, 39, 11, 1, 32, 25, 35, 8, 17, 7, 9, 4, 2, 34, 10, 3]


@pytest.mark.parametrize("adapter_input, multiplied_result", [
    (adapter_input1, 35), (adapter_input2, 220)
])
def test_calculate_joltage_diffs(adapter_input, multiplied_result):
    assert calculate_joltage_diffs(adapter_input) == multiplied_result


@pytest.mark.parametrize("adapter_input, arrangements", [
    (adapter_input1, 8), (adapter_input2, 19208)
])
def test_calculate_adapter_arrangements(adapter_input, arrangements):
    assert calculate_adapter_arrangements(adapter_input) == arrangements

def test_modified_fibonacci():
    store = {0:1, 1:1, 2:2, 3:4}

    assert modified_fibonacci(4, store) == 7
    assert modified_fibonacci(5, store) == 13

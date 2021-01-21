import pytest
from shuttle_search import (multiply_bus_id_and_wait_time, parse_bus_times,
                            check_valid_timestamp, find_earliest_timestamp,
                            get_bus_times_and_offsets)


earliest_departure = 939
bus_ids = [7, 13, 59, 31, 19]


def test_multiply_bus_id_and_wait_time():
    assert multiply_bus_id_and_wait_time(earliest_departure, bus_ids) == 295


def test_parse_bus_times():
    bus_listing = '7,13,x,x,59,x,31,19'
    assert parse_bus_times(bus_listing) == bus_ids


@pytest.mark.parametrize("timestamp, bus_listing", [
    (3417, '17,x,13,19'), (754018, '67,7,59,61'), (779210, '67,x,7,59,61'),
    (1261476, '67,7,x,59,61'), (1202161486, '1789,37,47,1889')
])
def test_check_valid_timestamp(timestamp, bus_listing):
    assert check_valid_timestamp(timestamp, bus_listing)


@pytest.mark.parametrize("timestamp, bus_listing", [
    (417, '17,x,13,19'), (54018, '67,7,59,61'), (79210, '67,x,7,59,61'),
    (1261473, '67,7,x,59,61'), (122161486, '1789,37,47,1889')
])
def test_check_invalid_timestamp(timestamp, bus_listing):
    assert check_valid_timestamp(timestamp, bus_listing) is False


def test_get_bus_times_and_offsets():
    bus_listing = '17,x,13,19'
    output = [(16, 19), (0, 17), (11, 13)]
    assert get_bus_times_and_offsets(bus_listing) == output


@pytest.mark.parametrize("timestamp, bus_listing", [
    (3417, '17,x,13,19'), (754018, '67,7,59,61'), (779210, '67,x,7,59,61'),
    (1261476, '67,7,x,59,61'), (1202161486, '1789,37,47,1889')
])
def test_find_earliest_timestamp(timestamp, bus_listing):
    assert find_earliest_timestamp(bus_listing) == timestamp

import pytest
from shuttle_search import (multiply_bus_id_and_wait_time, parse_bus_times,
                            check_valid_timestamp)


earliest_departure = 939
bus_ids = [7, 13, 59, 31, 19]


def test_multiply_bus_id_and_wait_time():
    assert multiply_bus_id_and_wait_time(earliest_departure, bus_ids) == 295


def test_parse_bus_times():
    bus_listing = '7,13,x,x,59,x,31,19'
    assert parse_bus_times(bus_listing) == bus_ids


@pytest.parametrize("timestamp, bus_ids", [])
def test_check_valid_timestamp():
    pass

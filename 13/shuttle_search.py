#!/usr/bin/env python3
import sys


def check_valid_timestamp(timestamp, bus_listing):
    bus_listing = bus_listing.split(',')
    for bus_id in bus_listing:
        if bus_id == 'x':
            timestamp += 1
            continue
        elif timestamp % int(bus_id) == 0:
            timestamp += 1
            continue
        else:
            return False

    return True


def find_earliest_timestamp(bus_listing, start_point=0):
    first_id = parse_bus_times(bus_listing)[0]
    count = start_point // first_id
    while True:
        timestamp = count * first_id
        print(timestamp)
        if check_valid_timestamp(timestamp, bus_listing):
            return timestamp
        else:
            count += 1



def multiply_bus_id_and_wait_time(earliest_departure, bus_ids):
    earliest_bus = min(bus_ids)
    min_wait = earliest_bus
    for id in bus_ids:
        wait = id - earliest_departure % id
        if wait < min_wait:
            min_wait = wait
            earliest_bus = id
    return earliest_bus * min_wait


def parse_bus_times(bus_listing):
    return [int(id) for id in bus_listing.split(',') if is_int(id)]


def is_int(s):
    try:
        int(s)
        return True
    except ValueError:
        return False


def main(input_file='input.txt'):
    with open(input_file) as input:
        earliest_departure = int(input.readline().strip())
        bus_ids = input.readline().strip()
    print('Earliest departure multiplier (part 1): ',
          multiply_bus_id_and_wait_time(earliest_departure,
                                        parse_bus_times(bus_ids)))
    print('Earliest valid timestamp (part 2): ',
          find_earliest_timestamp(bus_ids, start_point=100000000000000))


if __name__ == '__main__':
    if len(sys.argv) > 1:
        main(input_file=sys.argv[1])
    else:
        main()

import pytest
from rain_risk import FerryNavigation, WaypointNavigation


@pytest.fixture
def ferry():
    return FerryNavigation()


@pytest.fixture
def waypoint():
    return WaypointNavigation()


@pytest.fixture
def instructions():
    return ['F10', 'N3', 'F7', 'R90', 'F11']


# Part 1: Test the naive form of navigation

def test_ferry_init(ferry):
    assert (ferry.direction, ferry.x, ferry.y, ferry.position()) == \
            (0, 0, 0, [0, 0])


@pytest.mark.parametrize("direction, value, position_after", [
    ('N', 3, [0, 3]), ('W', 4, [-4, 0])
])
def test_compass_movement(direction, value, position_after, ferry):
    assert ferry.compass_movement(direction, value) == position_after
    assert ferry.direction == 0


@pytest.mark.parametrize("turn, angle, direction_after", [
    ('R', 90, 270), ('L', 270, 270)
])
def test_change_direction(turn, angle, direction_after, ferry):
    assert ferry.change_direction(turn, angle) == direction_after
    assert ferry.position() == [0, 0]


@pytest.mark.parametrize("initial_direction, value, position_after", [
    (0, 10, [10, 0]), (90, 10, [0, 10]), (180, 10, [-10, 0]), 
    (270, 10, [0, -10])
])
def test_forward_movement(initial_direction, value, position_after, ferry):
    ferry.direction = initial_direction
    assert ferry.forward_movement(value) == position_after


def test_execute_instructions(instructions, ferry):
    assert ferry.execute_instructions(instructions) == [17, -8]


def test_manhattan_distance(instructions, ferry):
    ferry.execute_instructions(instructions)
    assert ferry.manhattan_distance() == 25


# Part 2: Test the waypoint form of navigation

def test_waypoint_init(waypoint):
    test_ferry_init(waypoint)
    assert (waypoint.waypt_x, waypoint.waypt_y, waypoint.waypoint_position()) \
            == (10, 1, [10, 1])


@pytest.mark.parametrize("direction, value, position_after", [
    ('N', 3, [10, 4]), ('W', 4, [6, 1])
])
def test_move_waypoint(direction, value, position_after, waypoint):
    assert waypoint.move_waypoint(direction, value) == position_after


@pytest.mark.parametrize("hand, angle, position_after", [
    ('R', 90, [1, -10]), ('L', 270, [1, -10])
])
def test_rotate_waypoint(hand, angle, position_after, waypoint):
    assert waypoint.rotate_waypoint(hand, angle) == position_after
    assert waypoint.position() == [0, 0]


@pytest.mark.parametrize("waypt_x, waypt_y, value, position_after", [
    (10, 1, 10, [100, 10]), (-4, -4, 5, [-20, -20])
])
def test_waypt_forward_movement(waypt_x, waypt_y, value, position_after,
                                waypoint):
    waypoint.waypt_x = waypt_x
    waypoint.waypt_y = waypt_y
    assert waypoint.forward_movement(value) == position_after


def test_waypoint_execute_instructions(instructions, waypoint):
    assert waypoint.execute_instructions(instructions) == [214, -72]


def test_waypoint_manhattan_distance(instructions, waypoint):
    waypoint.execute_instructions(instructions)
    assert waypoint.manhattan_distance() == 286

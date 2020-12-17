#!/usr/bin/env python3
import sys
from math import radians, sin, cos


class FerryNavigation():


    def __init__(self):
        # TODO these could do with setter and getter decorated methods
        self.direction = 0
        self.x = 0
        self.y = 0
        
    
    def position(self):
        return [self.x, self.y]

    
    def parse_instruction(self, instruction):
        return (instruction[0], int(instruction[1:]))


    def compass_movement(self, direction, value):
        if direction == 'N':
            self.y += value
        elif direction == 'E':
            self.x += value
        elif direction == 'S':
            self.y -= value
        elif direction == 'W':
            self.x -= value
        return self.position()

    
    def change_direction(self, hand, angle):
        if hand == 'R':
            new_direction = self.direction - angle
        elif hand == 'L':
            new_direction = self.direction + angle
        self.direction = new_direction % 360
        return self.direction


    def forward_movement(self, value):
        self.x += value * int(cos(radians(self.direction)))
        self.y += value * int(sin(radians(self.direction)))
        return self.position()


    def execute_instructions(self, instructions):
        for instruction in instructions:
            code, value = self.parse_instruction(instruction)
            if code in ('N', 'E', 'S', 'W'):
                self.compass_movement(code, value)
            elif code in ('L', 'R'):
                self.change_direction(code, value)
            elif code == 'F':
                self.forward_movement(value)
        return self.position()


    def manhattan_distance(self):
        return abs(self.x) + abs(self.y)


class WaypointNavigation(FerryNavigation):


    def __init__(self):
        super().__init__()
        self.waypt_x = 10
        self.waypt_y = 1


    def waypoint_position(self):
        return [self.waypt_x, self.waypt_y]


    def move_waypoint(self, direction, value):
        if direction == 'N':
            self.waypt_y += value
        elif direction == 'E':
            self.waypt_x += value
        elif direction == 'S':
            self.waypt_y -= value
        elif direction == 'W':
            self.waypt_x -= value
        return self.waypoint_position()

    
    def rotate_waypoint(self, hand, angle):
        if hand == 'R':
            angle = -angle
        angle = radians(angle)
        # rotation matrix transformation
        new_x = self.waypt_x * int(cos(angle)) - self.waypt_y * int(sin(angle))
        new_y = self.waypt_x * int(sin(angle)) + self.waypt_y * int(cos(angle))
        self.waypt_x = new_x
        self.waypt_y = new_y
        return self.waypoint_position()


    def forward_movement(self, value):
        self.x += value * self.waypt_x
        self.y += value * self.waypt_y
        return self.position()


    def execute_instructions(self, instructions):
        for instruction in instructions:
            code, value = self.parse_instruction(instruction)
            if code in ('N', 'E', 'S', 'W'):
                self.move_waypoint(code, value)
            elif code in ('L', 'R'):
                self.rotate_waypoint(code, value)
            elif code == 'F':
                self.forward_movement(value)
        return self.position()


def main(input_file='input.txt'):
    with open(input_file) as input:
        instructions = [line.strip() for line in input.readlines()]
    ferry = FerryNavigation()
    ferry.execute_instructions(instructions)
    waypoint = WaypointNavigation()
    waypoint.execute_instructions(instructions)
    print('Manhattan distance (part 1): ', ferry.manhattan_distance())
    print('Manhattan distance (part 2): ', waypoint.manhattan_distance())

if __name__ == '__main__':
    if len(sys.argv) > 1:
        main(input_file=sys.argv[1])
    else:
        main()

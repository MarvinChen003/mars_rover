from scripts.planet import Planet


def plus_one(num):
    num += 1
    return num


def minus_one(num):
    num -= 1
    return num


COMMAND_MATRIX = {
    "Nf": ["x", plus_one],
    "Nb": ["x", minus_one],
    "Nl": ["y", minus_one],
    "Nr": ["y", plus_one],
    "Ef": ["y", plus_one],
    "Eb": ["y", minus_one],
    "El": ["x", plus_one],
    "Er": ["x", minus_one],
    "Sf": ["x", minus_one],
    "Sb": ["x", plus_one],
    "Sl": ["y", plus_one],
    "Sr": ["y", minus_one],
    "Wf": ["y", minus_one],
    "Wb": ["y", plus_one],
    "Wl": ["x", minus_one],
    "Wr": ["x", plus_one]
}


class Rover:

    # lateral axis x, direct-axis y
    def __init__(self, init_x, init_y, orientation):
        self.x = init_x
        self.y = init_y
        self.orientation = orientation

    def init_position(self):
        return [self.x, self.y, self.orientation]

    def edge_check(self):
        mars = Planet(10, 10)
        if self.x == mars.edge_x or self.y == mars.edge_y or self.x == 0 or self.y == 0:
            return True

    def move(self, edge_check, commands):

        for command in commands:
            reach_edge = edge_check()
            if reach_edge:
                return f'Reach the edge in x ray, current position [{self.x}, {self.y}, {self.orientation}]'

            if command in ['N', 'S', 'W', 'E']:
                self.orientation = command
            else:
                action_command = self.orientation + command
                axis = COMMAND_MATRIX[action_command][0]
                move = COMMAND_MATRIX[action_command][1]
                # reflection
                position = getattr(self, axis)
                setattr(self, axis, move(position))

        return [self.x, self.y, self.orientation]



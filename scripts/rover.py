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

    @staticmethod
    def turn_around(command):
        if command in ['N', 'S', 'W', 'E']:
            return True

    def reach_edge(self):
        mars = Planet(10, 10)
        if self.x == mars.edge_x or self.y == mars.edge_y or self.x == 0 or self.y == 0:
            return True

    def move(self, command):
        command_matrix_key = self.orientation + command
        axis = COMMAND_MATRIX[command_matrix_key][0]
        move = COMMAND_MATRIX[command_matrix_key][1]
        # reflection
        setattr(self, axis, move(getattr(self, axis)))

    def execute_command(self, commands):

        for command in commands:

            if self.reach_edge():
                return f'Reach the edge, stop. Current position [{self.x}, {self.y}, {self.orientation}]'

            if self.turn_around(command):
                self.orientation = command
            else:
                self.move(command)

        return [self.x, self.y, self.orientation]

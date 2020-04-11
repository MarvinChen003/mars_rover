class Rover:

    def __init__(self, init_x, init_y, orientation):
        self.x = init_x
        self.y = init_x
        self.orientation = orientation

    def init_position(self):
        return [self.x, self.y, self.orientation]

    def move(self, command):
        if command == 'f':
            rover_x = self.x + 1
            rover_y = self.y
            rover_orientation = self.orientation

            return [rover_x, rover_y, rover_orientation]

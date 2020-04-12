from scripts.planet import Planet


class Rover:

    def __init__(self, init_x, init_y, orientation):
        self.x = init_x
        self.y = init_y
        self.orientation = orientation

    def init_position(self):
        return [self.x, self.y, self.orientation]

    def move(self, commands):

        mars = Planet(10, 10)

        for command in commands:

            if self.x == mars.edge_x or self.y == mars.edge_y or self.x == 0 or self.y == 0 :
                return f'Reach the edge in x ray, current position [{self.x}, {self.y}, {self.orientation}]'

            if command in ['N', 'S', 'W', 'E']:
                self.orientation = command

            if command == 'f' and self.orientation == 'N':
                self.x = self.x + 1
            elif command == 'b' and self.orientation == 'N':
                self.x = self.x - 1
            elif command == 'l' and self.orientation == 'N':
                self.y = self.y - 1
            elif command == 'r' and self.orientation == 'N':
                self.y = self.y + 1

            if command == 'f' and self.orientation == 'E':
                self.y = self.y + 1
            elif command == 'b' and self.orientation == 'E':
                self.y = self.y - 1
            elif command == 'l' and self.orientation == 'E':
                self.x = self.x + 1
            elif command == 'r' and self.orientation == 'E':
                self.x = self.x - 1

            if command == 'f' and self.orientation == 'S':
                self.x = self.x - 1
            elif command == 'b' and self.orientation == 'S':
                self.x = self.x + 1
            elif command == 'l' and self.orientation == 'S':
                self.y = self.y + 1
            elif command == 'r' and self.orientation == 'S':
                self.y = self.y - 1

            if command == 'f' and self.orientation == 'W':
                self.y = self.y - 1
            elif command == 'b' and self.orientation == 'W':
                self.y = self.y + 1
            elif command == 'l' and self.orientation == 'W':
                self.x = self.x - 1
            elif command == 'r' and self.orientation == 'W':
                self.x = self.x + 1

        return [self.x, self.y, self.orientation]

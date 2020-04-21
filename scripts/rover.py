from scripts.planet import Planet


class Rover:

    global commands
    global actual_moves

    def __init__(self, init_x, init_y, orientation):
        self.x = init_x
        self.y = init_y
        self.orientation = orientation

    def init_position(self):
        return [self.x, self.y, self.orientation]

    def reach_edge(self):
        mars = Planet(10, 10)
        if self.x == mars.edge_x or self.y == mars.edge_y or self.x == 0 or self.y == 0:
            raise ValueError("Reach the edge, stop. Current position {:d},{:d},{:s}"
                             .format(self.x, self.y, self.orientation))

    # Use Command Pattern to reduce if/switch statement
    # Receiver
    def move(self, commands):
        for command in commands:
            self.command_handler(command)

        return [self.x, self.y, self.orientation]

    # Invoker
    def command_handler(self,  command_key):
        command = commands[command_key]
        actual_move = actual_moves[self.orientation]
        command(self, actual_move)

    # Command
    def move_forward(self, actual_move):
        self.reach_edge()
        self.x = self.x + actual_move[0]
        self.y = self.y + actual_move[1]

    def move_backward(self, actual_move):
        self.reach_edge()
        self.x = self.x - actual_move[0]
        self.y = self.y - actual_move[1]

    def turn_right(self, actual_move):
        self.orientation = actual_move[3]

    def turn_left(self, actual_move):
        self.orientation = actual_move[2]

    commands = {
        'f': move_forward,
        'b': move_backward,
        'r': turn_right,
        'l': turn_left
    }

    actual_moves = {
        'N': [+0, +1, 'W', 'E'],
        'S': [+0, -1, 'E', 'W'],
        'E': [+1, +0, 'N', 'S'],
        'W': [-1, +0, 'S', 'N']
    }




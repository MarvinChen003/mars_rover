from scripts.rover import Rover


def test_rover_init_position():
    rover = Rover(2, 2, 'N')
    assert rover.init_position() == [2, 2, 'N']


def test_move_forward():
    rover = Rover(2, 2, 'N')
    assert rover.move('f') == [3, 2, 'N']
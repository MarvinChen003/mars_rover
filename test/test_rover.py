from scripts.rover import Rover


def test_rover_init_position():
    rover = Rover(2, 2, 'N')
    assert rover.init_position() == [2, 2, 'N']


def test_move_forward_one_step():
    rover = Rover(2, 2, 'N')
    assert rover.move(rover.edge_check, 'f') == [3, 2, 'N']


def test_move_forward_multi_steps():
    rover = Rover(2, 2, 'N')
    assert rover.move(rover.edge_check, 'fff') == [5, 2, 'N']


def test_reach_x_edge_warning():
    rover = Rover(2, 2, 'N')
    assert rover.move(rover.edge_check, 'ffffffffffffff') == "Reach the edge in x ray, current position [10, 2, N]"


def test_reach_y_edge_warning():
    rover = Rover(2, 2, 'N')
    assert rover.move(rover.edge_check, 'rrrrrrrrrrrrrr') == "Reach the edge in x ray, current position [2, 10, N]"


def test_chaos_movement():
    rover = Rover(2, 2, 'N')
    assert rover.move(rover.edge_check, 'frfflbbEfrrrbbbSffffllNrfffWrrffff') == "Reach the edge in x ray, current position [0, 3, E]"


def test_rover_turn_north():
    rover = Rover(2, 2, 'N')
    assert rover.move(rover.edge_check, 'fEff') == [3, 4, 'E']



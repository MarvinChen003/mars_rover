from scripts.rover import Rover


def test_rover_init_position():
    rover = Rover(2, 2, 'N')
    assert rover.init_position() == [2, 2, 'N']


def test_move_forward_one_step():
    rover = Rover(2, 2, 'N')
    assert rover.execute_command('f') == [3, 2, 'N']


def test_move_forward_multi_steps():
    rover = Rover(2, 2, 'N')
    assert rover.execute_command('fff') == [5, 2, 'N']


def test_reach_x_edge_warning():
    rover = Rover(2, 2, 'N')
    assert rover.execute_command('ffffffffffffff') == "Reach the edge, stop. Current position [10, 2, N]"


def test_reach_y_edge_warning():
    rover = Rover(2, 2, 'N')
    assert rover.execute_command('rrrrrrrrrrrrrr') == "Reach the edge, stop. Current position [2, 10, N]"


def test_chaos_movement():
    rover = Rover(2, 2, 'N')
    assert rover.execute_command('frfflbbEfrrrbbbSffffllNrfffWrrffff') == "Reach the edge, stop. Current position [0, 3, E]"


def test_rover_change_direction():
    rover = Rover(2, 2, 'N')
    assert rover.execute_command('fEff') == [3, 4, 'E']



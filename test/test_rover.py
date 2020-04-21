import pytest
from scripts.rover import Rover


def test_rover_init_position():
    rover = Rover(2, 2, 'N')
    assert rover.init_position() == [2, 2, 'N']


def test_move_forward_one_step():
    rover = Rover(2, 2, 'N')
    assert rover.move('f') == [2, 3, 'N']


def test_move_forward_multi_steps():
    rover = Rover(2, 2, 'N')
    assert rover.move('fff') == [2, 5, 'N']


def test_reach_y_edge_warning():
    rover = Rover(2, 2, 'N')
    with pytest.raises(Exception) as e:
        rover.move('ffffffffffffff')
    assert str(e.value) == "Reach the edge, stop. Current position 2,10,N"


def test_reach_x_edge_warning():
    rover = Rover(2, 2, 'N')
    with pytest.raises(Exception) as e:
        rover.move('rfffffffffffffff')
    assert str(e.value) == "Reach the edge, stop. Current position 10,2,E"


def test_chaos_movement():
    rover = Rover(2, 2, 'N')
    with pytest.raises(Exception) as e:
        rover.move('frfflbbfrrrbbbffffllrfffrrffff')
    assert str(e.value) == "Reach the edge, stop. Current position 3,0,S"


def test_rover_change_direction():
    rover = Rover(2, 2, 'N')
    assert rover.move('frff') == [4, 3, 'E']



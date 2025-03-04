import pytest
from mars_rover import MarsRover
import mars_rover


class TestMarsRover:
    def test_initializes_rover_with_a_given_position(self):
        mars_rover = MarsRover(0, 0, "N")

        assert mars_rover.x == 0
        assert mars_rover.y == 0
        assert mars_rover.orientation == "N"

    def test_pass_commands_to_rover(self):
        commands = ["F", "F", "B"]

        mars_rover = MarsRover(0, 0, "N")

        mars_rover.command(commands)

        assert mars_rover.x == 0
        assert mars_rover.y == 1
        assert mars_rover.orientation == "N"

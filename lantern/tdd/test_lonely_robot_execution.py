import pytest
from lonely_robot import Robot, Asteroid, MissAsteroidError, EndAsteroidError, ObstaclesOnAsteroidError


class TestRobotCreation:
    def test_parameters(self):
        x, y = 10, 15
        width = 40
        height = 40
        asteroid = Asteroid(width, height)
        direction = "W"
        robot = Robot(x, y, asteroid, direction)
        assert robot.x == 10
        assert robot.y == 15
        assert robot.asteroid == asteroid
        assert robot.direction == direction

    @pytest.mark.parametrize(
        "asteroid_size,robot_coordinates",
        (
                ((15, 25), (26, 30)),
                ((15, 25), (26, 24)),
                ((15, 25), (15, 27)),
        )
    )
    def test_check_if_robot_on_asteroid(self, asteroid_size, robot_coordinates):
        with pytest.raises(MissAsteroidError):
            asteroid = Asteroid(*asteroid_size)
            Robot(*robot_coordinates, asteroid, "W")


class TestRobotMove:

    def setup(self):
        self.x, self.y = 10, 15
        self.asteroid = Asteroid(40, 40)

    @pytest.mark.parametrize("current_direction,expected_direction", [
        ("N", "W"),
        ("W", "S"),
        ("S", "E"),
        ("E", "N"),
    ])
    def test_left(self, current_direction, expected_direction):

        robot = Robot(self.x, self.y, self.asteroid, current_direction)
        robot.turn_left()
        assert robot.direction == expected_direction

    @pytest.mark.parametrize("current_direction,expected_direction", [
        ("N", "E"),
        ("E", "S"),
        ("S", "W"),
        ("W", "N"),
    ])
    def test_right(self, current_direction, expected_direction):
        robot = Robot(self.x, self.y, self.asteroid, current_direction)
        robot.turn_right()
        assert robot.direction == expected_direction

    @pytest.mark.parametrize("direction,stop_point", [
        ("N", (10, 16)),
        ("E", (11, 15)),
        ("S", (10, 14)),
        ("W", (9, 15)),
    ])
    def test_move_forward(self, direction, stop_point):
        robot = Robot(self.x, self.y, self.asteroid, direction)
        robot.move_forward()
        assert robot.x == stop_point[0]
        assert robot.y == stop_point[1]

    @pytest.mark.parametrize("direction,stop_point", [
        ("N", (10, 14)),
        ("E", (9, 15)),
        ("S", (10, 16)),
        ("W", (11, 15)),
    ])
    def test_move_backward(self, direction, stop_point):
        robot = Robot(self.x, self.y, self.asteroid, direction)
        robot.move_backward()
        assert robot.x == stop_point[0]
        assert robot.y == stop_point[1]

    @pytest.mark.parametrize("direction,robot_coordinates", [
        ("N", (10, 40)),
        ("E", (40, 10)),
        ("S", (10, 0)),
        ("W", (0, 10)),
    ])
    def test_check_if_robot_can_move_forward(self, direction, robot_coordinates):
        with pytest.raises(EndAsteroidError):
            robot = Robot(*robot_coordinates, self.asteroid, direction)
            robot.move_forward()

    @pytest.mark.parametrize("direction,robot_coordinates", [
        ("N", (0, 0)),
        ("E", (0, 0)),
        ("S", (40, 40)),
        ("W", (40, 40)),
    ])
    def test_check_if_robot_can_move_backward(self, direction, robot_coordinates):
        with pytest.raises(EndAsteroidError):
            robot = Robot(*robot_coordinates, self.asteroid, direction)
            robot.move_backward()

    @pytest.mark.parametrize("direction,robot_coordinates", [
        ("N", (30, 29)),
        ("E", (29, 30)),
        ("S", (30, 31)),
        ("W", (31, 30)),
    ])
    def test_check_for_obstacles_when_move_forward(self, direction, robot_coordinates):
        with pytest.raises(ObstaclesOnAsteroidError):
            robot = Robot(*robot_coordinates, self.asteroid, direction)
            robot.move_forward()

    @pytest.mark.parametrize("direction,robot_coordinates", [
        ("N", (30, 31)),
        ("E", (31, 30)),
        ("S", (30, 29)),
        ("W", (29, 30)),
    ])
    def test_check_for_obstacles_when_move_backward(self, direction, robot_coordinates):
        with pytest.raises(ObstaclesOnAsteroidError):
            robot = Robot(*robot_coordinates, self.asteroid, direction)
            robot.move_backward()

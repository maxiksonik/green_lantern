class Asteroid:
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.obstacles = ((self.width - 10, self.height - 10),
                          (self.width - 10, 10),
                          (10, 10),
                          (10, self.height - 10),
                          )


class Robot:
    def __init__(self, x, y, asteroid, direction):
        self.x = x
        self.y = y
        self.direction = direction
        self.asteroid = asteroid
        if self.x > self.asteroid.width:
            raise MissAsteroidError()
        if self.y > self.asteroid.height:
            raise MissAsteroidError()

    def turn_left(self):
        turns = {"E": "N",
                 "N": "W",
                 "W": "S",
                 "S": "E",
                 }
        self.direction = turns[self.direction]

    def turn_right(self):
        turns = {"E": "S",
                 "N": "E",
                 "W": "N",
                 "S": "W",
                 }
        self.direction = turns[self.direction]

    def move_forward(self):
        move = {
            "N": (0, 1),
            "E": (1, 0),
            "S": (0, -1),
            "W": (-1, 0),
        }
        self.__possibility_movement(move[self.direction])
        if self.direction == "N":
            self.y += 1
        elif self.direction == "E":
            self.x += 1
        elif self.direction == "S":
            self.y -= 1
        elif self.direction == "W":
            self.x -= 1

    def move_backward(self):
        move = {
            "N": (0, -1),
            "E": (-1, 0),
            "S": (0, 1),
            "W": (1, 0),
        }
        self.__possibility_movement(move[self.direction])
        if self.direction == "N":
            self.y -= 1
        elif self.direction == "E":
            self.x -= 1
        elif self.direction == "S":
            self.y += 1
        elif self.direction == "W":
            self.x += 1

    def __possibility_movement(self, move):
        if move[1] == 1:
            if self.y + 1 > self.asteroid.height:
                raise EndAsteroidError()
            for coordinates in self.asteroid.obstacles:
                if self.y + 1 == coordinates[1] and self.x == coordinates[0]:
                    raise ObstaclesOnAsteroidError()
        elif move[0] == 1:
            if self.x + 1 > self.asteroid.width:
                raise EndAsteroidError()
            for coordinates in self.asteroid.obstacles:
                if self.y == coordinates[1] and self.x + 1 == coordinates[0]:
                    raise ObstaclesOnAsteroidError()
        elif move[1] == -1:
            if self.y - 1 < 0:
                raise EndAsteroidError()
            for coordinates in self.asteroid.obstacles:
                if self.y - 1 == coordinates[1] and self.x == coordinates[0]:
                    raise ObstaclesOnAsteroidError()
        elif move[0] == -1:
            if self.x - 1 < 0:
                raise EndAsteroidError()
            for coordinates in self.asteroid.obstacles:
                if self.y == coordinates[1] and self.x - 1 == coordinates[0]:
                    raise ObstaclesOnAsteroidError()


class MissAsteroidError(Exception):
    pass


class EndAsteroidError(Exception):
    pass


class ObstaclesOnAsteroidError(Exception):
    pass

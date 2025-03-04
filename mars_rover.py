class MarsRover:
    def __init__(self, x: int, y: int, orientation: str) -> None:
        self.x = x
        self.y = y
        self.orientation = orientation

    def command(self, commands: list[str]): ...

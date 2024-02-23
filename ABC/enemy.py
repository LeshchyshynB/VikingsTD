class Enemy():
    def __init__(self, health, speed) -> None:
        self.health = health
        self.speed = speed

    def _move(self):
        ...


    def update(self):
        self._move()

from ..ABC.enemy import Enemy

class Warrior(Enemy):
    def __init__(self, health=300, speed=2) -> None:
        super().__init__(health, speed)


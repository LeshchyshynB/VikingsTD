from ..ABC.enemy import Enemy

class Villager(Enemy):
    def __init__(self, health=100, speed=1) -> None:
        super().__init__(health, speed)

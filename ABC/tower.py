import pygame

class Tower():
	def __init__(self, damage=0, distance=0, cooldown=0) -> None:
		self.damage = damage
		self.distance = distance
		self.cooldown = cooldown

		self.ready = True
		self.cooldown_tracker = 0
		self.clock = pygame.time.Clock()

	def _attack(self, target):
		if self.ready:
			target.health -= self.damage 
			self.ready = False
		
	def _cooldown(self):
		self.cooldown_tracker += self.clock.get_time()
		if self.cooldown_tracker > 200:
			self.cooldown_tracker = 0
			self.ready = True

	def update(self, target):
		self._attack(target)
		self._cooldown()
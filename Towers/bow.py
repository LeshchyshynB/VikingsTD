from ..ABS.tower import Tower

class BowTower(Tower):

	def _cooldown(self):
		self.cooldown_tracker += self.clock.get_time()
		if self.cooldown_tracker > 500:
			self.cooldown_tracker = 0
			self.ready = True
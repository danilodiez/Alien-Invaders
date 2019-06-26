

class GameStats():
	'''lleva las estadisticas del juego'''

	def __init__(self, ai_settings):
		"""constructor"""
		self.ai_settings = ai_settings
		self.reset_stats()
		#pone al juego en un estado inactivo
		self.game_active = False
		self.high_score = 0

	def reset_stats(self):
		'''inicia las estadisticas que cambian durante el juego'''
		self.ships_left = self.ai_settings.ship_limit
		self.score = 0
		self.level = 1
		self.ai_settings.ship_speed_factor = 3
		self.ai_settings.bullet_speed_factor = 3
		self.ai_settings.alien_speed_factor = 0.5
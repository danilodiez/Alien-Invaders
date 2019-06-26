import pygame.font
from pygame.sprite import Group
from ship import Ship


class Scoreboard():
	"""clase para guardar puntaje"""

	def __init__(self, ai_settings, screen, stats):
		#inicia el marcador
		self.screen = screen
		self.screen_rect = screen.get_rect()
		self.ai_settings = ai_settings
		self.stats = stats



		#tipo de fuente para la info
		self.text_color = (255, 255, 255)
		self.font = pygame.font.SysFont(None, 50)


		#prepara la imagen inicial del tablero
		self.prep_score()
		self.prep_high_score()
		self.prep_level()
		self.prep_ships()



	def prep_score(self):
		#convierte el puntaje en una imagen
		rounded_score = int(round(self.stats.score, -1))
		score_str = "{:,}".format(rounded_score)
		self.score_image = self.font.render(score_str, True, self.text_color,
			self.ai_settings.bg_color)	

		#muestra el puntaje en el borde superior derecho
		self.score_rect = self.score_image.get_rect()
		self.score_rect.right = self.screen_rect.right - 20
		self.score_rect.top = 20


	def show_score(self):
		'''dibuja en pantalla el cuadro del puntaje'''
		self.screen.blit(self.score_image, self.score_rect)
		self.screen.blit(self.high_score_image, self.high_score_rect)
		self.screen.blit(self.level_image, self.level_rect)
		#dibuja las naves
		self.ships.draw(self.screen)



	def prep_high_score(self):
		high_score = int(round(self.stats.high_score, -1))
		high_score_str = "{:,}".format(high_score)
		self.high_score_image = self.font.render(high_score_str, True,
			self.text_color, self.ai_settings.bg_color)

		#centra el high score
		self.high_score_rect = self.high_score_image.get_rect()
		self.high_score_rect.centerx = self.screen_rect.centerx
		self.high_score_rect.top = self.score_rect.top




	def prep_level(self):
		#convierte el nivel en una imagen
		self.level_image = self.font.render('NIVEL: '+str(self.stats.level), True,
			self.text_color, self.ai_settings.bg_color)

		#Pone el nivel abajo del marcador
		self.level_rect = self.level_image.get_rect()
		self.level_rect.right = self.score_rect.right
		self.level_rect.top = self.score_rect.bottom + 10	


	def prep_ships(self):
		"""muestra cuantas naves/vidas quedan"""
		self.ships = Group()
		for ship_number in range(self.stats.ships_left):
			ship = Ship(self.ai_settings, self.screen)
			ship.rect.x = ship_number * ship.rect.width
			ship.rect.y = -35
			self.ships.add(ship)

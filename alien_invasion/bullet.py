import pygame

from pygame.sprite import *

class Bullet(Sprite):
	"""Clase para manejar el disparo de las balas"""

	def __init__(self, ai_settings, screen, ship):
		"""Crea un objeto de bala en la posicion de la nace"""
		super(Bullet, self).__init__()
		self.screen = screen

		#Crea un rect de la bala en (0, 0) y despues pone la pos correcta
		self.rect = pygame.Rect(0, 0, ai_settings.bullet_width,
			ai_settings.bullet_height)
		self.rect.centerx = ship.rect.centerx-5
		self.rect.bottom = ship.rect.top+50
		#almacena la posicion de la bala como un valor decimal
		self.y = float(self.rect.y)

		self.color = ai_settings.bullet_color
		self.speed_factor = ai_settings.bullet_speed_factor


	def update(self):
		"""mueve la bala en la pantalla"""

		#actualiza la pos de la bala
		self.y -= self.speed_factor
		#actualiza la pos del rect
		self.rect.y = self.y

	def draw_bullet(self):
		#dibuja la bala en pantalla
		pygame.draw.rect(self.screen, self.color, self.rect)
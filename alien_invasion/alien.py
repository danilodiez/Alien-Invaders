import pygame
from pygame.sprite import Sprite 


class Alien(Sprite):
	"""clase que representa a UN alien"""

	def __init__(self,ai_settings, screen):
		"""Inicia el alien y su posicion inicial"""
		super(Alien, self).__init__()
		self.screen = screen
		self.ai_settings = ai_settings


		#carga la imagen del alien
		self.image = pygame.image.load('alien.png')
		self.rect = self.image.get_rect()

		#empieza cada alien cerca en la esquina sup izq
		self.rect.x=self.rect.width
		self.rect.y = self.rect.height


		#guarda la pos del alien
		self.x = float(self.rect.x)


	def blitme(self):
		"""dibuja el alien y su posicion"""
		self.screen.blit(self.image, self.rect)



	def check_edges(self):
		"""devuelve True si un alien choca el borde"""
		screen_rect = self.screen.get_rect()
		if self.rect.right >= screen_rect.right:
			return True
		elif self.rect.left <=0:
			return True


	def update(self):
		"""mueve los aliens a la derecha o izquierda"""
		self.x += (self.ai_settings.alien_speed_factor * 
						self.ai_settings.fleet_direction)
		self.rect.x = self.x
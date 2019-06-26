import pygame
from pygame.sprite import Sprite

class Ship(Sprite):

	def __init__(self, ai_settings, screen):
		#Inicia la nave y su posicion inicial
		super(Ship, self).__init__()
		self.screen=screen 
		self.ai_settings = ai_settings

		#carga la imagen de la nave
		self.image = pygame.image.load('nave.png')
		self.rect = self.image.get_rect()
		self.screen_rect = screen.get_rect()

		#pone cada nave nueva abajo en el centro de la pantalla
		self.rect.centerx = self.screen_rect.centerx
		self.rect.bottom = self.screen_rect.bottom

		#Asigna un valor decimal al centro de la nave
		self.center = float(self.rect.centerx)
		
		#flag de movimiennto
		self.moving_right = False
		self.moving_left = False

	def update(self):
		"""Actualiza la posicion de la nave con el flag"""
		if self.moving_right and self.rect.right <self.screen_rect.right:	
			self.center += self.ai_settings.ship_speed_factor
		if self.moving_left and self.rect.left>0:	
			self.center -= self.ai_settings.ship_speed_factor		

		self.rect.centerx = self.center	
			


	def blitme(self):
		#dibuja la nave en su posicion correspondiente
		self.screen.blit(self.image, self.rect)	


	def center_ship(self):
		"""centra la nave en la pantalla"""
		self.center = self.screen_rect.centerx	
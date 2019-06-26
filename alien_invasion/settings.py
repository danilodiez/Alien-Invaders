
import pygame


class Settings():
	"""Una clase para almacenar las configs del juego"""

	def __init__(self):
		"""arranca las configs del juego"""
		#configs de la pantalla
		self.screen_width = 1200
		self.screen_height = 800
		self.bg_color = (75, 0, 130)
		# ajustes de la nave
		self.ship_speed_factor = 3
		self.ship_limit = 2
		#Configs de las balas
		self.bullet_speed_factor = 3
		self.bullet_width = 7
		self.bullet_height = 20
		self.bullet_color = (235,216,0) #Color oro metalico
		self.speedup_scale = 1.5
		#Configs del alien
		self.alien_speed_factor = 7
		self.fleet_drop_speed = 50
		#+1 a la derecha, -1 a la izquierda
		self.fleet_direction = 1

		#puntaje
		self.alien_points = 50

		#que tan rapido aumenta el puntaje
		self.score_scale = 1.4


	def increase_speed(self):
		"""aumenta las velocidades"""
		self.ship_speed_factor *= self.speedup_scale	
		self.bullet_speed_factor *=self.speedup_scale	
		self.alien_speed_factor *=self.speedup_scale

		self.alien_points = int(self.alien_points * self.score_scale)

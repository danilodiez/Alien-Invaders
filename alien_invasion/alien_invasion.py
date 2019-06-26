import sys
from settings import Settings
import pygame
from ship import Ship
import game_functions as gf
from pygame.sprite import Group
import bullet
from pygame.locals import *
from game_stats import GameStats
from button import Button
from pygame import *
from scoreboard import Scoreboard


def run_game():
	# Inicia el juego y arranca objetos en la pantalla.
	clock=pygame.time.Clock
	pygame.init()
	ai_settings = Settings()
	screen = pygame.display.set_mode(
		(ai_settings.screen_width, ai_settings.screen_height))
	pygame.display.set_caption('Alien Invasion')

	#crea el boton de play
	play_button = Button(ai_settings, screen, 'JUGAR')

	#crea una instancia de las estadisticas
	stats = GameStats(ai_settings)
	sb = Scoreboard(ai_settings, screen, stats)
	#crea una nave
	ship = Ship(ai_settings, screen)
	
	#grupo para almacenar las balas
	bullets = Group()

	#grupo para los aliens
	aliens = Group()

	#crea los aliens
	gf.create_fleet(ai_settings,screen, ship, aliens)

	#cancion del juego

	pygame.mixer.music.load('tono american gods.ogg')
	pygame.mixer.music.play(-1)
	pygame.mixer.music.set_volume(1)
	#sonido de un disparo
	bullet_sound = pygame.mixer.Sound('bullet sound.wav')
	bullet_sound.set_volume(0.1)




	# Comienza el bucle del juego.

	while True:

		# Espera las acciones del mouse y el teclado.
		gf.check_events(ai_settings, screen, stats,sb, play_button, ship, 
			aliens, bullets, bullet_sound)
		
		if stats.game_active:
			ship.update()
			gf.update_bullets(ai_settings, screen, stats, sb,
			 ship, aliens, bullets)
			gf.update_aliens(ai_settings,screen, stats, sb, ship, aliens,
			 bullets)
			
		
		gf.update_screen(ai_settings, screen, stats, sb, ship,aliens, bullets,
			play_button)



	
run_game()

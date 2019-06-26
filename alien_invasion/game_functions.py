import sys
import pygame
from bullet import Bullet
from alien import Alien
from time import sleep
from pygame import *


def check_keydown_events(event,ai_settings,screen, ship, bullets, bullet_sound):
	"""Responde a apretar teclas"""
	if event.key == pygame.K_RIGHT:
		ship.moving_right = True
	elif event.key == pygame.K_LEFT:
		ship.moving_left = True
	elif event.key == pygame.K_SPACE:
		fire_bullet(ai_settings, screen, ship, bullets)
		pygame.mixer.Sound.play(bullet_sound)



def check_keyup_events(event, ship):
	"""Para dejar de apretar la tecla"""
	if event.key == pygame.K_RIGHT:
		ship.moving_right = False
	elif event.key == pygame.K_LEFT:
		ship.moving_left = False

def check_events(ai_settings,screen,stats, sb,  play_button, ship,aliens,
	bullets, bullet_sound):
	"""resonde a los eventos del mouse y del teclado"""

	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			sys.exit()

		elif event.type == pygame.KEYDOWN:
			check_keydown_events(event,ai_settings, screen, ship, bullets, bullet_sound)
		elif event.type == pygame.KEYUP:
			check_keyup_events(event, ship)
		elif event.type == pygame.MOUSEBUTTONDOWN:
			mouse_x, mouse_y = pygame.mouse.get_pos()	
			check_play_button(ai_settings, screen, stats,sb,  play_button,
				ship, aliens, bullets,mouse_x, mouse_y)


def check_play_button(ai_settings, screen,stats, sb,  play_button, ship,
	aliens, bullets, mouse_x, mouse_y):
	""" comienza el juego cuando se apriete jugar"""
	button_clicked = play_button.rect.collidepoint(mouse_x, mouse_y)
	if button_clicked and not stats.game_active:
		#esconde el cursor
		pygame.mouse.set_visible(False)	

		#reinicia las estadisticas
		stats.reset_stats()
		stats.game_active = True

		#resetea las imagenes de los tableros
		sb.prep_score()
		sb.prep_high_score()
		sb.prep_level()
		sb.prep_ships()

		#vacia la lista de aliens y de balas
		aliens.empty()
		bullets.empty()

		#vuelve a crear una flota de aliens
		create_fleet(ai_settings,screen, ship, aliens)
		ship.center_ship()

def update_screen(ai_settings, screen, stats, sb, ship, aliens, bullets,
	play_button):
	
	#Dibuja las pantallas detras de las naves y los aliens

	"""Actualiza imagenes en la pantalla y setea pantallas nuevas"""
	screen.fill(ai_settings.bg_color)
	for bullet in bullets.sprites():

		bullet.draw_bullet()
	
	# Hace visible la pantalla (?)

	ship.blitme()	
	aliens.draw(screen)
	

	#dibuja el tablero
	sb.show_score()

	#dibuja el boton de Jugar cuando el juego este inactivo
	if not stats.game_active:
		play_button.draw_button()

	pygame.display.flip()	




def update_bullets(ai_settings, screen, stats, sb,
 ship, aliens, bullets):
	"""actualiza la posicion de las balas y las borra"""
	bullets.update()

	#Borrar las balas fuera de pantalla
	for bullet in bullets.copy():
		if bullet.rect.top<=0:
			bullets.remove(bullet)

	#print(len(bullets))	para ver cuantas balas estan en juego	

	check_bullet_alien_collisions(ai_settings, screen,
	stats, sb, ship, aliens, bullets)





def check_bullet_alien_collisions(ai_settings, screen, stats,
sb, ship, aliens, bullets):
	#analiza y borra un alien si choco contra una bala
	collisions = pygame.sprite.groupcollide(bullets, aliens, True, True)
	if collisions:
		for aliens in collisions.values():

			stats.score += ai_settings.alien_points * len(aliens)
			sb.prep_score()
		check_high_score(stats, sb)	
	if len(aliens) == 0:
		#borra las balas y crea otra flota
		bullets.empty()
		create_fleet(ai_settings, screen, ship, aliens)
		#sube de nivel
		stats.level += 1
		sb.prep_level()
		ai_settings.increase_speed()

def fire_bullet (ai_settings, screen, ship, bullets):
	#crea una bala y la agraga a Group
	new_bullet = Bullet(ai_settings,screen,ship)
	bullets.add(new_bullet)



def get_number_aliens_x(ai_settings, alien_width):
	"""determina cuantos aliens entran en cada fila"""
	available_space_x = ai_settings.screen_width - 2 * alien_width
	number_aliens_x = int(available_space_x / (alien_width))
	return number_aliens_x



def get_number_rows(ai_settings, ship_height, alien_height):
	"""determina cuantas filas de aliens entran en pantalla"""
	available_space_y = (ai_settings.screen_height-
		( alien_height) - 1.5 * ship_height)
	number_rows = int(available_space_y / (1.5 * alien_height))
	return number_rows

def create_alien(ai_settings, screen, aliens, alien_number, row_number):
	"""crea un alien y lo pone en la fila"""
	alien = Alien(ai_settings, screen)
	alien_width = alien.rect.width
	alien.x = alien_width + 1.5*alien_width * alien_number
	alien.rect.x = alien.x
	alien.rect.y = alien.rect.height + 1.3 * alien.rect.height * row_number
	aliens.add(alien)

def create_fleet (ai_settings, screen, ship, aliens):
	"""crea una flota entera de aliens"""
	#crea un alien y encuentra el numero de aliens en una fila
	#el espacio entre cada alien es igual a un alien de ancho
	alien = Alien(ai_settings, screen)
	number_aliens_x = get_number_aliens_x(ai_settings, alien.rect.width)
	number_rows = get_number_rows(ai_settings, ship.rect.height,
		alien.rect.height)
	#crea la flota de aliens
	for row_number in range(number_rows):
		for alien_number in range(9):
			#crea un alien y lo pone en la fila
			create_alien(ai_settings,screen, aliens, alien_number,
				row_number)




def check_fleet_edges(ai_settings, aliens):
	"""responde a los cambios si la flota toca un borde"""
	for alien in aliens.sprites():
		if alien.check_edges():
			change_fleet_direction(ai_settings, aliens)
			break


def change_fleet_direction(ai_settings, aliens):
	"""baja toda la flota y cambia la direccion"""
	for alien in aliens.sprites():
		alien.rect.y += ai_settings.fleet_drop_speed
	ai_settings.fleet_direction *= -1





def ship_hit(ai_settings, screen, stats, sb, ship, aliens, bullets):
	"""responde a las colisiones"""
	if stats.ships_left >0:
		#resta una nave
		stats.ships_left -= 1

		#actualiza el tablero
		sb.prep_ships()

		#vacia las listas de aliens y balas
		aliens.empty()
		bullets.empty()

		#crea una flota nueva y centra a la nave
		create_fleet(ai_settings, screen, ship, aliens)
		ship.center_ship()

		#pausa
		sleep(2)
	else:
		stats.game_active = False	
		pygame.mouse.set_visible(True)

def check_aliens_bottom(ai_settings, screen, stats, sb, ship, aliens, bullets):
	'''detecta si un alien lleva abajo'''
	screen_rect = screen.get_rect()
	for alien in aliens.sprites():
		if alien.rect.bottom >= screen_rect.bottom:
			"""igual que si choca la nave"""
			ship_hit(ai_settings, screen, stats, sb, ship, aliens, bullets)
			break




def update_aliens(ai_settings,screen, stats, sb, ship, aliens, bullets):
	"""actualiza las posiciones de la flota"""
	check_fleet_edges(ai_settings, aliens)
	aliens.update()


	#detecta las colisiones nave-aliens
	if pygame.sprite.spritecollideany(ship, aliens):
		ship_hit(ai_settings, screen, stats,
		sb, ship, aliens, bullets)

	check_aliens_bottom(ai_settings,screen, stats, 
		sb, ship, aliens, bullets)	




def check_high_score(stats, sb):
	#detecta si hay un nuevo high score
	if stats.score > stats.high_score:
		stats.high_score = stats.score
		sb.prep_high_score()
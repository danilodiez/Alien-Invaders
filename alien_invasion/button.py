import pygame.font


class Button():

	def __init__(self, ai_settings, screen, msg):

		#atributos del boton
		self.screen = screen
		self.screen_rect = screen.get_rect()


		#dimensiones y props del boton
		self.width, self.height = 300,100
		self.button_color = (0, 250, 154) #verde agua
		self.text_color = (255, 255, 255) #blanco
		self.font =  pygame.font.SysFont(None, 48)


		#consturye el boton como un rect y lo centra
		self.rect = pygame.Rect(0, 0, self.width, self.height)
		self.rect.center = self.screen_rect.center

		#el mensaje se muestra una vez
		self.prep_msg(msg)


	def prep_msg(self, msg):
		"""pygame muestra mensajes convirtiendo texto a imagenes"""
		self.msg_image = self.font.render(msg, True, self.text_color,
			self.button_color)
		self.msg_image_rect = self.msg_image.get_rect()
		self.msg_image_rect.center = self.rect.center	


	def draw_button(self):
		#dibuja un boton vacio y le coloca la imagen
		self.screen.fill(self.button_color, self.rect)
		self.screen.blit(self.msg_image, self.msg_image_rect)		
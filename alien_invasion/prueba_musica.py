from pygame import *


def musica():
	mixer.init()
	mixer.music.load('tono american gods.ogg')
	mixer.music.play()

	while mixer.music.get_busy():
	time.Clock().tick(10)

input()	
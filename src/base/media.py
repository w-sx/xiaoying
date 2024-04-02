from pygame import mixer
import base.file as file

def init(uninit=False):
	if uninit: mixer.quit()
	else: mixer.init()

def sound(filename):
	if not mixer.get_init(): init()
	if not file.exists(filename): return
	return mixer.Sound(filename).play()

def music(filename) -> mixer.music:
	if not mixer.get_init(): init()
	if not file.exists(filename): return
	mixer.music.load(filename)
	mixer.music.play()
	return mixer.music

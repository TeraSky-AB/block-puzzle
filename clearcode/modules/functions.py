import pygame as pg

def isOnGrid(pos):
	if pos[0] > 65 and pos[0] < 65+320 and pos[1] > 65 and pos[1] < 65+320:
		return True
	else:
		return False

def quitGame():
	pg.display.quit()
	quit()
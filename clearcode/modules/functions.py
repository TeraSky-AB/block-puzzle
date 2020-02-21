import pygame as pg

def isOnGrid(pos):
	if pos[0] > 50 and pos[0] < 50+320 and pos[1] > 50 and pos[1] < 50+320:
		return True
	else:
		return False

def quitGame():
	pg.display.quit()